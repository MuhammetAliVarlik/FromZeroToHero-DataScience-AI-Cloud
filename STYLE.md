# Writing Style Guide

This course uses **simplified technical English**. The rules come from ASD-STE100 (Simplified Technical English), the standard that aerospace manuals use. We use the STE writing rules, but we do not use the STE dictionary. Technical terms such as *gradient*, *embedding* or *Kubernetes* are allowed.

Why: many readers are not native English speakers. Short, direct sentences are easier to read, to translate and to remember.

`tools/style_check.py` checks the measurable rules. Run it on every notebook that you change:

```bash
python tools/style_check.py "M26-LLM Foundations/10-Decoding Strategies.ipynb"
python tools/style_check.py --module M26      # all notebooks in one module
```

## 1. Sentences

1. Write **one idea in each sentence**.
2. Keep **procedure sentences at 20 words or fewer**. A procedure sentence tells the reader to do something.
3. Keep **descriptive sentences at 25 words or fewer**.
4. Use the **active voice**. Write "The optimizer updates the weights", not "The weights are updated by the optimizer".
   *Exception:* use the passive voice when the actor is not important ("The data is stored in Parquet").
5. Use the **present tense** for facts and for what the code does.
6. Put **conditions first**: "If the loss increases, decrease the learning rate."

## 2. Instructions

1. Use the **imperative**: "Run the cell.", "Install the package."
2. Write **one instruction in each sentence**. Do not join two actions with "and then".
3. Use a **numbered list** for steps that must happen in a sequence.
4. Give the **reason after the instruction**, in a new sentence if necessary.

## 3. Words

1. Use **one word for one meaning** in a lesson. If you start with *feature*, do not change to *attribute* or *column* for the same thing.
2. **Define a technical term the first time** you use it in a lesson. Use bold for the term: "The **learning rate** is the size of each optimisation step."
3. Do not use **idioms** or figures of speech: "a piece of cake", "under the hood", "the elephant in the room", "silver bullet".
4. Do not use **ambiguous phrasal verbs** when a simple verb exists: *find* (not *figure out*), *remove* (not *get rid of*), *start* (not *kick off*), *examine* (not *look into*).
5. Do not use **vague words**: *very*, *really*, *quite*, *basically*, *simply*, *obviously*, *just*. If something is "very fast", give the number.
6. Do not use **hype words**: *magic*, *revolutionary*, *game-changer*, *mind-blowing*, *ultimate*, *physics of* (when the topic is not physics).
7. Write **numbers with units**: "4 GiB VRAM", "120 ms", "0.85 F1".

## 4. Paragraphs and structure

1. Keep **paragraphs at 6 sentences or fewer**. Start with the main point.
2. Use **headings** for each concept. Use numbered headings in a lesson: `## 1. ...`, `## 2. ...`.
3. Use **lists** for three or more parallel items.
4. Use **tables** to compare options.

## 5. The lesson template

Every lesson notebook has these parts, in this sequence:

1. **Title and goal.** What the reader can do after the lesson.
2. **Concept.** The idea in plain words, then the mathematics (LaTeX) where it helps.
3. **Hands-on code.** Runnable cells with real output. Use real public data when the topic needs it. If the data is synthetic, say so in one sentence.
4. **Analysis.** Explain the numbers that the code printed. The text must agree with the output.
5. **Visualisation.** At least one plot with a title, axis labels and units.
6. **Insight.** One italic line that starts with `*Insight:`. It gives the key lesson in one or two sentences.
7. **Real-World Use Case or Analogy.** Connect the idea to a real situation.

## 6. Code and output

1. Code comments follow the same rules: short, active, present tense.
2. Never write a number in the text that the code did not produce. Run the notebook, then write the explanation.
3. Do not hide a failure behind a "sandbox" or "simulation" fallback. If a lesson needs special hardware or a service, say so at the top of the lesson. Then show how to run it with free tools.

## Examples

| Do not write | Write |
| :--- | :--- |
| Basically, under the hood, the tokenizer kind of splits text into pieces. | The tokenizer splits the text into tokens. |
| The model is then trained and after that it is evaluated on the test set by us. | Train the model. Then evaluate it on the test set. |
| This revolutionary technique gives very fast inference. | This technique reduces inference latency from 120 ms to 35 ms. |
| Let's figure out why the loss blew up. | Find why the loss increased. |
