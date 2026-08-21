# Anti-Gravity OS - safe Windows installer
# Examples:
#   .\install.ps1 -IDE 1 -InstallOption general -DryRun
#   .\install.ps1 -IDE 1 -InstallOption full -Yes
#   .\install.ps1 -TargetHost antigravity -GlobalConfig $HOME\.gemini -Yes
#   .\install.ps1 -GlobalConfig C:\path\to\config-parent -Yes
#   .\install.ps1 -TargetHost antigravity -InstallScope workspace -WorkspacePath C:\path\to\project -DryRun

[CmdletBinding()]
param(
    [string]$GlobalConfig,
    [string]$IDE,
    [ValidateSet('antigravity', 'gemini', 'codex', 'cursor', 'windsurf', 'opencode')]
    [string]$TargetHost,
    [ValidateSet('general', 'full')]
    [string]$InstallOption,
    [ValidateSet('global', 'workspace')]
    [string]$InstallScope,
    [string]$WorkspacePath,
    [switch]$DryRun,
    [switch]$Yes,
    [switch]$AntigravityGlobal
)

$ErrorActionPreference = 'Stop'

function Write-Step([string]$Message) { Write-Host "`n> $Message" -ForegroundColor Cyan }
function Write-Success([string]$Message) { Write-Host "  OK  $Message" -ForegroundColor Green }
function Write-Warn([string]$Message) { Write-Host "  WARN  $Message" -ForegroundColor Yellow }

function Get-FullPath([string]$Path) {
    if ([string]::IsNullOrWhiteSpace($Path)) {
        throw 'Install path cannot be empty.'
    }

    $expanded = [Environment]::ExpandEnvironmentVariables($Path.Trim().Trim('"'))
    if ($expanded.StartsWith('~')) {
        $expanded = Join-Path $env:USERPROFILE $expanded.Substring(1).TrimStart('\', '/')
    }
    return [IO.Path]::GetFullPath($expanded)
}

function Add-Namespace([string]$Path) {
    $fullPath = Get-FullPath $Path
    if ([IO.Path]::GetFileName($fullPath.TrimEnd('\', '/')) -ieq 'antigravity') {
        return $fullPath.TrimEnd('\', '/')
    }
    return Join-Path $fullPath 'antigravity'
}

function Select-InstallTarget {
    if ($GlobalConfig) {
        if (-not $TargetHost) {
            throw 'Custom/global config targets require -TargetHost antigravity|gemini|codex|cursor|windsurf|opencode.'
        }
        if ($TargetHost -eq 'antigravity') {
            $script:AntigravityGlobal = $true
            return Get-FullPath $GlobalConfig
        }
        if ($TargetHost -eq 'codex') {
            return Get-FullPath $GlobalConfig
        }
        return Add-Namespace $GlobalConfig
    }

    if ($TargetHost -and -not $IDE) {
        switch ($TargetHost) {
            'antigravity' { $script:AntigravityGlobal = $true; return Join-Path $env:USERPROFILE '.gemini' }
            'gemini' { return Join-Path $env:USERPROFILE '.gemini\antigravity' }
            'codex' { return Join-Path $env:USERPROFILE '.codex' }
            'cursor' { return Join-Path $env:USERPROFILE '.cursor\rules\antigravity' }
            'windsurf' { return Join-Path $env:USERPROFILE '.codeium\windsurf\memories\antigravity' }
            'opencode' { return Join-Path $env:USERPROFILE '.config\opencode\antigravity' }
            default { throw "Unsupported host '$TargetHost'." }
        }
    }

    if (-not $IDE) {
        Write-Host @"
Choose a host:
  [1] Antigravity 2.0                -> ~/.gemini (global) or a project workspace
  [2] Gemini compatibility namespace -> ~/.gemini/antigravity
  [3] Codex                         -> ~/.codex (global) or a project workspace
  [4] Cursor                        -> ~/.cursor/rules/antigravity
  [5] Windsurf                      -> ~/.codeium/windsurf/memories/antigravity
  [6] OpenCode                      -> ~/.config/opencode/antigravity
  [7] Custom parent directory
"@
        $script:IDE = Read-Host 'Enter 1-7'
    }

    switch ($IDE.Trim()) {
        '1' { $script:TargetHost = 'antigravity'; $script:AntigravityGlobal = $true; return Join-Path $env:USERPROFILE '.gemini' }
        '2' { $script:TargetHost = 'gemini'; return Join-Path $env:USERPROFILE '.gemini\antigravity' }
        '3' { $script:TargetHost = 'codex'; return Join-Path $env:USERPROFILE '.codex' }
        '4' { $script:TargetHost = 'cursor'; return Join-Path $env:USERPROFILE '.cursor\rules\antigravity' }
        '5' { $script:TargetHost = 'windsurf'; return Join-Path $env:USERPROFILE '.codeium\windsurf\memories\antigravity' }
        '6' { $script:TargetHost = 'opencode'; return Join-Path $env:USERPROFILE '.config\opencode\antigravity' }
        '7' {
            if (-not $TargetHost) {
                $script:TargetHost = (Read-Host 'Supported host (antigravity, gemini, codex, cursor, windsurf, opencode)').Trim().ToLowerInvariant()
            }
            if ($TargetHost -eq 'antigravity') {
                $script:AntigravityGlobal = $true
                return Get-FullPath (Read-Host 'Enter the .gemini directory')
            }
            if ($TargetHost -eq 'codex') {
                return Get-FullPath (Read-Host 'Enter the .codex directory for a global install')
            }
            if ($TargetHost -notin @('gemini', 'codex', 'cursor', 'windsurf', 'opencode')) {
                throw "Unsupported host '$TargetHost'."
            }
            return Add-Namespace (Read-Host 'Enter a parent directory for the antigravity namespace')
        }
        default { throw "Unknown host choice '$IDE'. Use 1-6." }
    }
}

function Select-InstallScope {
    if ($InstallScope) {
        if ($TargetHost -notin @('antigravity', 'codex') -and $InstallScope -eq 'workspace') {
            throw 'Workspace installation is currently supported for Antigravity and Codex only.'
        }
        return $InstallScope
    }
    if ($AntigravityGlobal -and $TargetHost -eq 'antigravity') {
        return 'global'
    }
    if ($TargetHost -notin @('antigravity', 'codex')) {
        return 'global'
    }
    if ($Yes -or [Console]::IsInputRedirected) {
        return 'global'
    }

    Write-Host @"

Installation scope:
  [1] Global    - use this V4 $TargetHost setup across your projects.
  [2] Workspace - test or use it in one project only; global host configuration is unchanged.
"@
    $choice = (Read-Host 'Choose 1 or 2 [1]').Trim()
    if ([string]::IsNullOrWhiteSpace($choice)) { $choice = '1' }
    switch ($choice) {
        '1' { return 'global' }
        '2' { return 'workspace' }
        default { throw 'Choose 1 for Global or 2 for Workspace.' }
    }
}

function Get-PythonInvocation {
    foreach ($candidate in @(
        @{ Name = 'python3'; Prefix = @() },
        @{ Name = 'python'; Prefix = @() },
        @{ Name = 'py'; Prefix = @('-3') }
    )) {
        $command = Get-Command $candidate.Name -ErrorAction SilentlyContinue
        if ($command) {
            return @{ File = $command.Source; Prefix = $candidate.Prefix }
        }
    }
    return $null
}

function Get-ManifestCounts {
    $manifestPath = Join-Path $scriptRoot 'global\manifest.yaml'
    if (-not (Test-Path -LiteralPath $manifestPath)) {
        throw "Manifest not found: $manifestPath"
    }
    $manifest = Get-Content -LiteralPath $manifestPath -Raw -Encoding UTF8 | ConvertFrom-Json
    $generalSkills = @($manifest.skills | Where-Object { $_.profiles -contains 'general' }).Count
    return [pscustomobject]@{
        Agents = @($manifest.agents).Count
        Workflows = @($manifest.workflows).Count
        GeneralSkills = $generalSkills
        AllSkills = @($manifest.skills).Count
    }
}

function Select-InstallOption {
    if ($InstallOption) {
        return $InstallOption
    }

    $counts = Get-ManifestCounts
    $agentDescription = if ($TargetHost -eq 'codex') {
        "$($counts.Agents) canonical roles (5 specialist Codex agents)"
    } else {
        "$($counts.Agents) custom agents"
    }
    Write-Host @"

Your Installation Options:
  [1] General Profile - installs $agentDescription, $($counts.Workflows) workflows, and $($counts.GeneralSkills) General-profile skills. Spatial, Media, and Growth remain dormant.
  [2] Full System - installs $agentDescription, $($counts.Workflows) workflows, and all $($counts.AllSkills) registered skills, including Spatial, Media, and Growth.
"@
    $choice = (Read-Host 'Choose 1 or 2 [1]').Trim()
    if ([string]::IsNullOrWhiteSpace($choice)) { $choice = '1' }
    switch ($choice) {
        '1' { return 'general' }
        '2' { return 'full' }
        default { throw 'Choose 1 for General or 2 for Full System.' }
    }
}

function Resolve-HostPayload([string]$HostId, [switch]$PreviewOnly, [string]$Option) {
    $profileKey = if ($Option -eq 'full') { 'general+spatial+media+growth' } else { 'general' }
    $prebuilt = Join-Path $scriptRoot (Join-Path (Join-Path 'dist' $HostId) $profileKey)
    if (-not (Test-Path -LiteralPath (Join-Path $prebuilt 'adapter.json'))) {
        $legacyPayload = Join-Path $scriptRoot (Join-Path 'dist' $HostId)
        if (Test-Path -LiteralPath (Join-Path $legacyPayload 'adapter.json')) {
            $prebuilt = $legacyPayload
        }
    }
    if (Test-Path -LiteralPath (Join-Path $prebuilt 'adapter.json')) {
        return @{ Path = $prebuilt; Built = $false; PendingBuild = $false }
    }

    $python = Get-PythonInvocation
    if (-not $python) {
        throw "No prebuilt dist/$HostId payload and no Python 3 runtime were found. Use a release package containing dist/$HostId or install Python 3 and rerun."
    }
    if ($PreviewOnly) {
        return @{ Path = $prebuilt; Built = $false; PendingBuild = $true }
    }

    $cli = Join-Path $scriptRoot 'global\scripts\os.py'
    $arguments = @($python.Prefix) + @($cli, 'build', '--host', $HostId, '--profile', 'general')
    if ($Option -eq 'full') {
        $arguments += @('--packs', 'spatial,media,growth')
    }
    & $python.File @arguments
    if ($LASTEXITCODE -ne 0 -or -not (Test-Path -LiteralPath (Join-Path $prebuilt 'adapter.json'))) {
        throw "Failed to build the $HostId host payload. Run the repository validator, or use a release package containing dist/$HostId."
    }
    return @{ Path = $prebuilt; Built = $true; PendingBuild = $false }
}

function Assert-SafeTarget([string]$Target, [string]$Source) {
    $targetFull = Get-FullPath $Target
    $sourceFull = Get-FullPath $Source
    $targetLeaf = [IO.Path]::GetFileName($targetFull.TrimEnd('\', '/'))
    $root = [IO.Path]::GetPathRoot($targetFull).TrimEnd('\', '/')
    $targetParent = (Split-Path -Parent $targetFull).TrimEnd('\', '/')
    $userHome = (Get-FullPath $env:USERPROFILE).TrimEnd('\', '/')

    if ($targetLeaf -ine 'antigravity') {
        throw "Refusing non-namespaced target: $targetFull"
    }
    if ($targetFull.TrimEnd('\', '/') -ieq $root -or $targetFull.TrimEnd('\', '/') -ieq $userHome) {
        throw "Refusing dangerous target: $targetFull"
    }
    if ($targetParent -ieq $root) {
        throw "Refusing to install directly below a filesystem root: $targetFull"
    }
    if ($sourceFull.StartsWith($targetFull + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase) -or
        $targetFull.StartsWith($sourceFull + [IO.Path]::DirectorySeparatorChar, [StringComparison]::OrdinalIgnoreCase) -or
        $targetFull -ieq $sourceFull) {
        throw 'Source and target must not contain one another.'
    }
    if (Test-Path -LiteralPath $targetFull) {
        $item = Get-Item -LiteralPath $targetFull -Force
        if (($item.Attributes -band [IO.FileAttributes]::ReparsePoint) -ne 0) {
            throw "Refusing symlink/reparse-point target: $targetFull"
        }
    }
}

function Copy-DirectoryContents([string]$Source, [string]$Destination) {
    Get-ChildItem -LiteralPath $Source -Force | ForEach-Object {
        Copy-Item -LiteralPath $_.FullName -Destination $Destination -Recurse -Force
    }
}

function Configure-PortableUris([string]$Directory) {
    $targetUri = 'file:///' + $Directory.Replace('\', '/')
    $utf8WithoutBom = New-Object Text.UTF8Encoding($false)
    $replacementCount = 0
    Get-ChildItem -LiteralPath $Directory -Filter '*.md' -File -Recurse | ForEach-Object {
        $content = [IO.File]::ReadAllText($_.FullName)
        if ($content.Contains('{{GLOBAL_CONFIG_URI}}')) {
            [IO.File]::WriteAllText($_.FullName, $content.Replace('{{GLOBAL_CONFIG_URI}}', $targetUri), $utf8WithoutBom)
            $replacementCount++
        }
    }
    return $replacementCount
}

$scriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$target = Get-FullPath (Select-InstallTarget)
$InstallScope = Select-InstallScope
if ($TargetHost -in @('antigravity', 'codex') -and $InstallScope -eq 'workspace') {
    if ($GlobalConfig) {
        throw '-GlobalConfig is a global target. Use -WorkspacePath for a workspace installation.'
    }
    $workspaceCandidate = if ($WorkspacePath) { $WorkspacePath } else { (Get-Location).Path }
    $target = Get-FullPath $workspaceCandidate
}
$InstallOption = Select-InstallOption

if ($AntigravityGlobal -and $TargetHost -ne 'antigravity') {
    throw '-AntigravityGlobal is only valid with -TargetHost antigravity.'
}
if ($TargetHost -eq 'antigravity') {
    if ($PSBoundParameters.ContainsKey('AntigravityGlobal') -and $AntigravityGlobal -and $InstallScope -eq 'workspace') {
        throw '-AntigravityGlobal conflicts with -InstallScope workspace.'
    }
    $script:AntigravityGlobal = $InstallScope -eq 'global'
    $script:AntigravityWorkspace = $InstallScope -eq 'workspace'
}

if ($TargetHost -eq 'codex') {
    $script:CodexGlobal = $InstallScope -eq 'global'
    $script:CodexWorkspace = $InstallScope -eq 'workspace'
}

if ($script:AntigravityGlobal -or $script:AntigravityWorkspace) {
    $python = Get-PythonInvocation
    if (-not $python) {
        throw 'Native Antigravity installation needs Python 3. Install Python 3 or use a release package with the installer runtime.'
    }
    if (-not $DryRun -and -not $Yes) {
        $confirmation = Read-Host "Install into Antigravity $InstallScope target '$target'? Type INSTALL to continue"
        if ($confirmation -cne 'INSTALL') {
            Write-Warn 'Installation cancelled. No files were changed.'
            exit 0
        }
        $Yes = $true
    }
    $cli = Join-Path $scriptRoot 'global\scripts\os.py'
    $mode = if ($script:AntigravityGlobal) { '--antigravity-global' } else { '--antigravity-workspace' }
    $arguments = @($python.Prefix) + @(
        $cli, 'install', '--host', 'antigravity', '--target', $target,
        '--option', $InstallOption, $mode
    )
    if ($DryRun) { $arguments += '--dry-run' }
    else { $arguments += '--yes' }
    & $python.File @arguments
    exit $LASTEXITCODE
}

if ($script:CodexGlobal -or $script:CodexWorkspace) {
    $python = Get-PythonInvocation
    if (-not $python) {
        throw 'Native Codex installation needs Python 3. Install Python 3 or use a release package with the installer runtime.'
    }
    if (-not $DryRun -and -not $Yes) {
        $confirmation = Read-Host "Install into Codex $InstallScope target '$target'? Type INSTALL to continue"
        if ($confirmation -cne 'INSTALL') {
            Write-Warn 'Installation cancelled. No files were changed.'
            exit 0
        }
        $Yes = $true
    }
    $cli = Join-Path $scriptRoot 'global\scripts\os.py'
    $mode = if ($script:CodexGlobal) { '--codex-global' } else { '--codex-workspace' }
    $arguments = @($python.Prefix) + @(
        $cli, 'install', '--host', 'codex', '--target', $target,
        '--option', $InstallOption, $mode
    )
    if ($DryRun) { $arguments += '--dry-run' }
    else { $arguments += '--yes' }
    & $python.File @arguments
    exit $LASTEXITCODE
}

$payloadInfo = Resolve-HostPayload -HostId $TargetHost -PreviewOnly:$DryRun -Option $InstallOption
$installSource = Get-FullPath $payloadInfo.Path
Assert-SafeTarget -Target $target -Source $installSource
$parent = Split-Path -Parent $target
$timestamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$backupRoot = Join-Path $parent '.antigravity-backups'
$backup = Join-Path $backupRoot ($timestamp + '-' + [Guid]::NewGuid().ToString('N').Substring(0, 8))
$stage = Join-Path $parent ('.antigravity-stage-' + [Guid]::NewGuid().ToString('N'))
$sourceFileCount = if (Test-Path -LiteralPath $installSource) { (Get-ChildItem -LiteralPath $installSource -File -Recurse -Force).Count } else { 0 }

Write-Step 'Installation plan'
Write-Host "  Host: $TargetHost"
Write-Host "  Installation option: $InstallOption"
Write-Host "  Payload: $installSource"
if ($payloadInfo.PendingBuild) { Write-Host '  Payload action: build with global/scripts/os.py after approval' }
Write-Host "  Target: $target"
Write-Host "  Managed source files: $sourceFileCount"
if (Test-Path -LiteralPath $target) {
    Write-Host "  Existing namespace backup: $backup"
    Write-Host '  Existing extra files are retained in the staged replacement.'
} else {
    Write-Host '  Existing namespace: none'
}
Write-Host '  Shared parent directories are never cleared.'

if ($DryRun) {
    Write-Success 'Dry run complete. No files were written.'
    exit 0
}

if (-not $Yes) {
    $confirmation = Read-Host "Install only into '$target'? Type INSTALL to continue"
    if ($confirmation -cne 'INSTALL') {
        Write-Warn 'Installation cancelled. No files were changed.'
        exit 0
    }
}

$backupCreated = $false
$activated = $false
try {
    New-Item -ItemType Directory -Path $parent -Force | Out-Null
    New-Item -ItemType Directory -Path $stage | Out-Null

    if (Test-Path -LiteralPath $target) {
        Copy-DirectoryContents -Source $target -Destination $stage
    }
    if ($payloadInfo.PendingBuild) {
        $payloadInfo = Resolve-HostPayload -HostId $TargetHost -Option $InstallOption
        $installSource = Get-FullPath $payloadInfo.Path
    }
    Copy-DirectoryContents -Source $installSource -Destination $stage
    $uriCount = Configure-PortableUris -Directory $stage

    if (Test-Path -LiteralPath $target) {
        New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
        Move-Item -LiteralPath $target -Destination $backup
        $backupCreated = $true
    }

    Move-Item -LiteralPath $stage -Destination $target
    $activated = $true

    $adapterPath = Join-Path $target 'adapter.json'
    if (-not (Test-Path -LiteralPath $adapterPath)) {
        throw 'Post-install validation failed: adapter.json is missing.'
    }
    $instructionTarget = (Get-Content -LiteralPath $adapterPath -Raw -Encoding UTF8 | ConvertFrom-Json).instruction_target
    if ([string]::IsNullOrWhiteSpace($instructionTarget) -or -not (Test-Path -LiteralPath (Join-Path $target $instructionTarget))) {
        throw "Post-install validation failed: host instruction target '$instructionTarget' is missing."
    }

    Write-Success "Installed Anti-Gravity OS at $target"
    Write-Success "Configured portable URIs in $uriCount file(s)."
    if ($backupCreated) {
        Write-Success "Previous namespace retained at $backup"
    }
} catch {
    Write-Warn "Installation failed: $($_.Exception.Message)"
    if ($activated -and (Test-Path -LiteralPath $target)) {
        Assert-SafeTarget -Target $target -Source $installSource
        Remove-Item -LiteralPath $target -Recurse -Force
    }
    if ($backupCreated -and (Test-Path -LiteralPath $backup)) {
        Move-Item -LiteralPath $backup -Destination $target
        Write-Warn 'Previous installation was restored.'
    }
    if (Test-Path -LiteralPath $stage) {
        Remove-Item -LiteralPath $stage -Recurse -Force
    }
    throw
}
