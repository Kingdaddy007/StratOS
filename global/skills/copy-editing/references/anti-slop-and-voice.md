# Anti-Slop and Voice Review

## Use this reference

Load this reference only when the user asks to humanize existing text, remove
AI-sounding prose, preserve their personal voice, or detect generic writing
patterns without rewriting.

## Boundaries

- Preserve meaning, facts, uncertainty, vocabulary, humour, cadence, and useful
  imperfection unless the user explicitly authorizes a deeper rewrite.
- Diagnose observable writing patterns. Never claim that AI wrote the text,
  estimate an AI probability, or present a style score as measurement.
- Flag clusters and repeated habits, not one ordinary word, one dash, one list,
  clean grammar, or a short sample with too little evidence.
- Preserve quotations, code, titles, exact technical terms, citations, and
  source language verbatim unless they are expressly in editing scope.
- Never invent specificity, lived experience, opinions, sensory detail, slang,
  examples, or stronger certainty to make prose appear human.

## Select a mode

| Mode | Use when | Return |
| --- | --- | --- |
| Detect | The user asks what sounds generic or machine-like without requesting a rewrite. | Named patterns, quoted evidence, reader effect, and a small proposed fix. |
| Edit | The user supplies text to improve. | The minimum effective revision plus a concise account of material changes. |

## Inspect named patterns

Use only patterns that are visible in the supplied text:

| Pattern | Observable signal | Correction |
| --- | --- | --- |
| Generic throat-clearing | The opening delays the actual point with a reusable setup. | Start at the first specific claim, scene, fact, or decision. |
| Inflated importance | Labels such as pivotal, transformative, or vital substitute for consequence. | State what changed, for whom, and with what verified consequence. |
| Unsupported attribution | Anonymous experts, research, or consensus lend weight without a source. | Name and preserve the source, request it, or remove the claim. |
| False binary or dramatic reveal | Repeated “not X, but Y”, colon reveals, or staged rhetorical questions manufacture emphasis. | State the actual claim directly. |
| Formulaic enumeration | Repeated three-part lists or identical paragraph shapes make the prose interchangeable. | Use the natural number and structure required by the content. |
| Synonym cycling | One entity receives several labels merely to avoid repetition. | Repeat the clearest exact term. |
| Repetitive cadence | Consecutive sentences use nearly identical length and syntax. | Vary structure only where clarity and the author’s real cadence improve. |
| Formatting theatre | Decorative bold, headings, fragments, emoji, or excessive bullets carry emphasis that the prose has not earned. | Let structure follow the content and publication format. |
| Assistant residue | Help-offers, prompt restatements, reasoning scaffolds, or generic recaps leak into publishable prose. | Remove the conversational wrapper and keep the result. |
| Diff narration | Documentation explains what was added or changed instead of the current truth. | Describe the current system unless history is itself required. |
| Generic recap | The ending restates the piece or adds an empty optimistic conclusion. | End on the last concrete consequence, decision, or next action. |

## Edit safely

1. Read the full draft and identify the intended reader, job, and facts that
   cannot change.
2. Identify a few voice signals worth preserving. Keep that diagnosis internal
   unless the user asks for it.
3. Select only the repeated patterns that materially reduce clarity, trust, or
   distinctiveness.
4. Make the smallest revision that removes those patterns without flattening
   the writer.
5. Re-read for changed meaning, invented proof, erased uncertainty, and a new
   generic house voice.

## Output shape

For detection: `pattern -> quoted evidence -> reader effect -> proposed fix`.

For editing: provide the revised text, then list only material changes and any
fact or voice question that remains unresolved.
