#!/usr/bin/env bash
# Anti-Gravity OS - safe macOS/Linux installer

set -Eeuo pipefail

GLOBAL_CONFIG=""
IDE=""
HOST_ID=""
INSTALL_OPTION=""
DRY_RUN=false
ASSUME_YES=false
TARGET=""
BACKUP=""
STAGE=""
BACKUP_CREATED=false
ACTIVATED=false

step() { printf '\n> %s\n' "$1"; }
success() { printf '  OK  %s\n' "$1"; }
warn() { printf '  WARN  %s\n' "$1" >&2; }

usage() {
    cat <<'EOF'
Usage: ./install.sh [--ide 1-6] [--host HOST] [--global-config PARENT] [--option general|full] [--dry-run] [--yes]

The installer always writes to a dedicated directory named "antigravity".
--global-config is a parent directory unless it already ends in /antigravity.
If --option is omitted, the installer asks whether to install General or Full.
EOF
}

while (($#)); do
    case "$1" in
        --global-config)
            [[ $# -ge 2 ]] || { warn '--global-config needs a value'; exit 2; }
            GLOBAL_CONFIG="$2"; shift 2 ;;
        --ide)
            [[ $# -ge 2 ]] || { warn '--ide needs a value'; exit 2; }
            IDE="$2"; shift 2 ;;
        --host)
            [[ $# -ge 2 ]] || { warn '--host needs a value'; exit 2; }
            HOST_ID="$2"; shift 2 ;;
        --option)
            [[ $# -ge 2 ]] || { warn '--option needs a value'; exit 2; }
            INSTALL_OPTION="$2"; shift 2 ;;
        --dry-run) DRY_RUN=true; shift ;;
        --yes) ASSUME_YES=true; shift ;;
        --help|-h) usage; exit 0 ;;
        *) warn "Unknown option: $1"; usage; exit 2 ;;
    esac
done

SCRIPT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
GLOBAL_SOURCE="$SCRIPT_ROOT/global"
[[ -f "$GLOBAL_SOURCE/GEMINI.md" ]] || { warn "Incomplete source: $GLOBAL_SOURCE"; exit 1; }

expand_path() {
    local path="$1"
    [[ -n "$path" ]] || { warn 'Install path cannot be empty'; return 1; }
    path="${path/#\~/$HOME}"
    [[ "$path" = /* ]] || path="$PWD/$path"
    [[ "$path" != *'/../'* && "$path" != */.. && "$path" != ../* ]] || {
        warn "Refusing path containing parent traversal: $path"; return 1;
    }
    printf '%s\n' "${path%/}"
}

add_namespace() {
    local base
    base="$(expand_path "$1")"
    if [[ "${base##*/}" == 'antigravity' ]]; then
        printf '%s\n' "$base"
    else
        printf '%s/antigravity\n' "$base"
    fi
}

select_target() {
    if [[ -n "$GLOBAL_CONFIG" ]]; then
        [[ -n "$HOST_ID" ]] || { warn 'Custom/global config targets require --host gemini|codex|cursor|windsurf|opencode.'; return 1; }
        SELECTED_TARGET="$(add_namespace "$GLOBAL_CONFIG")"
        return
    fi

    if [[ -z "$IDE" ]]; then
        cat <<'EOF'
Choose a host:
  [1] Gemini     -> ~/.gemini/antigravity
  [2] Codex      -> ~/.codex/antigravity
  [3] Cursor     -> ~/.cursor/rules/antigravity
  [4] Windsurf   -> ~/.codeium/windsurf/memories/antigravity
  [5] OpenCode   -> ~/.config/opencode/antigravity
  [6] Custom parent directory
EOF
        read -r -p 'Enter 1-6: ' IDE
    fi

    case "$IDE" in
        1) HOST_ID='gemini'; SELECTED_TARGET="$HOME/.gemini/antigravity" ;;
        2) HOST_ID='codex'; SELECTED_TARGET="$HOME/.codex/antigravity" ;;
        3) HOST_ID='cursor'; SELECTED_TARGET="$HOME/.cursor/rules/antigravity" ;;
        4) HOST_ID='windsurf'; SELECTED_TARGET="$HOME/.codeium/windsurf/memories/antigravity" ;;
        5) HOST_ID='opencode'; SELECTED_TARGET="$HOME/.config/opencode/antigravity" ;;
        6)
            local custom_parent
            if [[ -z "$HOST_ID" ]]; then
                read -r -p 'Supported host (gemini, codex, cursor, windsurf, opencode): ' HOST_ID
            fi
            read -r -p 'Parent directory for the antigravity namespace: ' custom_parent
            SELECTED_TARGET="$(add_namespace "$custom_parent")" ;;
        *) warn "Unknown host choice '$IDE'. Use 1-6."; return 1 ;;
    esac
}

assert_supported_host() {
    case "$HOST_ID" in gemini|codex|cursor|windsurf|opencode) return 0 ;; esac
    warn "Unsupported host '$HOST_ID'. Use gemini, codex, cursor, windsurf, or opencode."
    return 1
}

find_python() {
    if command -v python3 >/dev/null 2>&1; then PYTHON=(python3); return 0; fi
    if command -v python >/dev/null 2>&1; then PYTHON=(python); return 0; fi
    return 1
}

resolve_host_payload() {
    local profile_key='general'
    if [[ "$INSTALL_OPTION" == 'full' ]]; then profile_key='general+spatial+media+growth'; fi
    INSTALL_SOURCE="$SCRIPT_ROOT/dist/$HOST_ID/$profile_key"
    if [[ ! -f "$INSTALL_SOURCE/adapter.json" && -f "$SCRIPT_ROOT/dist/$HOST_ID/adapter.json" ]]; then
        INSTALL_SOURCE="$SCRIPT_ROOT/dist/$HOST_ID"
    fi
    PENDING_BUILD=false
    if [[ -f "$INSTALL_SOURCE/adapter.json" ]]; then return 0; fi
    if ! find_python; then
        warn "No prebuilt dist/$HOST_ID payload and no Python 3 runtime were found. Use a release package containing dist/$HOST_ID or install Python 3 and rerun."
        return 1
    fi
    if [[ "$DRY_RUN" == true ]]; then PENDING_BUILD=true; return 0; fi
    local build_args=("$SCRIPT_ROOT/global/scripts/os.py" build --host "$HOST_ID" --profile general)
    if [[ "$INSTALL_OPTION" == 'full' ]]; then build_args+=(--packs spatial,media,growth); fi
    "${PYTHON[@]}" "${build_args[@]}"
    [[ -f "$INSTALL_SOURCE/adapter.json" ]] || {
        warn "Failed to build the $HOST_ID payload. Run validation or use a release package containing dist/$HOST_ID."
        return 1
    }
}

select_install_option() {
    if [[ -n "$INSTALL_OPTION" ]]; then
        case "$INSTALL_OPTION" in general|full) return 0 ;; esac
        warn "Unsupported installation option '$INSTALL_OPTION'. Use general or full."
        return 1
    fi

    local counts=''
    local general_description='installs the core General-profile skills'
    local full_description='installs all registered skills'
    if command -v python3 >/dev/null 2>&1; then
        counts="$(python3 -c 'import json,sys; m=json.load(open(sys.argv[1], encoding="utf-8")); s=m.get("skills", []); print(len(m.get("agents", [])), len(m.get("workflows", [])), sum("general" in x.get("profiles", []) for x in s), len(s))' "$SCRIPT_ROOT/global/manifest.yaml" 2>/dev/null || true)"
    fi
    if [[ -n "$counts" ]]; then
        read -r agent_count workflow_count general_skill_count all_skill_count <<< "$counts"
        general_description="installs $agent_count custom agents, $workflow_count workflows, and $general_skill_count General-profile skills"
        full_description="installs $agent_count custom agents, $workflow_count workflows, and all $all_skill_count registered skills"
    fi

    cat <<EOF

Your Installation Options:
  [1] General Profile - $general_description. Spatial, Media, and Growth remain dormant.
  [2] Full System - $full_description, including Spatial, Media, and Growth.
EOF
    read -r -p 'Choose 1 or 2 [1]: ' choice
    choice="${choice:-1}"
    case "$choice" in
        1) INSTALL_OPTION='general' ;;
        2) INSTALL_OPTION='full' ;;
        *) warn 'Choose 1 for General or 2 for Full System.'; return 1 ;;
    esac
}

assert_safe_target() {
    local target="$1"
    [[ "${target##*/}" == 'antigravity' ]] || { warn "Refusing non-namespaced target: $target"; return 1; }
    [[ "$target" != '/' && "$target" != "$HOME" ]] || { warn "Refusing dangerous target: $target"; return 1; }
    [[ "${target%/*}" != '' ]] || { warn "Refusing to install directly below the filesystem root: $target"; return 1; }
    [[ "$INSTALL_SOURCE" != "$target" && "$INSTALL_SOURCE" != "$target/"* && "$target" != "$INSTALL_SOURCE/"* ]] || {
        warn 'Source and target must not contain one another.'; return 1;
    }
    [[ ! -L "$target" ]] || { warn "Refusing symlink target: $target"; return 1; }
}

copy_contents() {
    local source="$1" destination="$2"
    cp -a "$source/." "$destination/"
}

configure_uris() {
    local directory="$1" target_uri="file://$1" count=0 file
    while IFS= read -r -d '' file; do
        if grep -q '{{GLOBAL_CONFIG_URI}}' "$file"; then
            if command -v perl >/dev/null 2>&1; then
                TARGET_URI="$target_uri" perl -0pi -e 's|\{\{GLOBAL_CONFIG_URI\}\}|$ENV{TARGET_URI}|g' "$file"
            else
                warn 'Perl is required to replace portable URI placeholders safely.'
                return 1
            fi
            count=$((count + 1))
        fi
    done < <(find "$directory" -type f -name '*.md' -print0)
    printf '%s\n' "$count"
}

rollback() {
    local exit_code=$?
    trap - ERR INT TERM
    warn 'Installation failed; starting rollback.'
    if [[ "$ACTIVATED" == true && -d "$TARGET" ]]; then
        assert_safe_target "$TARGET"
        rm -rf -- "$TARGET"
    fi
    if [[ "$BACKUP_CREATED" == true && -d "$BACKUP" ]]; then
        mv -- "$BACKUP" "$TARGET"
        warn 'Previous installation was restored.'
    fi
    if [[ -n "$STAGE" && -d "$STAGE" ]]; then
        rm -rf -- "$STAGE"
    fi
    exit "$exit_code"
}

SELECTED_TARGET=""
select_target
assert_supported_host
select_install_option
TARGET="$(expand_path "$SELECTED_TARGET")"
resolve_host_payload
assert_safe_target "$TARGET"
PARENT="${TARGET%/*}"
TIMESTAMP="$(date -u +%Y%m%d-%H%M%S)"
BACKUP_ROOT="$PARENT/.antigravity-backups"
BACKUP="$BACKUP_ROOT/$TIMESTAMP-$$"
STAGE="$PARENT/.antigravity-stage-$$-$RANDOM"
if [[ -d "$INSTALL_SOURCE" ]]; then SOURCE_FILE_COUNT="$(find "$INSTALL_SOURCE" -type f | wc -l | tr -d ' ')"; else SOURCE_FILE_COUNT=0; fi

step 'Installation plan'
printf '  Host: %s\n  Payload: %s\n  Target: %s\n  Managed payload files: %s\n' "$HOST_ID" "$INSTALL_SOURCE" "$TARGET" "$SOURCE_FILE_COUNT"
if [[ "$PENDING_BUILD" == true ]]; then printf '  Payload action: build with global/scripts/os.py after approval\n'; fi
if [[ -d "$TARGET" ]]; then
    printf '  Existing namespace backup: %s\n' "$BACKUP"
    printf '  Existing extra files are retained in the staged replacement.\n'
else
    printf '  Existing namespace: none\n'
fi
printf '  Shared parent directories are never cleared.\n'

if [[ "$DRY_RUN" == true ]]; then
    success 'Dry run complete. No files were written.'
    exit 0
fi

if [[ "$ASSUME_YES" != true ]]; then
    read -r -p "Install only into '$TARGET'? Type INSTALL to continue: " CONFIRMATION
    [[ "$CONFIRMATION" == 'INSTALL' ]] || { warn 'Installation cancelled. No files were changed.'; exit 0; }
fi

trap rollback ERR INT TERM
mkdir -p -- "$PARENT"
mkdir -- "$STAGE"
if [[ "$PENDING_BUILD" == true ]]; then
    DRY_RUN=false
    resolve_host_payload
fi
if [[ -d "$TARGET" ]]; then copy_contents "$TARGET" "$STAGE"; fi
copy_contents "$INSTALL_SOURCE" "$STAGE"
URI_COUNT="$(configure_uris "$STAGE")"

if [[ -d "$TARGET" ]]; then
    mkdir -p -- "$BACKUP_ROOT"
    mv -- "$TARGET" "$BACKUP"
    BACKUP_CREATED=true
fi
mv -- "$STAGE" "$TARGET"
ACTIVATED=true
[[ -f "$TARGET/adapter.json" ]]
INSTRUCTION_TARGET="$(sed -n 's/^[[:space:]]*"instruction_target"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' "$TARGET/adapter.json" | head -n 1)"
[[ -n "$INSTRUCTION_TARGET" && -f "$TARGET/$INSTRUCTION_TARGET" ]]
trap - ERR INT TERM

success "Installed Anti-Gravity OS at $TARGET"
success "Configured portable URIs in $URI_COUNT file(s)."
if [[ "$BACKUP_CREATED" == true ]]; then success "Previous namespace retained at $BACKUP"; fi
