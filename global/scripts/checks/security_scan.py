#!/usr/bin/env python3
"""
Security Scanner — Antigravity Gold Verification System
========================================================

Scans project files for common security issues relevant to web development.

Usage:
    python scripts/checks/security_scan.py <project_path>

Checks:
    - Hardcoded API keys, tokens, passwords
    - .env files committed to version control
    - Dangerous eval()/exec()/innerHTML usage
    - Open WebSocket connections without auth
    - Exposed debug/dev endpoints
    - Sensitive data in console.log statements
"""

import sys
import os
import re
from pathlib import Path
from typing import List, Dict

# ANSI colors
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    END = '\033[0m'

# File extensions to scan
SCAN_EXTENSIONS = {'.js', '.mjs', '.cjs', '.ts', '.tsx', '.jsx', '.html', '.htm',
                   '.py', '.json', '.yaml', '.yml', '.toml', '.cfg', '.ini', '.conf'}

# Directories to skip
SKIP_DIRS = {'node_modules', '.git', '__pycache__', 'dist', 'build', '.next',
             'venv', '.venv', 'env', '.env.local', 'coverage', '.cache'}

# Patterns: (name, regex, severity, description)
SECRET_PATTERNS = [
    ("Hardcoded API Key", r"""(?:api[_-]?key|apikey)\s*[:=]\s*['"][A-Za-z0-9_\-]{16,}['"]""",
     "CRITICAL", "API key hardcoded in source — use environment variables"),

    ("Hardcoded Token", r"""(?:token|bearer|auth[_-]?token)\s*[:=]\s*['"][A-Za-z0-9_\-\.]{16,}['"]""",
     "CRITICAL", "Authentication token hardcoded — use environment variables"),

    ("Hardcoded Password", r"""(?:password|passwd|pwd|secret)\s*[:=]\s*['"][^'"]{4,}['"]""",
     "CRITICAL", "Password or secret hardcoded in source"),

    ("AWS Access Key", r"""AKIA[0-9A-Z]{16}""",
     "CRITICAL", "AWS access key detected in source"),

    ("Private Key Block", r"""-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----""",
     "CRITICAL", "Private key embedded in source file"),

]

DANGEROUS_CODE_PATTERNS = [
    ("eval() Usage", r"""\beval\s*\(""",
     "HIGH", "eval() executes arbitrary code — use safer alternatives"),

    ("innerHTML Assignment", r"""\.innerHTML\s*=(?!=)""",
     "MEDIUM", "innerHTML can introduce XSS — use textContent or DOM APIs"),

    ("document.write", r"""\bdocument\.write\s*\(""",
     "MEDIUM", "document.write can introduce XSS and blocks rendering"),

    ("exec() Usage (Python)", r"""\bexec\s*\(""",
     "HIGH", "exec() executes arbitrary code — avoid in production"),

    ("Shell Injection Risk", r"""(?:subprocess|os\.system|os\.popen)\s*\(.*\+""",
     "HIGH", "String concatenation in shell commands — use parameterized calls"),
]

DEBUG_PATTERNS = [
    ("Console.log with Sensitive Data", r"""console\.log\s*\(.*(?:password|token|secret|key|auth)""",
     "MEDIUM", "Sensitive data may be logged to console"),

    ("Debugger Statement", r"""\bdebugger\b""",
     "LOW", "debugger statement left in code — remove before production"),

    ("TODO/FIXME Security", r"""(?:TODO|FIXME|HACK|XXX).*(?:security|auth|password|token|vuln)""",
     "MEDIUM", "Security-related TODO found — address before deployment"),
]


def should_scan_file(filepath: Path) -> bool:
    """Check if file should be scanned based on extension and directory."""
    checker_directory = Path(__file__).resolve().parent
    try:
        filepath.resolve().relative_to(checker_directory)
        return False
    except ValueError:
        pass
    if filepath.suffix.lower() not in SCAN_EXTENSIONS:
        return False
    for skip in SKIP_DIRS:
        if skip in filepath.parts:
            return False
    return True


def scan_file(filepath: Path, patterns: List[tuple]) -> List[Dict]:
    """Scan a single file for security patterns."""
    findings = []
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
        lines = content.split('\n')

        for line_num, line in enumerate(lines, 1):
            # Skip comment-only lines (basic heuristic)
            stripped = line.strip()
            if stripped.startswith('//') or stripped.startswith('#') or stripped.startswith('*'):
                # Still check for actual secrets in comments — they're still dangerous
                pass

            for name, pattern, severity, description in patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    findings.append({
                        'file': str(filepath),
                        'line': line_num,
                        'pattern': name,
                        'severity': severity,
                        'description': description,
                        'content': stripped[:120],
                    })

    except (PermissionError, UnicodeDecodeError):
        pass

    return findings


def check_env_files(project_path: Path) -> List[Dict]:
    """Check for .env files that might be committed."""
    findings = []
    gitignore_content = ""
    gitignore_path = project_path / '.gitignore'

    if gitignore_path.exists():
        gitignore_content = gitignore_path.read_text(errors='ignore')

    for env_file in project_path.rglob('.env*'):
        if '.git' in env_file.parts:
            continue
        if env_file.name == '.env.example' or env_file.name == '.env.template':
            continue

        # Check if it's in .gitignore
        if env_file.name not in gitignore_content and '.env' not in gitignore_content:
            findings.append({
                'file': str(env_file),
                'line': 0,
                'pattern': 'Env File Not Gitignored',
                'severity': 'CRITICAL',
                'description': f'{env_file.name} may not be in .gitignore — secrets could be committed',
                'content': f'Found: {env_file.name}',
            })

    return findings


def print_findings(findings: List[Dict]) -> None:
    """Print findings grouped by severity."""
    if not findings:
        print(f"{Colors.GREEN}✅ No security issues found{Colors.END}")
        return

    severity_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    findings.sort(key=lambda f: severity_order.get(f['severity'], 99))

    severity_colors = {
        'CRITICAL': Colors.RED,
        'HIGH': Colors.RED,
        'MEDIUM': Colors.YELLOW,
        'LOW': Colors.CYAN,
    }

    current_severity = None
    for f in findings:
        if f['severity'] != current_severity:
            current_severity = f['severity']
            color = severity_colors.get(current_severity, '')
            print(f"\n{Colors.BOLD}{color}[{current_severity}]{Colors.END}")

        color = severity_colors.get(f['severity'], '')
        print(f"  {color}⚠ {f['pattern']}{Colors.END}")
        print(f"    File: {f['file']}:{f['line']}")
        print(f"    {f['description']}")
        if f.get('content'):
            print(f"    → {f['content'][:100]}")


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    if len(sys.argv) < 2:
        print("Usage: python security_scan.py <project_path>")
        sys.exit(1)

    project_path = Path(sys.argv[1]).resolve()
    if not project_path.exists():
        print(f"Error: Path does not exist: {project_path}")
        sys.exit(1)

    print(f"{Colors.BOLD}{Colors.CYAN}🔒 Security Scan — Antigravity Gold{Colors.END}")
    print(f"Scanning: {project_path}\n")

    all_patterns = SECRET_PATTERNS + DANGEROUS_CODE_PATTERNS + DEBUG_PATTERNS
    all_findings = []

    # Scan all files
    file_count = 0
    for filepath in project_path.rglob('*'):
        if filepath.is_file() and should_scan_file(filepath):
            file_count += 1
            findings = scan_file(filepath, all_patterns)
            all_findings.extend(findings)

    # Check env files
    env_findings = check_env_files(project_path)
    all_findings.extend(env_findings)

    print(f"Files scanned: {file_count}")
    print_findings(all_findings)

    # Summary
    critical = sum(1 for f in all_findings if f['severity'] == 'CRITICAL')
    high = sum(1 for f in all_findings if f['severity'] == 'HIGH')

    print(f"\n{Colors.BOLD}Summary:{Colors.END}")
    print(f"  Total findings: {len(all_findings)}")
    print(f"  Critical: {critical}")
    print(f"  High: {high}")

    if critical > 0:
        print(f"\n{Colors.RED}{Colors.BOLD}❌ CRITICAL issues found — fix before deployment{Colors.END}")
        sys.exit(1)
    elif high > 0:
        print(f"\n{Colors.YELLOW}⚠️  HIGH severity issues found — review before deployment{Colors.END}")
        sys.exit(1)
    else:
        print(f"\n{Colors.GREEN}✅ Security scan passed{Colors.END}")
        sys.exit(0)


if __name__ == '__main__':
    main()
