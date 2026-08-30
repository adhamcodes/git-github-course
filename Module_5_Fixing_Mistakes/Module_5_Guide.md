# MODULE 5 — Fixing Mistakes (Lessons 21–24)

**Goal:** Replace fear with a recovery process. You will learn the difference between changing files, changing the staging area, undoing commits, and rewriting history.

**Resources:**
- Git book — Undoing Things: https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things
- GitHub — Undoing changes: https://docs.github.com/en/get-started/using-git/undoing-changes

> Before this module, read **[../SAFETY.md](../SAFETY.md)**. Do every destructive experiment only in your separate `git-github-lab` repository.

---

## Lesson 21 — Working-tree vs staging mistakes: `restore` and `stash`

### LEARN
There are two different questions:

- **Do I want to keep the edit but remove it from the next commit?** Use `git restore --staged <file>`.
- **Do I want to discard the uncommitted edit itself?** `git restore <file>` can do that — and the discarded edit may not be recoverable by Git because it was never committed.

`git stash` temporarily stores tracked work so you can get a clean working tree. Treat it as temporary storage, not a long-term backup system.

### PREDICT
Before each command below, say what you think will happen to:

1. the working file,
2. the staging area,
3. commit history.

### DO
```bash
echo "important edit" >> notes.txt
git add notes.txt
git status

git restore --staged notes.txt
git status
# The edit should remain in the file, but it is no longer staged.

git stash
git status
git stash list
git stash pop
```

Now, only in a throwaway file:

```bash
echo "throwaway edit" > disposable.txt
git add disposable.txt
git commit -m "Add disposable file"
echo "uncommitted change" >> disposable.txt
git diff
git restore disposable.txt
```

Inspect the file and explain what disappeared and why.

### TRANSITION CONDITION
Without the guide, demonstrate:
- unstage while keeping an edit,
- stash and restore tracked work,
- explain why `git restore <file>` can be destructive.

---

## Lesson 22 — Fix your latest local commit: `amend` and soft reset

### LEARN
`git commit --amend` replaces your latest commit with a new commit. `git reset --soft HEAD~1` moves the branch back one commit while leaving that commit's changes staged.

Both rewrite local history. They are useful for your own unpublished work. Once other people may depend on the commit, prefer preserving shared history instead of casually rewriting it.

### DO
```bash
echo "line" >> notes.txt
git add notes.txt
git commit -m "Add lien"

git commit --amend -m "Add line"
git log --oneline -3
```

Then make another throwaway commit and inspect a soft reset:

```bash
echo "another line" >> notes.txt
git add notes.txt
git commit -m "Add another line"
git reset --soft HEAD~1
git status
git diff --staged
```

Recommit the staged change when finished.

### TRANSITION CONDITION
Explain why amend/reset change commit identity, demonstrate each on unpublished work, and show the resulting state with `git status`/`git log`.

---

## Lesson 23 — Preserve history with `revert`; understand `reset`

### LEARN
`git revert <commit>` creates a new commit whose patch reverses an earlier commit. That makes it a strong default for undoing a change that has already been shared.

`git reset` moves a branch reference. Modes such as `--soft` and `--hard` additionally control what happens to the staging area and working tree. `--hard` can discard uncommitted work.

### DO
Create a harmless commit specifically for this exercise:

```bash
echo "temporary feature" > temp-feature.txt
git add temp-feature.txt
git commit -m "Add temporary feature"
git log --oneline -3
```

Then revert that commit:

```bash
git revert HEAD
git log --oneline -4
```

Observe that history contains both the original change and the later undo commit.

For reset, use only a disposable branch/repository and inspect state before and after rather than memorizing flags.

### TRANSITION CONDITION
You can explain:
- why revert is suitable for shared history,
- why reset rewrites where a branch points,
- why `reset --hard` requires extra care.

---

## Lesson 24 — Recover committed work with `reflog`

### LEARN
`git reflog` records recent movements of references such as `HEAD` in your local repository. It can often help you find a commit after a reset, rebase, or accidental branch movement.

It is **not** a universal backup for every lost file. Work that was never committed may not be recoverable from reflog.

### DO — controlled recovery drill

1. Make and commit a unique file:

```bash
echo "recover me" > recovery.txt
git add recovery.txt
git commit -m "Add recovery target"
git log --oneline -3
```

2. Record the commit hash somewhere outside the repo for the exercise.
3. In this throwaway lab only, move the branch back:

```bash
git reset --hard HEAD~1
```

4. Find the commit again:

```bash
git reflog
```

5. **Preserve it safely by creating a branch instead of immediately hard-resetting again:**

```bash
git switch -c recovered-work <recovered-commit-hash>
```

6. Confirm `recovery.txt` is back and inspect the graph:

```bash
git log --oneline --graph --decorate --all
```

### TRANSITION CONDITION
From memory, recover a deliberately displaced **committed** change using reflog and a recovery branch, and explain why an uncommitted edit is a different situation.

---

## Module 5 Complete When...

- [ ] You distinguish working-tree, staging, and history recovery
- [ ] You can unstage without discarding work
- [ ] You can stash and restore temporary work
- [ ] You can amend/reset your own unpublished history deliberately
- [ ] You can use revert to preserve shared history
- [ ] You can recover a displaced commit with reflog + a recovery branch

Then complete **Gate 5 — Recovery** in [`../ASSESSMENTS.md`](../ASSESSMENTS.md). Pass it before starting Module 6.