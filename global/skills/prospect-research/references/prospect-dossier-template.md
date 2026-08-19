# Prospect Dossier Template

Use one dossier per prospect. Replace bracketed values; do not invent evidence. URLs and observations should be traceable to the page inspected and the inspection date.

```json
{
  "studio_name": "[Studio name]",
  "country": "[Country]",
  "city": "[City]",
  "segment": "luxury residential interior design",
  "website_url": "https://example.com",
  "instagram_url": "https://instagram.com/example",
  "founder_name": "[Founder or principal]",
  "contact_method": "[Email, WhatsApp, or direct message]",
  "website_status": "[No site / weak / broken / strong with named gap]",
  "inspection_date": "YYYY-MM-DD",
  "team_size": null,
  "dedicated_marketing_or_pr": false,
  "evidence": {
    "instagram": "[Recent completed-project evidence, activity, and access signal]",
    "website": "[Named website gap and pages inspected]",
    "completed_projects": "[Evidence that work is real and completed]",
    "premium_positioning": "[Specific language or service signal]"
  },
  "scores": {
    "visual_asset_quality": 0,
    "website_gap": 0,
    "business_maturity": 0,
    "active_online_presence": 0,
    "contact_accessibility": 0,
    "personalization_potential": 0
  },
  "main_gap": "[One concrete failure, not a generic impression]",
  "hero_concept_angle": "[Only required for Elite prospects or after Growth engagement]",
  "outreach_hook": "[Specific observation that proves personalization]",
  "recommended_action": "[Prepare concept for review / Verify manually / Prepare light outreach draft for review / Add to a local nurture proposal / Do not target]",
  "notes": "[Risks, uncertainty, and next verification step]"
}
```

## Scoring limits

The six scores must be integers within these limits: visual asset quality 0–25, website gap 0–20, business maturity 0–10, active online presence 0–15, contact accessibility 0–20, and personalization potential 0–10. The helper calculates the total and tier; it does not decide whether evidence is truthful.

## Evidence gate

Do not finalize a score until both `evidence.instagram` and `evidence.website` are substantive, completed-project evidence is present, and team size/marketing access has been checked or explicitly marked unknown. Unknown facts require `Verify manually`, not confident assumptions.
