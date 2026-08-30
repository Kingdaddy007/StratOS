# Architecture Map

## Build-time relationship

```mermaid
flowchart LR
  source["global/ canonical source"] --> manifest["manifest.yaml registry"]
  source --> compiler["os.py validate/build"]
  manifest --> compiler
  compiler --> dist["dist/<host>/ generated payload"]
  dist --> adapters["Antigravity / Gemini / Codex / Cursor / Windsurf / OpenCode / Zed"]
  adapters --> host["host instruction + skills + workflows"]
```

## Runtime task relationship

```mermaid
flowchart TD
  request["User request"] --> authority["Authority and trust rules"]
  authority --> router["GLOBAL_MEMORY.md router"]
  router --> mode["diagnose / propose / implement / incident-mitigate"]
  mode --> workflow["Selected workflow"]
  workflow --> skill["Selected skill"]
  skill --> refs["Conditional references"]
  workflow --> context[".agents/contexts active project truth"]
  workflow --> state[".agents/workflows/<task-id>.json"]
  workflow --> evidence["Verification + approval record"]
```

`global/` is edited source. `dist/` is generated output. `.agents/contexts/` and `.agents/workflows/` are runtime project state. `USER_PROFILE.md` stores preferences only; it never overrides authority or grants permission.
