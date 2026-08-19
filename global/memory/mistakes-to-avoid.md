# MEMORY: MISTAKES TO AVOID

**Version:** Gold v1.0
**Layer:** 12 — Institutional Learning
**Tier:** 3 — Loaded on demand
**File:** memory/mistakes-to-avoid.md
**Purpose:** Records mistakes that have been made, their root causes, and how to avoid repeating them. This is the organizational scar tissue — hard-won lessons that prevent repeat failures.
**Loaded When:** Working in an area where past mistakes occurred. Building something similar to a past failure. Reviewing an area that has a known trap. Onboarding to understand project history.
**Format:** Append-only. Never delete entries — past mistakes remain relevant even after fixes are in place.

---

## WHEN TO ADD AN ENTRY

Add an entry when:

- A bug reaches production that should have been caught earlier
- A technical decision turns out to be wrong and the cost was real
- The same type of mistake happens twice — a pattern has been detected
- An incident reveals a systemic or structural weakness
- A code review catches something that almost shipped
- You think — "I do not want to make this mistake again"

Do NOT log:

- Every small bug — only log bugs with lessons worth remembering
- Mistakes that are obvious and unlikely to recur in any form
- Mistakes already documented in `postmortems.md` — reference the postmortem instead
- Blame or emotional venting — this file is for pattern recognition and prevention, not attribution
- Tiny mistakes with no real recurrence risk or structural lesson

---

## HOW TO USE THIS FILE

Anti-Gravity should consult this file when:

- Working in an area where past mistakes are known to have occurred
- Building something similar to a previous failure
- Reviewing or auditing an area with known traps
- A recurring mistake or regression suggests a pattern exists

If a mistake happens more than once, it is no longer just an accident. It is a pattern, and it belongs in this file.

If the project has already paid for a mistake once, Anti-Gravity should try hard not to make it pay again.

---

## ENTRY FORMAT

[YYYY-MM-DD] — [Mistake Title]

Category
[Coding / Architecture / Testing / Security / API / Infra / Release / Product / Process / Domain]

What Happened
[Factual description of what went wrong — not blame, just facts]

Impact
[Who was affected? How severely? How long did it last?]

Root Cause
[Why did this happen? Not "someone made an error" — what structural issue allowed this mistake to occur and not be caught?]

Warning Signs
[What signals usually appear before this mistake happens again?]

- [signal 1]
- [signal 2]
- [signal 3]

How It Was Fixed
[What was done to resolve the immediate issue?]

How to Prevent Recurrence
[What check, test, process, or pattern prevents this class of mistake?]

- [prevention 1]
- [prevention 2]
- [prevention 3]

The Lesson
[One sentence: what to remember next time you are in a similar situation]

Related Files / Areas

- [postmortem / benchmark / context / workflow / ADR / code area]
- [related item 2]

Tags: #auth #database #deployment #testing #scope-creep #performance

---

## CATEGORY INDEX

> **For Anti-Gravity:** Before starting any task, scan the relevant category below.
> Only read the full entries if a category title matches your current work area.

### Build / Compile Failures

<!-- Entries tagged: #build #compile #dependency #import -->

- [Jump to entries tagged #build]

### Data Integrity

<!-- Entries tagged: #data-integrity #timestamp #candles #database #migration -->

- (none yet)

### UI / Frontend Bugs

<!-- Entries tagged: #lwc #crash #split-view #rendering #css -->

- (none yet)

### Architecture / Design Decisions

<!-- Entries tagged: #architecture #refactor #structure #module -->

- (none yet)

### Security / Auth

<!-- Entries tagged: #auth #security #authorization #data-leakage -->

- (none yet — see Example Entry for reference pattern)

### API / Integration

<!-- Entries tagged: #api #websocket #integration -->

- (none yet)

### Testing / Verification

<!-- Entries tagged: #testing #regression #edge-case -->

- (none yet)

### Tooling / Process

<!-- Entries tagged: #tooling #python #process #npm #config -->

- (none yet)

### Performance

<!-- Entries tagged: #performance #memory #cpu #bottleneck -->

- (none yet)

> **Rule:** When adding a new entry below, also add a one-line summary to the relevant category above.
> This index should always be scannable in under 10 seconds.

---

## QUALITY BAR FOR ENTRIES

A strong entry:

- Describes a recurring or important failure mode with real cost
- Identifies the structural root cause — not just the surface event
- Gives concrete prevention rules that can be applied proactively
- Includes warning signs so the mistake can be caught before it recurs
- Is specific enough to guide future reviews and recommendations

A weak entry:

- Is too vague or emotional to guide future behavior
- Records something trivial with no future relevance
- Lacks a prevention principle — only describes what went wrong
- Attributes blame without identifying structural cause
- Records something already obvious and unlikely to recur

---

## USAGE RULES

1. Record recurring mistakes and mistakes with real cost — not one-off trivial errors.
2. Focus on mistakes that produced:
   - Real bugs or production incidents
   - Repeated confusion or regressions
   - Security risk or data integrity issues
   - Structural weakness that persisted over time
3. Keep corrective guidance concrete and actionable.
4. Do not delete history silently — if a mistake is no longer relevant, mark it as historical rather than removing it.
5. Use this file to improve future recommendations, reviews, and workflow discipline.
6. Most recent entries appear at the top.

---

## EXAMPLE ENTRY

2024-05-22 — Read Queries Missing Project Membership Check

Category
Security / Authorization

What Happened
A user who was removed from a project could still view that project's tasks on the sprint board. Write operations correctly returned 403, but read operations only checked if the project existed — not whether the user was still a member.

Impact
Data leakage across authorization boundaries. Unknown number of removed users may have viewed project data after removal. Duration approximately three months since the feature was originally built.

Root Cause
The authorization check pattern was applied inconsistently. Write operations all checked project membership. Read operations only checked that the project existed. There was no centralized membership check helper — each developer implemented their own check, and reads were not treated as requiring the same authorization rigor as writes.

Warning Signs

- Authorization is only applied in Server Actions but not in query functions or data fetching paths
- A new read endpoint is added without a corresponding membership or permission check
- "Works for me" testing only tests the happy path as a valid member

How It Was Fixed

- Created a centralized membership verification helper used by ALL data access paths — read and write
- Added the check to all read query functions
- Wrote integration tests for every read path verifying non-member access returns 403
- Added to the security review checklist: "verify read AND write authorization"

How to Prevent Recurrence

- The centralized membership helper is now mandatory for all data access
- Code review checklist explicitly includes authorization check verification for read paths
- Integration tests cover non-member access for every endpoint

The Lesson
Authorization checks must be applied to reads, not just writes. If a user cannot modify data, they should not be able to see it either.

Related Files / Areas

- memory/postmortems.md
- contexts/security-baselines.md
- skill-security.md

Tags: #auth #security #authorization #data-leakage

---

## ENTRIES

<!-- Append new entries below this line. Most recent at the top. -->
<!-- Append new entries below this line. Most recent at the top. -->
