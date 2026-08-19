# The I2V Bible: Image-to-Video Best Practices (v5.0)

This guide covers the specific, non-obvious rules for creating high-quality prompts in Image-to-Video (I2V) mode.

## The Golden Rule of I2V

> **Your prompt should ONLY describe what the image CANNOT show: motion and camera movement.**

Do not re-describe the character, the clothing, the background, or the style. The model can see the image. Re-describing it in text creates a conflict that confuses the model and leads to poor results.

---

## The Correct I2V Workflow

1.  **Start with a strong reference image.** It should be clear, well-lit, and show the subject and style you want.
2.  **Upload the image.** It will be tagged as `@Image1`.
3.  **Write a motion-only prompt.** Your prompt should be 1-3 sentences and focus exclusively on what you want to happen *next*.

---

## Prompt Examples

**Reference Image:** A knight in silver armor stands in a forest.

| Goal | Prompt | Why It Works |
| :--- | :--- | :--- |
| **Simple Action** | `The knight raises his sword and points it at the camera. His expression is serious. Slow push-in on his face.` | The prompt only describes the action, the emotion, and the camera move. It doesn't mention the armor, the forest, or the sword itself. |
| **Complex Action** | `The knight performs a fast, three-hit sword combo. The camera is handheld and tracks the blade, with motion blur on the background.` | Again, the prompt is 100% focused on motion and camera. |
| **Facial Expression** | `The knight's eyes widen in surprise. He takes a small step back. Close-up shot.` | I2V is excellent for subtle emotional changes. |

**Reference Image:** A woman in a red dress stands on a city street.

| Goal | Prompt | Why It Works |
| :--- | :--- | :--- |
| **Walking** | `She walks forward, looking confident. The camera tracks with her, medium shot.` | Simple, clear, motion-focused. |
| **Turning** | `She turns her head to look behind her, a worried expression on her face. The camera stays static.` | Describes the emotional shift and the camera action (or lack thereof). |

---

## Common I2V Mistakes

**Reference Image:** A knight in silver armor stands in a forest.

-   **BAD:** `@Image1. A knight in shining silver armor stands in a dark forest. He is holding a large broadsword. He raises his sword.`
    -   **Why it fails:** The prompt wastes 90% of its content re-describing what the model can already see. This creates conflict and noise.

-   **BAD:** `@Image1. The knight attacks.`
    -   **Why it fails:** Too vague. The model doesn't know *how* to attack. You must describe the specific motion.

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
