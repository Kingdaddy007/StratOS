# Intent vs. Precision: Directing the AI (v5.0)

This reference explains the core philosophical shift in the v5.0 skill library: treating Seedance 2.0 as an AI director you collaborate with, not a render engine you command.

## The Old Way: Precision (and why it fails)

The old workflow was based on the idea that more detail equals more control. This led to long, hyper-specific prompts that tried to dictate every single element of the frame.

**Example of a Precision-Based Prompt:**

`A 30-year-old woman with blonde hair in a messy bun, wearing a red silk dress with a high neckline, stands on a wet asphalt street at night. The street is illuminated by a single sodium-vapor streetlight that casts a warm, orange glow. Rain falls at a 15-degree angle. The camera is a 50mm lens at f/1.8, positioned at a low angle, and pushes in slowly over 8 seconds...`

**Why this fails:**

1.  **Cognitive Overload:** This level of detail is difficult for a human to write and even harder for the model to interpret correctly.
2.  **Competing Demands:** The prompt contains dozens of competing demands. `red silk dress` + `wet` + `night` + `orange glow` is a nightmare for the lighting engine.
3.  **It Fights the Model:** This approach treats the model like a dumb renderer. It doesn't leverage the model's own vast knowledge of cinematography and composition.

---

## The New Way: Intent (and why it works)

The new workflow focuses on conveying the **intent** and **feeling** of the shot. You provide the key creative ingredients and let the AI director figure out the best way to cook the meal.

**Example of an Intent-Based Prompt:**

`A woman in a red dress stands alone on a wet city street at night. She looks vulnerable, but there's a hint of defiance in her expression. The mood is lonely and cinematic, like a classic film noir. Slow push-in on her face.`

**Why this works:**

1.  **Clear Creative Direction:** The prompt tells the model the *feeling* to aim for (`lonely`, `cinematic`, `film noir`, `vulnerable`, `defiance`). This is a much more powerful instruction than specifying the f-stop.
2.  **Leverages the Model:** The model knows what "film noir" lighting looks like. It knows how to frame a shot to make someone look "vulnerable." You are collaborating with its knowledge, not fighting it.
3.  **Concise and Effective:** This prompt is shorter, easier to write, and has a much higher success rate.

---

## The Trade-Off

-   **Precision** gives you the *illusion* of control but often leads to failure.
-   **Intent** gives you *less* direct control over the micro-details but *more* control over the final creative result.

Your job as a prompter is to be the **Director of Photography**, not the focus puller. Set the scene, define the mood, and let your AI crew do their jobs.

---

*Maintained by [Emily (@iamemily2050)](https://github.com/Emily2040)*
