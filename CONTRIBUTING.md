# Contributing

Thanks for helping improve this course.

This repository is a textbook and reference implementation. Learner practice belongs in a separate disposable `git-github-lab` repository unless a contribution specifically improves the curriculum itself.

## Before opening a change

1. Read `SAFETY.md` if the change teaches recovery, reset, rebase, force operations, or history rewriting.
2. Keep the course beginner-accessible. Prefer a precise mental model and a small reproducible exercise over adding more commands.
3. Do not add claims of mastery that the learner cannot demonstrate.
4. Do not add secrets, personal tokens, real credentials, or private repository data.
5. Keep external resources supplementary; the core lesson must remain understandable without hunting through tutorials.

## Required local check

Run:

```bash
python scripts/validate_repo.py
```

The same validator runs on both Linux and Windows in GitHub Actions.

## Pull request standard

A useful pull request should explain:

- what learner problem it solves
- what behavior or understanding changes
- how the change was tested
- any safety implications

For changes that add or modify a Git command exercise, include the expected observable repository state before and after the exercise.

## Course design rule

The learning loop is:

> **LEARN → PREDICT → DO → INSPECT → BREAK/RECOVER → EXPLAIN → PROVE**

Not every lesson needs every stage as a heading, but major capabilities should eventually require evidence rather than passive reading.
