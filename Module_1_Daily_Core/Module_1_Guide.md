# MODULE 1 — The Daily Core Loop (Lessons 4–8)

**Goal:** Learn the everyday Git loop by understanding repository state, reviewing changes before staging, creating focused commits, and reading history deliberately.

**Primary references:**
- [Pro Git — Recording Changes](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository)
- [GitHub Docs — Using Git](https://docs.github.com/en/get-started/using-git)

> Work only inside your disposable `git-github-lab` repository from [`../STUDENT_LAB.md`](../STUDENT_LAB.md).

---

## Lesson 4 — Working tree, staging area, repository, and `git status`

### LEARN

For beginner work, use this three-part model:

1. **Working tree** — the files you currently see and edit.
2. **Staging area (index)** — the exact snapshot you are preparing for the next commit.
3. **Repository history** — commits Git has already recorded.

```text
edit files
   ↓
working tree
   ↓ git add
staging area
   ↓ git commit
repository history
```

`git status` is your first diagnostic command. It answers questions like:

- Am I inside a repository?
- Which branch am I on?
- What is untracked?
- What changed but is not staged?
- What is staged for the next commit?

### PREDICT

Before running anything, predict what Git will report for the `README.md` you created in Module 0.

### DO

```bash
git status
git status --short
```

`git status --short` is a compact view you will learn to recognize later. Normal `git status` is clearer while you are new.

Create another file:

```bash
echo "first experiment" > notes.txt
git status
```

### EXPLAIN

Why are these files not yet part of Git history even though Git can see them?

### TRANSITION CONDITION

Without the guide, explain the three-part model and use `git status` to identify the current branch and untracked files.

---

## Lesson 5 — Stage deliberately, inspect the staged snapshot, then commit

### LEARN

`git add` does **not** mean “upload.” It copies the selected version of a change into Git's staging area for the next commit.

A professional habit is:

> **inspect → stage intentionally → inspect staged diff → commit**

`git add .` is convenient, but blindly staging everything can accidentally include debug files, generated files, credentials, or unrelated changes. Learn selective staging first.

### DO

Stage only `README.md`:

```bash
git add README.md
git status
```

Inspect exactly what is staged:

```bash
git diff --staged
```

Notice `notes.txt` is still untracked.

Commit the staged snapshot:

```bash
git commit -m "Add student lab README"
git status
```

Now stage and commit `notes.txt` separately:

```bash
git add notes.txt
git diff --staged
git commit -m "Add experiment notes"
```

### COMMIT MESSAGE RULE

For this course, use concise messages that describe one coherent change:

```text
Add student lab README
Document fetch experiment
Fix conflict exercise instructions
```

Avoid messages like `stuff`, `update`, or `final final 2`.

### TRANSITION CONDITION

From memory: create a file, inspect status, stage only that file, inspect it with `git diff --staged`, and commit it with a useful message.

---

## Lesson 6 — Unstaged vs staged diffs, history, and `HEAD`

### LEARN

These commands answer different questions:

- `git diff` — what changed in the working tree compared with the staged/recorded state?
- `git diff --staged` — what will the next commit contain?
- `git log` — what commits exist in history?
- `git show <commit>` — what does one commit contain/change?
- `HEAD` — normally the commit your currently checked-out branch points to.

### DO

```bash
echo "unstaged change" >> notes.txt
git diff
```

Now stage it:

```bash
git add notes.txt
git diff
git diff --staged
```

Notice how the change moved from the unstaged diff to the staged diff.

Commit it, then inspect history:

```bash
git commit -m "Expand experiment notes"
git log --oneline --decorate
git show HEAD
```

Optional visual history:

```bash
git log --oneline --graph --decorate --all
```

### TRANSITION CONDITION

Given an edited file, you can determine whether its change is unstaged or staged and choose the correct diff command to inspect it.

---

## Lesson 7 — `.gitignore`: prevent untracked noise, not erase history

### LEARN

`.gitignore` tells Git which **untracked** paths it should normally ignore.

Common examples:

- dependency/build directories
- temporary logs
- local environment files
- editor/OS noise

Critical rule:

> Adding a tracked file to `.gitignore` does **not** remove it from history or automatically stop tracking it.

Also, `.gitignore` is convenience—not a security system. Never commit real secrets and assume adding them to `.gitignore` later makes them safe.

### DO

Create `.gitignore`:

```text
.env
*.log
scratch/
```

Create ignored files/directories, then inspect:

```bash
echo "fake-local-value" > .env
echo "debug" > debug.log
mkdir scratch
echo "temporary" > scratch/temp.txt
git status
```

They should not appear as normal untracked files.

Ask Git why a path is ignored:

```bash
git check-ignore -v .env
```

Stage **only** `.gitignore` after inspecting:

```bash
git add .gitignore
git diff --staged
git commit -m "Ignore local scratch files"
```

### TRANSITION CONDITION

You can add an ignore rule, verify it with `git status` / `git check-ignore`, and explain why `.gitignore` cannot erase a secret that was already committed.

---

## Lesson 8 — Core loop checkpoint: make a clean history

### GOAL

Prove you can operate the local loop without blindly typing commands.

### DO — CLOSED GUIDE

In your lab, create three sensible changes but commit them as **two coherent commits**.

For each commit:

1. inspect with `git status`
2. inspect the relevant working-tree diff
3. stage only the intended paths
4. inspect with `git diff --staged`
5. commit with a useful message
6. inspect history afterward

Use:

```bash
git status
git diff
git add <path>
git diff --staged
git commit -m "..."
git log --oneline --decorate
```

### DEBUG CHALLENGE

Stage a file, then edit it **again before committing**.

Run:

```bash
git status
git diff
git diff --staged
```

Explain why the same file can have both staged and unstaged changes at once.

### TRANSITION CONDITION

From memory, create two focused commits and explain what each of these represents:

- working-tree change
- staged change
- commit
- `HEAD`

---

## Module 1 gate

You are ready for branching when you can:

- [ ] use `git status` as your first diagnostic
- [ ] distinguish working-tree, staged, and committed state
- [ ] inspect with `git diff` and `git diff --staged`
- [ ] stage intentionally instead of reflexively using `git add .`
- [ ] make focused commits with useful messages
- [ ] inspect history and `HEAD`
- [ ] use `.gitignore` without treating it as a secret-removal tool

Then complete **Gate 1 — Local Git Fundamentals** in [`../ASSESSMENTS.md`](../ASSESSMENTS.md) before Module 2.