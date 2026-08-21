# Canonical Agent Contracts

## Purpose

This directory defines reusable V4 agent roles. Each `AGENT.md` is a portable
behaviour and authority contract. It is not itself a host installation file.

## Boundaries

- Canonical agents define purpose, activation, exclusions, authority ceiling,
  delegation limits, default skill IDs, and optional profile-specific skill IDs.
- Every agent declares a machine-checked `return_contract` and
  `delegation_contract`. The return contract is the minimum evidence-bearing
  handoff; the delegation contract prevents worker scope, authority, or
  recursion from expanding silently.
- A role's baseline `skills` are always relevant methods. `conditional_skills`
  add methods only when the matching optional profile is installed. They do not
  make a role an owner of every skill or load every installed skill.
- Every role uses the installed `GLOBAL_MEMORY.md` routing index to select the
  smallest relevant skill, reference, and workflow. A tool list is a capability
  ceiling, not permission or a reason to use a tool.
- The Studio Director owns the parent route. A specialist follows an assigned
  route inside its charter or reports that another route is needed; it does not
  silently replace the parent workflow.
- An assigned workflow or acceptance gate narrows a specialist charter. The
  specialist returns candidate evidence and limitations; the accountable parent
  resolves integration and final gate status. Host adapters must preserve this
  boundary in generated agent instructions.
- They must not contain host tool names, user-private facts, credentials, live
  project assumptions, or authority that exceeds the root policy.
- A host adapter renders its own agent format from this source. Generated agent
  files belong only in `dist/<host>/`.
- A reusable agent definition does not authorize an always-running agent or a
  permanent worker swarm.
- A specialist handoff must name the task and scope, inputs and provenance,
  authority ceiling, findings, confidence, conflicts, recommendation,
  stop/escalate condition, residual risk, and owner. A missing field is an
  incomplete handoff, not a successful result.

## Verification

- Run `python global/scripts/os.py validate`.
- Build the `antigravity` General payload and confirm every registered agent is
  generated under `.agents/agents/<id>/agent.md`.
