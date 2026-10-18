# understanding-llms

Build a GPT-style language model from scratch in PyTorch, learning every concept
through mastery-based tutoring (Bloom's 2 sigma: 1:1 tutoring + mastery gates).

## The loop (repeat per module)

1. `/tutor`  – learn the concept Socratically. You write all the code.
2. `/assign` – get the module's gate tasks (explain, implement, debug, transfer).
3. Do the work in `modules/<NN_name>/`. Run `pytest modules/<NN_name>`.
4. `/grade`  – independent examiner checks your work and hidden tests.
5. Pass -> next module. Fail -> corrective tasks, then re-grade on a fresh variant.
6. `/review` – every ~3 modules: spaced retrieval quiz + curriculum adjustment.

Use `/lookup <question>` any time for quick PyTorch API questions.

## Which model for which command

Pick the model in Claude Desktop's model picker BEFORE running the command.

| Command   | Role               | Model            |
|-----------|--------------------|------------------|
| /plan     | Curriculum architect | GPT-6 Astra    |
| /review   | Curriculum architect | GPT-6 Astra    |
| /tutor    | Socratic tutor     | GPT-6.1 Sol      |
| /assign   | Examiner           | Kimi K3          |
| /grade    | Examiner           | Kimi K3          |
| /lookup   | Reference desk     | Gemini 3.8 Flash |

Rule: the tutor and the examiner must be different models.
Start a NEW chat whenever you switch roles, so contexts don't bleed together.

## Folder map

- `CLAUDE.md` – rules every model follows (read automatically)
- `roles/` – detailed instructions for each role
- `state/` – shared memory between models (curriculum, mastery log, profile)
- `modules/` – your code, one folder per module
- `grading/hidden/` – examiner-only tests. Honor system: don't open them.
- `templates/` – formats the examiner uses for assignments and reports
- `notes/` – your own explanations, written in your words
