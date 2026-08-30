# Student Lab — Your Safe Git Playground

The course repository is the textbook. This lab is where you actually use Git.

## Create the lab

Choose a normal development folder on your computer, then:

```bash
mkdir git-github-lab
cd git-github-lab
git init
```

Create a simple README:

```text
# Git & GitHub Lab

Throwaway practice repository for learning Git safely.
```

Then make your first commit:

```bash
git add README.md
git commit -m "Initialize Git learning lab"
```

## Recommended structure

```text
git-github-lab/
├── README.md
├── notes/
├── experiments/
├── conflict-lab/
└── recovery-lab/
```

You may delete, rename, branch, merge, reset, recover, and recreate files here. That is the point.

## Why separate it from the course?

A curriculum repository should stay stable. A Git-learning repository should become messy.

Your lab gives you:

- real commit history
- safe deliberate mistakes
- realistic branch practice
- conflict/recovery experiments
- something you can delete and recreate if necessary

## Lesson workflow

For every lesson:

1. Read the lesson in the course repository.
2. Predict what each Git command will change.
3. Recreate the exercise in this lab.
4. Run `git status` before and after meaningful steps.
5. Use `git diff` or `git diff --staged` to inspect content changes.
6. Record errors/confusion in `notes/`.
7. Pass the Transition Condition without reading the commands.

## Remote practice

When Module 3 begins, create an empty GitHub repository named something like `git-github-lab` and connect this local repository to it. Do not use an important project for remote exercises.

## Destructive-command boundary

Use `recovery-lab/` for exercises involving reset, reflog, discarded edits, or rewritten history. Read **[SAFETY.md](SAFETY.md)** before those lessons.

## Graduation condition

By the end of the course, this lab should contain evidence that you have actually:

- created meaningful commit history
- branched and merged
- resolved conflicts
- pushed/pulled/fetched
- recovered deliberately lost committed work
- practiced a safe revert
- inspected and understood divergence

That history is more valuable than checked boxes in the curriculum repo.
