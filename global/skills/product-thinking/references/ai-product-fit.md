# AI Product Fit

Use this reference when deciding whether an AI capability improves a product or service, and whether it should assist a person or act with bounded autonomy.

## Decision sequence

1. **Start with the task and outcome.** Describe the current workflow, user progress, alternative, and failure cost without naming an AI architecture.
2. **Compare the baseline.** Consider no change, a deterministic rule, an existing tool, a process change, or a human-supported service. Prefer the simpler option when it meets the need more reliably or transparently.
3. **Test unique value.** AI may fit variable-language interpretation, personalisation, prediction, recognition across changing cases, or genuinely dynamic assistance. It may not fit fixed, predictable, highly auditable, or error-intolerant work.
4. **Choose automation or augmentation.** Automation may fit repetitive, unwanted, bounded tasks. Augmentation may fit high-stakes, creative, personally meaningful, socially accountable, or preference-rich tasks where the person should remain in control.
5. **Specify the safety envelope.** State error types and cost, data boundaries, representative evaluation cases, confidence/uncertainty handling, user correction or override, escalation, fallback, and monitoring/review.

## Proportional record

```markdown
Task and outcome: [what must improve]
Baseline considered: [rule/tool/process/human/no change]
Why AI adds unique value: [or why it does not]
Automation or augmentation: [and control retained by the user]
Error and data boundary: [failure cost, sensitive data, prohibited actions]
Evaluation and fallback: [representative cases, correction, safe alternative]
```

For high-consequence decisions, use the appropriate Security, Architecture, Testing, legal/domain, and release controls. This reference does not grant permission to collect data, act externally, or deploy.
