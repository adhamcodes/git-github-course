# Module 1 Exercises — Daily Core

Work only in your disposable student lab.

## Challenge 1 — Three states of one file

Create a file, stage it, then modify it again before committing.

Before running any corrective command, predict what each of these will show:

```bash
git status
git diff
git diff --staged
```

Explain why the same file can appear in both staged and unstaged state.

## Challenge 2 — Selective commit

Create changes in at least three files. Make one focused commit that intentionally includes only part of the work.

**Evidence:** show the staged diff before the commit and explain why the omitted changes did not belong in it.

## Challenge 3 — Ignore-rule trap

Track a harmless fake configuration file, then add its pattern to `.gitignore`.

Predict whether Git stops tracking it. Test the prediction and explain why `.gitignore` is not a secret-removal mechanism.

## Boss check — Inspect before acting

Have another person or future-you make several mixed changes in the lab. Without immediately staging anything, determine:

- what changed
- what is staged
- what is not staged
- what is untracked
- what belongs in the next commit

**Pass when:** your first instinct is inspection, not `git add .`.
