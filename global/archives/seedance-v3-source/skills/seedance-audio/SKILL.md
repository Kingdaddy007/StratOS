---
name: seedance-audio
description: 'Design sound layers, specify dialogue lip-sync, and troubleshoot audio failures for Seedance 2.0 video generation. Covers @Audio1 reference input, multi-character constraints, known failure modes (silent output, desync, audio rewrite bug), and the boundary between Seedance 2.0 video generation and the separate Jimeng Digital Human tool. Use when adding audio to a Seedance prompt, fixing lip-sync errors, building multi-character dialogue scenes, or diagnosing why uploaded audio is ignored or replaced.'
license: MIT
---
## STATUS VERIFICATION GATE

Treat platform availability, model limits, filter behavior, enforcement actions, and API status dated February-March 2026 as historical snapshots. Before relying on them, verify current official ByteDance/Seedance documentation. If verification is unavailable, label the claim unverified and avoid presenting it as current fact.

# seedance-audio

Audio design, lip-sync, and multi-character dialogue for **Seedance 2.0 video generation**.

> **Source intelligence**: ByteDance official Seedance 2.0 release blog (seed.bytedance.com), Douyin/抖音 creator community, CSDN practitioner tutorials, Q1 2026. Western sources have minimal real-world data.

---

## ⚠️ Critical Distinction: Two Separate Tools on the Jimeng Platform

The Jimeng platform hosts **two completely different tools** that both involve lip-sync. Mixing them up is the most common documentation error.

| Tool | Model | Where to find | What it does |
|------|-------|--------------|--------------|
| **视频生成 (Video Generation)** | **Seedance 2.0** | Jimeng → Video Generation → Seedance 2.0 | Generates full video clips (4–15 s) with native audio-video joint generation. Audio is part of the generated output. |
| **数字人 (Digital Human)** | **OmniHuman-1** | Jimeng → Digital Human | Portrait animation tool — uploads a face image + audio → generates a talking head with precise lip-sync. Has Master/Quick/Standard modes. |

**This skill covers Seedance 2.0 video generation only.**
The Master mode (大师模式), Quick mode (快速模式), Standard mode (标准模式), and OmniHuman-1 engine all belong to the **Digital Human tool** — not Seedance 2.0. Do not import those concepts here.

---

## Scope

- Seedance 2.0 native audio generation architecture
- Audio reference input system (rhythm, mood, beat, lip-sync)
- Dialogue specification and lip-sync in video generation prompts
- Multi-character lip-sync: the confirmed problem and known workarounds
- Known failure modes and field-tested fixes
- Platform audio constraints (format, duration, file limits)
- Suspended features (Feb 2026 enforcement)
- Sound layer design
- Beat-sync (卡点) technique
- Sound-driven visual timing

## Out of scope

- Digital Human (数字人) feature and its Master/Quick/Standard modes → separate tool
- OmniHuman-1 → separate model, separate feature
- Impact VFX physics → see [skill:seedance-vfx]
- Music-driven camera cuts → see [skill:seedance-camera]
- Copyright enforcement → see [skill:seedance-copyright]

---

## How Seedance 2.0 Audio Works

For most use cases, **describe the sound you want in natural language.** The model understands sound concepts.

- `The scene is silent except for the sound of wind.`
- `A heavy metal track plays.`
- `The sword makes a "shing" sound when drawn.`

Use the `@Audio1` reference only for precise lip-sync or music video beat-matching.

Seedance 2.0 uses a **unified multimodal audio-video joint generation architecture** (统一多模态音视频联合生成架构). Audio and video are generated together — not as separate passes. This is its core architectural difference from older video models.

**What the model generates automatically:**
```
Ambient audio:     environmental sounds matched to visual scene
Background music:  mood-appropriate score matched to visual content  
Sound effects:     event-locked sounds (footsteps, impacts, etc.)
Dialogue:          natural speech with lip-sync when characters talk in the prompt
```

**What audio reference input does:**
When you upload an MP3 as `@Audio1`, you are providing a **reference** that influences:
- Rhythm and pacing of the visual edit
- Mood and tonal character of generated audio
- Beat-sync cut timing
- Voice/speech reference for dialogue generation and lip-sync

Audio input does **not** guarantee the model will play your exact uploaded audio unchanged — it treats the file as a reference, not a playback track. (See Failure Mode 1 for the workaround when you need exact audio preservation.)

---

## Platform Audio Constraints (Hard Limits)

Violating these causes silent failure with no error message.

```
Format:       MP3 only.
              WAV, AAC, OGG, FLAC, M4A are accepted with no error
              but produce no lip-sync or fail silently. #1 silent failure cause.
Duration:     ≤ 15 seconds per audio file. Hard limit.
              Optimal range: 3–8 s for best lip-sync accuracy.
File budget:  Max 3 audio clips per generation (part of the Rule of 12).
Bitrate:      128–320 kbps recommended. Below 64 kbps degrades sync.
Size:         ≤ 10 MB per file.
Noise:        Background noise in audio degrades phoneme recognition.
              Use clean, noise-free recordings.
```

---

## Dialogue and Lip-Sync

Seedance 2.0 generates lip-sync from two pathways:

**Pathway 1 — Text-driven dialogue** (most reliable):
```
Character A says: "We leave at dawn."
Framing: medium close-up, locked-off camera.
Character lips match the dialogue naturally.
```

**Pathway 2 — Audio-driven** (音频驱动):
```
Upload MP3 audio as @Audio1.
In prompt: "Lip-sync matches @Audio1 exactly. Camera: medium close-up, locked."
```

**Key rules for reliable lip-sync:**
- Keep lines short. Long dialogue degrades visual stability.
- Put dialogue in quotes: `Character says: "We leave at dawn."`
- Specify framing: `medium close-up, locked-off camera`
- Remove head/face motion tokens (nodding, turning, shaking) — they compete with the lip engine
- Specify pauses with timing: `"brief pause at 2s, then continues"`

---

## ⚠️ Multi-Character Lip-Sync: Officially Unsolved

ByteDance's own official Seedance 2.0 release blog explicitly states:

> **"Seedance 2.0 仍需继续解决多人口型匹配、偶现音频失真等问题"**
> Translation: "Seedance 2.0 still needs to continue solving multi-person lip-sync matching and occasional audio distortion issues."

This is not a community complaint. It is an official acknowledgment from the Seedance team. Multi-person lip-sync in a single generation is an **open, unresolved problem** in Seedance 2.0 as of Q1 2026.

**What actually happens with multiple characters:**
- The model may animate only one character's mouth
- Both characters may produce garbled or misaligned mouth movements
- Audio routing between two characters is unreliable
- Results are inconsistent even with the same prompt

**The workaround: separate generation + compositing**

This is the field-tested solution used by Douyin creators:

```
STEP 1 — Split dialogue audio by character
  Character A lines → CharA.mp3 (≤8 s each segment, MP3, 128–320 kbps)
  Character B lines → CharB.mp3 (≤8 s each segment, MP3, 128–320 kbps)

STEP 2 — Generate each character separately
  Generation 1: Character A reference image + CharA audio segment 1
    Prompt: "Medium close-up, locked camera. Character A speaks.
             Lip-sync matches @Audio1 exactly. No head rotation."

  Generation 2: Character B reference image + CharB audio segment 1
    Prompt: "Medium close-up, locked camera. Character B listens,
             expression engaged but mouth closed."

  Generation 3: Character B reference image + CharB audio segment 2
    Prompt: "Character B speaks. Lip-sync matches @Audio1. Same framing."

  ...repeat for each dialogue exchange.

STEP 3 — Composite in CapCut / Jianying / Premiere
  - Place both character clips in a PiP (picture-in-picture) layout
  - Apply Linear Mask between the two figure positions
  - Set feather: 15–20% to avoid hard edges
  - When A speaks: A layer = generated video / B layer = static original image
  - When B speaks: swap layers
  - Silent character uses still image = zero extra generation credits
```

**Why this works:**
Each generation has a single face → clean audio routing → reliable sync.
The compositing swap creates the illusion of a two-way conversation without the model ever needing to handle two mouths at once.

---

## Known Failure Modes and Fixes

These failure patterns are documented from Douyin/Bilibili creator community reports, Q1 2026, and the official ByteDance evaluation.

### Failure 1: Model rewrites or replaces uploaded audio (音频被乱改)

**Symptom**: You upload your own MP3; the generated video plays completely different audio — the model has substituted or altered your content.

**Why it happens**: Seedance's native audio generation engine can override the reference when it detects audio it knows how to generate (ambient, music, SFX). The model treats audio input as a reference signal, not a playback instruction. Competing motion tokens amplify this behavior.

**Fixes (field-tested by Douyin creators — 时间戳反向套路法):**
```
Fix A — Explicit preservation instruction:
  Add to prompt: "Audio @Audio1 plays exactly as uploaded from 0s to end.
                  Do not modify or replace the audio content."

Fix B — Remove competing audio tokens:
  Strip all ambient/SFX/music tokens from the prompt.
  Do not write: "background rain", "jazz music", "street noise"
  These invite the native audio engine to take over.

Fix C — Simplify:
  Reduce prompt to under 50 words total.
  Complex prompts increase the chance of audio substitution.
```

### Failure 2: Lip-sync desync / mouth misalignment

**Causes and fixes:**
```
Cause: Audio too long (>10 s is the practical ceiling, not 15 s)
Fix:   Trim to 3–8 s for best results. The 15 s limit is technical maximum,
       not the sweet spot.

Cause: Noisy audio (background music, reverb, crowd noise in the MP3)
Fix:   Clean the audio before uploading.
       Remove background noise, reverb, and crowd sound.

Cause: Fast speech rate
Fix:   Record at ~80% of natural speaking pace. Slightly slower = better sync.

Cause: Head/face motion tokens in prompt
Fix:   Remove "nodding", "turning head", "looking away" — these compete
       with the phoneme engine. Use "locked camera, neutral expression".

Cause: Multi-speaker audio uploaded for single-character generation
Fix:   Always split audio by speaker before uploading. Never upload a
       conversation track and expect one character to lip-sync it.
```

### Failure 3: Multi-character lip-sync broken

**Root cause**: Confirmed open problem in Seedance 2.0 (ByteDance official admission, Feb 2026).

**Fix**: Use the separate generation + compositing workflow described above. Never attempt dual-character lip-sync in a single generation.

### Failure 4: Silent audio format failure

**Symptom**: Upload succeeds, no error shown, but output has no lip-sync or generic generation failure.

**Cause**: File is not MP3. WAV, AAC, OGG, FLAC, M4A all fail silently.

**Fix**: Convert to MP3 (128–320 kbps, ≤15 s, ≤10 MB) before uploading.
```
FFmpeg command: ffmpeg -i input.wav -codec:libmp3lame -b:a 192k output.mp3
```

### Failure 5: Occasional audio distortion

**Status**: Officially acknowledged by ByteDance in Seedance 2.0 release notes.
Unpredictable. No reliable prevention method documented yet by community.

**Current mitigation**: If audio distortion occurs, regenerate. Shorter clips (4–6 s) show lower distortion rates in community testing.

### Failure 6: Audio exceeds 15 seconds → fail or truncation

**Fix — Segmented generation pipeline:**
```
1. Split audio at natural pause points into 3–8 s segments (not 15 s slices)
2. Each segment becomes one generation
3. Use the same character reference image across all segments
4. Maintain identical framing, lighting, camera angle in the prompt
5. Stitch in CapCut/Jianying with 0-frame cuts (dissolves break lip continuity)
```

### Failure 7: Voice cloning / Face-to-Voice features

**Status**: Suspended as of February 2026 (ByteDance enforcement — privacy/copyright).
No timeline for restoration announced.

**Current alternative:**
- Use external TTS tools (ElevenLabs, Minimax TTS, etc.) to generate clean speech MP3
- Upload that MP3 as your audio reference

### Failure 8: Real person face uploads blocked

**Status**: Blocked as of Feb 15, 2026 (ByteDance enforcement).

**Workaround:**
- Generate an AI character illustration first (using Jimeng image generation)
- Use that illustration as the character reference
- Do not upload photos of real people

---
## REFERENCE LOADING RULES

Load `references/extended-guidance.md` when the task needs detailed implementation rules, examples, edge cases, diagnostics, or verification beyond the core workflow above. Inspect its Contents first and load only the matching sections.

## OUTPUT SHAPE

Deliver the requested artifact or decision, the key rationale and tradeoffs, and a concise verification checklist.

## NON-NEGOTIABLE CHECKLIST

1. Apply the core workflow above.
2. Load matching extended guidance for substantive or high-risk work.
3. Preserve user constraints and verify the result before delivery.