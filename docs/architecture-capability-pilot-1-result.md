# Architecture Capability Pilot 1 — Result

**Date:** 2026-08-18  
**Candidate:** Quality-attribute scenario and trade-off analysis  
**Decision:** Advance to a Luna Max confirmation run; do not install as canonical policy yet.

## Plain-language result

We gave the same three tasks to three conditions:

- **A — Current:** the task with the architecture capability already installed in the user's Codex environment.
- **B — Kernel:** the same environment plus the compact proposed Anti-Gravity architecture kernel.
- **C — Candidate:** the kernel plus the quality-attribute scenario and trade-off instructions.

Condition C produced the strongest blinded result in every scenario. Its main benefit was not a different technology choice. It made the agent rank what mattered, define measurable success, expose trade-offs, and remain quiet when architecture was irrelevant.

This is encouraging evidence, not final proof. One independent run cannot satisfy the suite's repeatability gate.

## Blinded scores

| Scenario | A — Current | B — Kernel | C — Candidate | C over B |
|---|---:|---:|---:|---:|
| Greenfield appointment booking | 98.50 | 98.00 | **99.50** | +1.50 |
| Landing-page restyle control | 88.00 | 88.00 | **93.00** | +5.00 |
| Unjustified microservices request | 94.75 | 96.00 | **98.50** | +2.50 |
| **Equal-weight mean** | **93.75** | **94.00** | **97.00** | **+3.00** |

## What materially improved

1. The booking answer ranked integrity, offline utility, operability, tenant isolation, and recoverability with observable targets.
2. The visual-control answer stayed local and explicitly preserved content, behaviour, routes, data, dependencies, and component boundaries.
3. The microservices answer converted investor signalling into measurable capacity, recovery, ownership, and extraction evidence instead of obeying an arbitrary service count.
4. The candidate did not introduce a prohibited microservice, event-streaming, multi-region, or authoritative offline-write design.

## What did not improve much

- All three conditions already selected a managed PostgreSQL modular monolith for the booking product.
- Much of the difference was decision clarity and evidence quality, not a radically different topology.
- Some candidate-guided output was longer than necessary.

## Experimental limitation

The current global Codex installation automatically activated the existing architecture skill in all three conditions. Therefore, Condition A was not an uncustomised base model. This pilot measures whether the proposed kernel and candidate improve the current installed capability, which is the useful deployment question, but it does not measure the OS against a completely raw model.

The response-generating tasks used the user's configured default model because no model override had been specified when they were created. Future new test tasks must use **gpt-5.6-luna** at **max** effort, per the user's instruction.

## Decision gate

The candidate passes the first-run safety and usefulness checks:

- better target-task scores than the kernel
- no prohibited architecture overreach
- correct silence on an adjacent visual task
- a repeatable improvement mechanism: ranked scenarios tied to ownership, trade-offs, and verification

It does **not** yet pass the independent-run requirement. The next action is a Luna Max confirmation run. If the candidate again beats the kernel without extra ceremony, integrate it as a compact conditional capability under architecture—not as an always-on standalone process.
