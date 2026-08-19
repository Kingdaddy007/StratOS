# README - TEMPLATES FOLDER

**Location:** `global/global_templates/`
**Layer:** Support layer
**Loading Tier:** Tier 3 - on demand

---

## PURPOSE

This folder now serves **two distinct jobs**:

1. **Output scaffolds** for formal deliverables such as feature plans, review reports, and ADRs.
2. **Authoring templates** for creating or refreshing runtime context files.

Templates are not runtime truth. They are scaffolds used to create structured outputs or author runtime truth efficiently.

---

## TEMPLATE TYPES

### Output templates

Use these when Anti-Gravity needs to deliver a structured artifact:

- `architecture-decision-record.md`
- `debug-report.md`
- `code-review-report.md`
- `feature-plan.md`
- `prd-template.md`
- `risk-assessment.md`
- `project-brief.md`
- `decision-evidence-record.md`

### Context-authoring templates

Use these when creating or refreshing live files in `contexts/`:

- `project-context-template.md`
- `stack-context-template.md`
- `coding-standards-template.md`

Project inception and similar setup flows should load these templates, then write the resulting runtime truth into `contexts/`.

---

## LOADING RULES

Load templates only when the task needs one of these:

- a formal artifact shape
- a scaffold for creating or refreshing a runtime context file

Do not load templates as startup context. Templates are support material, not operating truth.

---

## INTERACTION WITH OTHER FOLDERS

| Folder | Relationship |
| :--- | :--- |
| `workflows/` | Workflows decide when templates are needed |
| `contexts/` | Context templates help author live context files, but they are not the runtime files themselves |
| `skills/` | Skills generate the reasoning that fills templates |
| `rubric/` | Rubrics may evaluate outputs that were shaped by templates |

---

## QUALITY BAR

A strong template:

- is easy to use under pressure
- makes important sections hard to forget
- stays shorter than the file it is helping create
- separates authoring guidance from runtime truth
- is specific enough to help, but not so bloated it becomes another manual

---

## FINAL RULE

`global_templates/` should make strong work easier to create without bloating the files Anti-Gravity reads during normal execution.
