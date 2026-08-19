# Extended Guidance

## Contents

- [Sound Layer Structure](#sound-layer-structure)
- [Mix Intent](#mix-intent)
- [Dialogue Prompt Syntax](#dialogue-prompt-syntax)
- [Multi-Language Generation](#multi-language-generation)
- [Beat-Sync / 卡点 Technique](#beat-sync-卡点-technique)
- [Sound-Driven Timing](#sound-driven-timing)
- [Agent Gotchas](#agent-gotchas)

## Sound Layer Structure

Seedance 2.0 generates audio and video jointly. The audio layer influences pacing and cut feel even when not explicitly specified.

```
Ambient bed:      continuous environmental sound
Foreground SFX:   1–2 event-locked sounds
Music cue:        entry time + arc (rising / falling / steady)
Silence design:   deliberate absence — where silence matters most
```

**Compact syntax:**

```
Sound: rain bed + distant train hum.
SFX: chess piece click at 2s.
Music: low piano note enters at 3s, resolves on last frame.
Silence holds final 0.5s.
```

---

## Mix Intent

```
Dialogue scene:   dialogue clean and prominent, music low, ambient subtle
Music-driven:     music leads, ambient secondary, no dialogue
SFX-driven:       environmental sounds prominent, no music
Action:           layered SFX prominent, music rhythmic, no dialogue
Atmospheric:      ambient dominant, sparse SFX, no music or faint drone
```

---

## Dialogue Prompt Syntax

**Single character:**
```
Character A (deep male voice) says: "I told you not to come here."
Framing: medium close-up, locked-off camera.
Lip-sync matches @Audio1 exactly. No head rotation.
```

**Two-character (generate SEPARATELY — see compositing workflow):**
```
Generation 1 (Character A's turn):
  Character A says: "I told you not to come here."
  Character B listens silently, expression neutral.
  [Use Character A reference image only]

Generation 2 (Character B's turn):
  Character B says: "You didn't leave me a choice."
  [Use Character B reference image only]
```

**Timestamp anchoring:**
```
At 0s: character begins speaking quietly.
At 2s: brief pause, character looks down.
At 4s: character resumes with urgency.
Lip-sync follows @Audio1 throughout.
Camera locked, no head rotation.
```

---

## Multi-Language Generation

```
Character speaks in Mandarin: "[dialogue]"
Character speaks in English: "[dialogue]"
Character speaks in Cantonese: "[Cantonese dialogue]"
Character speaks in Sichuan dialect: "[dialect text]"
Character speaks in Japanese: "[dialogue]"
Character speaks in Korean: "[dialogue]"
```

Dialect support confirmed including regional Chinese dialects. 8+ languages supported.

**Best practice**: Use audio reference that matches the written language in the prompt.

---

## Beat-Sync / 卡点 Technique

For music-synced visual editing:

1. Upload scene images + one music reference audio/video
2. Prompt:

```
@Image1 through @Image6 are scene images.
@Audio1 provides rhythm and beat reference.
Cut scene transitions on musical downbeats.
Characters move with energy matching the music tempo.
Visual pacing: fast during chorus, slower during verse.
```

**Beat-sync best practices:**
- 5–7 scene images works best (more = more cuts = more complex choreography)
- Use clearly rhythmic audio (not ambient or atmospheric tracks)
- Short clips (4–8 s) are more reliable than 15 s clips for rhythmic precision
- Beat-sync and dialogue-sync are mutually exclusive in one generation — never mix both

---

## Sound-Driven Timing

Use audio cues to anchor visual events:

```
Sound: thunder crack at 3s.
Visual: lightning illuminates the scene exactly at the thunder crack.
Character flinches at the sound.
```

---

## Agent Gotchas

1. **MP3 only, always.** WAV/AAC/OGG/FLAC/M4A all fail silently. No error message.
2. **15 seconds max per clip. Sweet spot is 3–8 s.** Sync quality drops after 10 s.
3. **Multi-character lip-sync is officially unsolved.** ByteDance said so. Use compositing.
4. **The model treats audio as reference, not playback.** Use timestamp anchoring if you need exact audio preserved.
5. **Clean audio = better sync.** Noisy source degrades phoneme recognition significantly.
6. **Slow the speech.** Slightly slower than natural pace improves sync accuracy.
7. **Remove head motion tokens.** "Nodding", "turning" compete with the lip engine.
8. **Voice clone is suspended** (Feb 2026). Use external TTS instead.
9. **Real face uploads are blocked** (Feb 2026). Use AI-generated character art.
10. **Beat-sync and dialogue are mutually exclusive** in one prompt.
11. **Shorter segments = better sync.** Split long dialogue at natural pauses, not arbitrary cuts.
12. **Maintain consistent framing/lighting across segments** so stitched clips cut invisibly.
13. **Occasional audio distortion is a known bug.** Regenerate if it occurs.
14. **Master/Quick/Standard modes do not exist in Seedance 2.0.** Those belong to the separate Jimeng Digital Human (OmniHuman-1) tool.
