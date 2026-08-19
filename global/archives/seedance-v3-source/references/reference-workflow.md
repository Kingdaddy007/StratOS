# The @reference System: The Director's Most Powerful Tool (v5.0)

This reference explains the `@reference` system, which is the most reliable and powerful way to control Seedance 2.0. The core philosophy is simple: **Show, don't just tell.**

---

## Why Use References?

Text prompts are inherently ambiguous. A reference image or video provides the model with thousands of times more data than a text description. It is the ground truth for your creative vision.

> **Rule of Thumb:** If you can show it, do. Use text to describe what the reference *can't* show, like motion, emotion, and intent.

---

## The Four Types of References

Seedance 2.0 accepts four types of `@` tags. You can use multiple references in a single prompt.

| Reference Type | Tag Syntax | What It Controls | Best For |
| :--- | :--- | :--- | :--- |
| **Image** | `@Image1` | Character identity, clothing, scene composition, lighting, color grade. | Character consistency, style transfer, setting a scene. |
| **Video** | `@Video1` | Motion, action choreography, camera movement, editing rhythm, style. | Action scenes, dance sequences, complex camera work. |
| **Audio** | `@Audio1` | Lip-sync, music timing, beat synchronization, ambient sound. | Dialogue scenes, music videos, sound-driven effects. |
| **Material** | `@materialName` | (In-platform feature) Re-using a previously generated character or style. | Maintaining consistency across a long series of clips. |

---

## The Reference-First Workflow

This is the recommended workflow for any prompt beyond a simple T2V generation.

### 1. Gather Your Assets

Before you write a single word, gather your reference files:

- **Character:** A clear image of your character's face and clothing.
- **Style:** An image or video clip that has the color grading, lighting, and mood you want.
- **Motion:** A video clip that shows the *type* of action or camera movement you need.
- **Audio:** The audio track for dialogue or music.

### 2. Upload and Tag

Upload your assets to the platform. The `@Image1`, `@Video1`, etc., tags are assigned automatically.

### 3. Write a Minimal Prompt

Your text prompt now serves as instructions for how to *use* the references.

**Example: Action Scene**

```
// BAD: Text-only, overspecified
A man in a black leather jacket throws a fast right hook, then a spinning back kick. The camera is handheld and shaky. The scene is a dark alley at night with neon lights...

// GOOD: Reference-first, intent-driven
@Image1 [character image], @Video1 [action movie clip reference].
Transfer the fighting style and camera work from @Video1 to the character in @Image1. The scene is a dark alley at night.
```

### 4. Iterate

Generate a 5-second test clip. If the model has misinterpreted the reference, add a short clarifying sentence to the prompt (e.g., `Focus on the character's fluid kicks, not the punches.`) and re-roll.

---

## Advanced Techniques

- **Style Transfer:** `Apply the color grade and moody lighting from @Image1 to the scene.`
- **Motion Transfer:** `Transfer the dance choreography from @Video1 to the character in @Image2.`
- **Camera Transfer:** `Match the slow, orbital camera movement from @Video1.`
- **Bridging:** `Generate a 5-second transition that bridges the end of @Video1 and the start of @Video2.`

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
