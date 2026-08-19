# prompt-examples · Seedance 2.0

## Contents

- [Level 1 · Minimal Intent · T2V](#level-1-minimal-intent-t2v)
- [Level 2 · Directed · I2V](#level-2-directed-i2v)
- [Level 3 · Time-Segmented · I2V](#level-3-time-segmented-i2v)
- [Level 4 · Full Choreography · R2V](#level-4-full-choreography-r2v)
- [Chinese Level 2 · I2V](#chinese-level-2-i2v)
- [Chinese Level 3 · Segmented](#chinese-level-3-segmented)
- [Product Ad · T2V](#product-ad-t2v)
- [Architecture Walkthrough · I2V](#architecture-walkthrough-i2v)
- [One-Take Chain · Clip 1 of 4](#one-take-chain-clip-1-of-4)

Compiled plain-text prompts ready for direct use. Each example shows the delegation level, mode, and source JSON key values.

---

## Level 1 · Minimal Intent · T2V

```
Foggy mountain lake at dawn. Static wide shot.
Mist rolls across still water. Trees motionless.
Wind and water ambience.
```

---

## Level 2 · Directed · I2V

```
@Image1 character identity.
Young woman in red coat walks along rain-soaked street.
Slow tracking follow, medium shot.
Cinematic. Neon reflections on wet pavement.
Soft rain ambience.
```

---

## Level 3 · Time-Segmented · I2V

```
@Image1 character identity. @Image2 background lock.
0–3 s: stands at window, back to camera, static wide.
3–7 s: turns slowly, uncertain expression. Slow push-in to medium close-up.
7–10 s: direct eye contact. MCU locked. Soft piano.
Golden side key, soft fill. Cinematic desaturated palette.
```

---

## Level 4 · Full Choreography · R2V

```
@Image1 Fighter A (black jacket). @Image2 Fighter B (grey hoodie).
A throws right hook → B ducks → B counters with left uppercut → A stumbles back.
Rooftop at night. Wet concrete. Neon signs bg.
Handheld low-angle, whip-pan to follow impact at 4 s.
0–4 s slow-motion 0.3×; 4–8 s real-time; 8–10 s 0.5× snap on impact.
Hard side light, practical neon fill.
Crowd ambient sfx, impact punch sfx at 4 s and 8 s.
Maintain character identity throughout.
```

---

## Chinese Level 2 · I2V

```
@Image1 角色锁定。
年轻女性，红色风衣，走在雨夜街道。
缓慢跟拍，中景。
霓虹反光，湿地倒影。电影感。
雨声环境音。
```

---

## Chinese Level 3 · Segmented

```
@Image1 角色。@Image2 背景锁定。
0–3秒：背对镜头站立窗前，固定广角。
3–7秒：缓慢转身，表情迷茫，缓推至中近景。
7–10秒：与镜头直视，MCU定帧。轻柔钢琴声。
黄金侧光，柔和补光。低饱和电影调色。
```

---

## Product Ad · T2V

```
Glass perfume bottle on white marble surface.
Camera slow orbit 90°, hero shot.
Soft studio key, rim highlight, no fill.
Macro depth-of-field. 4K pristine detail.
No text. No people.
```

---

## Architecture Walkthrough · I2V

```
@Image1 building exterior reference.
Drone approaches from south at 40 m altitude, slow descent.
Enters through glass lobby — interior reveal.
Golden hour warm light, clear sky.
Architectural photography style. No people.
```

---

## One-Take Chain · Clip 1 of 4

```
Continuous steadicam follow, no cuts.
Enters narrow alley — market stalls left and right.
Camera height 1.5 m, walk-pace forward.
Warm afternoon light, dust particles.
End frame: open plaza visible ahead.
```

*(Re-upload end frame as @Image1 for next clip.)*
