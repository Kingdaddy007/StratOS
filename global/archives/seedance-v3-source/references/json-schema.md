# json-schema · Seedance 2.0 Prompt Schema v3

JSON is for **storage only**. Always compile to plain text before sending to the platform.

## Schema v3

```json
{
  "meta": {
    "mode": "i2v",
    "level": 3,
    "dur": 10,
    "ar": "16:9",
    "res": "1080p",
    "seed": 42
  },
  "ref": {
    "char": "@Image1",
    "bg": "@Image2",
    "cam": "@Video1",
    "bgm": "@Audio1"
  },
  "shot": {
    "subj": "young woman in red coat",
    "act": "turns, looks up, smiles",
    "cam": "slow push-in, MCU",
    "light": "golden backlight, soft fill",
    "style": "cinematic",
    "snd": "wind ambience, soft piano"
  },
  "lock": ["character identity", "background"],
  "exit": "freeze on smile, 0.5s"
}
```

## Field Reference

| Field | Values | Required |
|---|---|---|
| `meta.mode` | `t2v` `i2v` `v2v` `r2v` | yes |
| `meta.level` | `1` `2` `3` `4` | yes |
| `meta.dur` | integer, seconds | yes |
| `meta.ar` | `16:9` `9:16` `4:3` `3:4` `21:9` `1:1` | yes |
| `meta.res` | `720p` `1080p` `2k` | yes |
| `meta.seed` | integer or omit | no |
| `ref.*` | `@TagN` strings or omit | no |
| `shot.subj` | noun phrase | yes |
| `shot.act` | verb phrase + timing | yes |
| `shot.cam` | movement + framing | yes |
| `shot.light` | descriptor | recommended |
| `shot.style` | 1–3 tokens | recommended |
| `shot.snd` | ambient + sfx + music | no |
| `lock` | array of consistency targets | no |
| `exit` | last-frame or timing note | no |

## Compiler Output (plain text from above schema)

```
@Image1 character identity. @Image2 background lock. @Audio1 bgm.
Young woman in red coat turns, looks up, smiles.
Slow push-in to MCU.
Golden backlight, soft fill.
Cinematic.
Wind ambience, soft piano.
Maintain character identity, maintain background. Freeze on smile, 0.5 s.
```

## Budget Triage (over character limit — cut in this order)

| Priority | Field | Cut rule |
|---|---|---|
| 6 (cut last) | `shot.subj` `shot.act` | Never cut |
| 5 | `ref.*` | Never cut |
| 4 | `shot.cam` | Compress to 3 words |
| 3 | `shot.light` | Drop to 1 phrase |
| 2 | `shot.style` | Reduce to 1 token |
| 1 (cut first) | `shot.snd` `exit` | Remove entirely |

## Segmented Shot (Level 3–4)

```json
{
  "seg": [
    { "t": "0-4s", "act": "stands still, wind moves coat", "cam": "static wide" },
    { "t": "4-8s", "act": "turns head slowly",             "cam": "slow push-in" },
    { "t": "8-10s","act": "direct eye contact, smiles",    "cam": "MCU, locked" }
  ]
}
```

Compiled:
```
0–4 s: stands still, wind moves coat. Static wide.
4–8 s: turns head slowly. Slow push-in.
8–10 s: direct eye contact, smiles. MCU, locked.
```
