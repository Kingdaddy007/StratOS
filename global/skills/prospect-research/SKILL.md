---
name: prospect-research
description: 'Use this skill when finding, scoring, or profiling prospects for the Cinematic Digital Showroom offer targeting luxury residential interior designers and boutique interior design studios. Activated by "find prospects", "research interior designers", "find Lagos prospects", "find Dubai prospects", "who should I target this week", "score this designer", "prospect research", "find designers with weak websites", or any task that involves identifying, qualifying, or prioritizing outreach targets for the BEVAMPED studio offer. Do NOT use for general web research, competitor profiling, or sales outreach copy (use sales-enablement or copywriting skills for those).'
---

# Prospect Research

## WHEN TO USE THIS

- Finding new outreach targets for the Cinematic Digital Showroom offer.
- Scoring and ranking a list of interior designers by ICP fit.
- Auditing a specific designer's Instagram and website to decide on action.

## AUTHORITY AND EXTERNAL-ACTION BOUNDARY

This skill researches and scores prospects, then prepares a dossier or a proposed next action. It does not contact a prospect, send a message, publish a concept, update a CRM, upload data, or make a purchase. Any external action remains subject to the host's just-in-time approval gate.

## REFERENCE LOADING RULES

- Load `references/prospect-dossier-template.md` whenever creating, reviewing, or handing off a prospect dossier.
- Load `scripts/dossier_helper.py` only when the user requests a machine-readable dossier, batch scoring, validation, or a repeatable export. The script is a local helper; it does not browse, contact, or upload anything.
- Do not load either resource for general market research that is not qualifying an outreach prospect.

## NEVER DO

- Target budget decorators, home staging businesses, or Airbnb/short-let stylists.
- Target designers who already have excellent cinematic/conversion-focused websites.
- Target large corporate firms with heavy procurement or gatekeepers.
- Target firms with 20+ staff, dedicated marketing departments, or corporate bidding structures.
- Accept prospects without real completed project photography.
- Score a prospect without checking both their Instagram AND website.
- Produce a concept for a Growth Tier (50–79) prospect without prior interest shown.

---

## PRIMARY ICP

**Luxury residential interior designers and boutique interior design studios** with:
- Strong completed project photography
- Premium or luxury positioning language
- Active Instagram or social presence
- Weak, static, outdated, broken, or nonexistent website
- Founder-led or principal-led access

**Geographic priority:** Nigeria (Lagos, Abuja, Port Harcourt) first → Dubai/UAE second → London, Johannesburg, Miami, NYC, LA last.

**Nigeria signals:** Outdated WordPress/Wix, no website, Instagram-only, broken widgets, casino/spam footer links, no inquiry funnel.
**Dubai signals:** Static portfolio site, no scroll motion, no case-study depth, no HNWI intake funnel, strong visuals but weak conversion.

---

## DISQUALIFY IF

| Signal | Reason |
| --- | --- |
| Mostly reposted Pinterest/inspiration content | No real client proof |
| Budget, affordable, DIY decor language | Wrong price tier |
| No completed project evidence | Cannot build a concept |
| Already excellent modern cinematic website | No gap to close |
| Large commercial firm with multiple gatekeepers | Slow cycle, wrong ICP |
| Team size is 20+ employees or has dedicated PR/Marketing teams | High gatekeeper risk, unreachable founder |
| Inactive social + no contact method | Unreachable |

---

## SEARCH SOURCES

Instagram · Google Search · Google Maps · Houzz · LinkedIn · Pinterest · `/last30days` (for recent X, Reddit, YouTube, and community signals) · luxury lifestyle award directories · interior design association directories · real estate/luxury home publications.

**Instagram inspection:** bio, highlights, recent posts, project captions, follower quality, engagement quality, tagged locations, website link.
**Website inspection:** homepage, portfolio, services, about, contact, mobile layout, CTAs, inquiry path, case studies, testimonials, technical issues.
**Recent activity inspection (/last30days):** Run `/last30days <founder name>` or `/last30days <studio name>` to pull recent X threads, Reddit mentions, YouTube interviews, or news from the last 30 days to extract high-relevance personalization hooks.

---

## SEARCH QUERIES

**Nigeria:** `luxury interior designer Lagos` · `turnkey interior design Lagos` · `bespoke interior designer Abuja` · `villa interior designer Port Harcourt` · `site:instagram.com luxury interior designer Lagos`

**Dubai:** `luxury interior designer Dubai` · `villa interior designer Palm Jumeirah` · `boutique interior design studio Dubai` · `site:instagram.com villa interior designer Dubai`

---

## SCORING SYSTEM (100 points)

| Category | Points | Top Score Criteria |
| --- | --- | --- |
| Visual Asset Quality | /25 | Exceptional editorial photography, luxury completed projects |
| Website Gap | /20 | No site, broken site, hacked, severe template gap |
| Business Maturity | /10 | Established premium boutique, clear high-value residential history |
| Active Online Presence | /15 | Active, professional, recent project content |
| Contact Accessibility | /20 | Direct founder email/WhatsApp, active founder presence, direct DM access |
| Personalization Potential | /10 | Obvious gap + strong imagery + clear concept angle |

**Elite Tier (80–100):** Prepare a proposed concept and high-personalisation outreach draft for human review. Do not send, publish, or record anything externally without approval.
**Growth Tier (50–79):** Prepare a light personalised draft for human review; consider a concept only after evidence of interest. Do not send it without approval.
**Low Tier (below 50):** Do not target.

---

## POSITIVE SIGNALS

Premium language cues: `bespoke` · `curated` · `refined` · `turnkey` · `villa` · `penthouse` · `private residence` · `full-service design` · `custom joinery` · `quiet luxury`

Founder Visibility: Founder's face, name, or voice is prominent on Instagram reels/stories (highly accessible and brand-conscious).

Strong personalization hooks: broken website element · no site despite strong Instagram · luxury project buried in a static gallery · founder story that can become a hero concept · diaspora/HNWI client angle.

---

## ANTI-PATTERNS

| Anti-Pattern | What It Is | Fix |
| --- | --- | --- |
| Galaxy-brain ICP stretch | Targeting hospitality or commercial firms first because they "feel premium" | Lock to luxury residential and boutique studios as primary ICPs |
| Generic gap messaging | Saying "your website looks outdated" without naming a specific failure | Name one concrete gap: broken counter, no case studies, Instagram-vs-website mismatch |
| Concept before contact | Building a full hero concept for a Growth Tier prospect with no prior response | Prepare a light outreach draft for human review; consider a concept only after evidence of interest |
| Budget exception | Accepting a prospect that shows budget language because their visuals are good | Disqualify. Ability to pay matters as much as visual quality |

---

## OUTPUT SHAPE

**Prospect scan (5+ designers):**
Search Scope → Executive Summary (totals by tier) → Structured Prospect Profiles → Market Observations → Recommended Next Actions

**Single prospect audit:**
Scores by category → Total ICP score + tier → Main website gap → Suggested hero concept angle → Suggested outreach hook → Proposed next action for human approval

**Prospect profile fields (required):**
Studio name · Country · City · Segment · Website URL · Instagram URL · Founder name · Contact method · Website status · All 6 category scores · Total score · Main gap · Hero concept angle · Outreach hook · Proposed next action

For repeatable work, store one JSON dossier per prospect using the template and run `python scripts/dossier_helper.py validate <dossier.json>` before delivery. Use `score` only after both Instagram and website evidence has been recorded.

---

## NON-NEGOTIABLE CHECKLIST

1. Both Instagram AND website inspected before scoring.
2. Visual Asset Quality score based on real completed projects only — not inspiration reposts.
3. Website Gap scored based on specific named failures, not general impressions.
4. Personalization hook is concrete and specific, not generic ("your site looks old").
5. Prospect tier (Elite / Growth / Low) stated explicitly.
6. Proposed next action is one of: Prepare concept for review / Verify manually / Prepare light outreach draft for review / Add to a local nurture proposal / Do not target.
7. No concept created for Growth Tier without prior prospect engagement.
8. Confirm studio team size is under 20 staff and no dedicated marketing/PR department is evident before finalising score.
