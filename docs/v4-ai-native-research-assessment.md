# V4 AI-Native Product Architecture Research Assessment

**Status:** research synthesis, not active policy and not a skill rewrite  
**Date:** 2026-08-18  
**Decision:** the research is sufficient to define a capability map. It is not sufficient to blindly copy any report into Anti-Gravity.

## What question this answers

This study is about products that expose AI to their users: for example, a product feature that generates, retrieves, reasons, classifies, uses a tool, or acts in the world. It is **not** about using Codex, Gemini, or another model to help Beloved build ordinary software.

The design target is simple:

```text
ordinary product architecture
            |
            +-- only when the product itself uses AI --> a thin AI-native control layer
```

The second branch is conditional. A normal booking app, portfolio, dashboard, or API does not become an "AI system" merely because an AI assistant helped build it.

## How the reports were assessed

The reports were compared on five questions:

1. Does it answer the actual product-architecture question instead of recommending a fashionable stack?
2. Does it distinguish an AI feature, a controlled workflow, a tool-using agent, and autonomous action?
3. Are important claims traceable to primary, official, or peer-reviewed sources?
4. Does it preserve reversibility and avoid forcing RAG, agents, memory, or a particular vendor?
5. Can its recommendations be translated into proportionate controls rather than bureaucracy?

## Report verdict

| Report | Role in the synthesis | What it did well | Limitation | Decision |
| --- | --- | --- | --- | --- |
| **Manus - Architecture for AI-Native Digital Products** | Primary evidence base | Clear scope; precise boundary between AI and ordinary product systems; strong source ledger; small controls tied to triggers and failure modes | Intentionally compact; does not fully explore implementation alternatives | **Use as the primary foundation** |
| **Grok - rigorous source-backed study** | Technical counterweight | Excellent explanation of operating modes, containment, external enforcement, testable controls, fallbacks, and evaluation | Its source list mixes official material with blog and vendor sources; several striking numerical claims need independent checking before adoption | **Use for structure and challenge, not unverified statistics** |
| **Gemini - AI-Native Product Architecture Study** | Pattern and idea bank | Good taxonomy, helpful examples of optional patterns, useful distinction between general and AI-specific architecture | Many citations are explainers or vendor blogs rather than the underlying primary sources; several designs are presented too universally | **Retain as optional ideas only** |
| **ChatGPT - deep-research report** | Cross-check only | Covers the expected headings | Does not provide a usable claim-to-source trail; too generic to decide policy from | **Do not use as a decision source** |

## The durable conclusions

These are supported by the stronger reports and corroborated by primary guidance.

1. **Start with an AI suitability decision.** Use AI where ambiguity, generation, language/media transformation, or judgement is the job. Prefer conventional software, search, rules, or human service where the answer must be deterministic.
2. **Keep product authority outside the model.** Authentication, authorization, policy enforcement, durable state, audit records, budgets, and actual external effects remain in ordinary product code or trusted services. A model may propose; the product decides whether to execute.
3. **Treat autonomy as a graduated decision.** Begin with an AI feature or a coded workflow. Tool-using loops and open-ended autonomy require a clear benefit, bounded permissions, stop conditions, evidence, and a proportional approval path.
4. **Make AI behaviour changeable and inspectable.** Model selection, prompts/instructions, retrieval configuration, tools, and relevant thresholds are product behaviour. They need owners, versioning appropriate to their impact, and regression checks before a material change ships.
5. **Do not add retrieval, memory, or tools by default.** Each increases the attack surface, operating cost, privacy burden, and failure modes. Add one only when the product job needs it.
6. **Separate deterministic proof from human judgement.** Authorization, tenant filtering, schemas, idempotency, budget caps, and whether a side effect happened can be checked mechanically. Usefulness, tone, user trust, and nuanced harm require representative human review as well.
7. **Design a non-AI path or a clear degraded state.** Provider outage, timeout, cost cap, failed evaluation, or unsafe output should not silently turn into a false answer or uncontrolled action.

These conclusions align with the [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf), [OWASP LLM06: Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), and the [NCSC/CISA secure AI development guidance](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development).

## What does **not** become policy from this research

- No universal "agent stack."
- No mandatory RAG, vector database, long-term memory, multi-agent design, fine-tuning, or provider abstraction.
- No fixed vendor, framework, database, protocol, token budget, test count, confidence threshold, or architecture pattern.
- No claim that model output is safe because another model checked it.
- No adoption of report statistics until the exact source and scope are independently verified.
- No separate identity, logging, security, or approval system for AI. The AI-specific layer must extend the ordinary product controls that already own those concerns.

## Confidence and next decision

**Confidence:** high for the capability boundaries; medium for implementation recipes; intentionally low for the reports' unverified numerical claims.

The next decision is not "rewrite every skill." It is to map these capabilities to what Anti-Gravity already has, then decide for each gap whether it is:

- ordinary engineering judgement;
- a short reusable reference;
- a workflow or approval gate; or
- a future AI-native skill that earns its existence through a concrete recurring need.

That mapping is recorded in [V4 Architecture Evidence Map](v4-architecture-evidence-map.md) and [V4 Architecture Asset Map](v4-architecture-asset-map.md).
