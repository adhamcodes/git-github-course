# MODULE 2 — Branching & Merging (Lessons 9–12)

**Goal:** Isolate work on branches, understand what a branch actually points to, compare lines of history, and merge deliberately without treating branches as mysterious copies of folders.

**Primary references:**
- [Pro Git — Branching](https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell)
- [Learn Git Branching](https://learngitbranching.js.org/) — optional visual practice

> Continue inside your disposable `git-github-lab` repository.

---

## Lesson 9 — Branches are movable names for commits

### LEARN

A Git branch is not a second physical copy of your project. It is a lightweight name/reference that normally points to one commit.

When you commit while a branch is checked out, that branch name moves forward to the new commit.

`HEAD` normally tells Git which branch you currently have checked out.

```text
A---B---C  main, HEAD
```

After:

```bash
git switch -c experiment
```

both names initially point to the same commit:

```text
A---B---C  main, experiment, HEAD -> experiment
```

### DO

```bash
git branch
git switch -c experiment
git branch
git log --oneline --decorate -5
```

Inspect the decoration on the latest commit. You should see both `main` and `experiment` before you make a new commit.

### PREDICT

If you now commit on `experiment`, which branch name will move: `experiment`, `main`, or both?

### TRANSITION CONDITION

Create and switch branches from memory and explain, without using “copy of a folder,” what a branch is.

---

## Lesson 10 — Divergence and comparing branches

### LEARN

Commits belong to history; branches point into that history. Once one branch receives a new commit and another does not, their tips differ.

### DO

On `experiment`:

```bash
echo "experiment branch" > experiment.txt
git add experiment.txt
git diff --staged
git commit -m "Add experiment file"
```

Inspect:

```bash
git log --oneline --graph --decorate --all
git diff main..experiment
```

Switch to `main`:

```bash
git switch main
git status
```

`experiment.txt` may disappear from the working tree because the checked-out commit on `main` does not contain it.

Now create a different commit on `main`:

```bash
echo "main branch" > main-note.txt
git add main-note.txt
git commit -m "Add main branch note"
git log --oneline --graph --decorate --all
```

Now the history truly **diverges**.

### EXPLAIN

Why did switching branches change visible files without deleting history?

### TRANSITION CONDITION

Demonstrate two branches with different commits and use the graph/diff commands to explain how they differ.

---

## Lesson 11 — Merge deliberately: fast-forward vs merge commit

### LEARN

`git merge <branch>` integrates the named branch **into the branch you are currently on**.

That direction matters.

Two common outcomes:

- **Fast-forward** — your current branch is simply behind the other branch with no independent commits, so its pointer can move forward.
- **Three-way merge** — the branches diverged, so Git combines their histories. If changes do not conflict, Git can create a merge commit automatically.

A merge commit is not inherently better or worse than a linear history. Teams choose workflows deliberately.

### DO — merge the divergent history you created

Make sure you are on `main`:

```bash
git switch main
git status
```

Before merging, inspect:

```bash
git log --oneline --graph --decorate --all
```

Merge:

```bash
git merge experiment
```

If no conflict exists, Git should combine the histories.

Inspect again:

```bash
git log --oneline --graph --decorate --all
git status
```

### FAST-FORWARD MINI-DEMO

Create a branch from the current `main`, add one commit, then return to unchanged `main` and merge it:

```bash
git switch -c ff-demo
echo "fast forward" > ff-demo.txt
git add ff-demo.txt
git commit -m "Add fast-forward demo"
git switch main
git merge ff-demo
```

Compare this graph with the divergent merge.

### TRANSITION CONDITION

You can state which branch receives the merge, predict whether a simple scenario can fast-forward, and verify the result using the commit graph.

---

## Lesson 12 — Branch lifecycle, safe deletion, and branch inspection

### LEARN

Branches are cheap and normally short-lived for focused work.

Useful inspection commands:

```bash
git branch
git branch -vv
git branch --merged
git branch --no-merged
```

`git branch -d <name>` is the safer delete: Git refuses in common cases where the branch tip has not been merged into the current history.

`git branch -D <name>` forces deletion of the branch name and can make work harder to find. You do not need it in normal beginner workflow.

Deleting a branch does **not necessarily erase the commit objects immediately**, but do not rely on that as a backup strategy.

### DO

Inspect before deleting:

```bash
git branch --merged
git branch -vv
```

Then delete your merged demo branches:

```bash
git branch -d experiment
git branch -d ff-demo
```

### CLOSED-GUIDE PRACTICE

From `main`:

1. create a focused feature branch
2. make two coherent commits
3. compare it with `main`
4. merge it deliberately
5. inspect the graph
6. safely delete the merged branch

### TRANSITION CONDITION

Perform the full branch lifecycle from memory and explain why deleting a branch name is different from deleting files in your working tree.

---

## Module 2 gate

You are ready for remotes when you can:

- [ ] explain branch and `HEAD` accurately
- [ ] create/switch branches and inspect them
- [ ] create and recognize divergent history
- [ ] compare branches before merging
- [ ] explain fast-forward vs three-way merge at a beginner level
- [ ] merge in the correct direction
- [ ] safely delete merged branches

Then complete **Gate 2 — Branching** in [`../ASSESSMENTS.md`](../ASSESSMENTS.md) before Module 3.