# MODULE 3 — Remotes: Connecting Local Git to GitHub (Lessons 13–16)

**Goal:** Understand the relationship between your local repository and remote repositories, then deliberately clone, fetch, pull, push, and inspect tracking relationships.

**Primary references:**
- [Pro Git — Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)
- [GitHub Docs — Using Git](https://docs.github.com/en/get-started/using-git)

---

## Lesson 13 — Remotes, `origin`, remote-tracking branches, and clone

### LEARN

A **remote** is a saved name for another Git repository URL.

`origin` is only a conventional name. It is not a special server and it does not mean “GitHub” by definition.

When you clone a normal repository, Git usually:

1. creates a local repository
2. downloads the remote history
3. adds a remote named `origin`
4. creates remote-tracking references such as `origin/main`
5. checks out a local branch that tracks the remote branch

A useful model:

```text
local main         <- branch you can commit on
origin/main        <- your local record of where remote main was at last fetch
GitHub main        <- branch that actually exists on the remote server
```

`origin/main` does not magically update every second. `git fetch` refreshes your remote-tracking references.

### DO

Clone one of your own disposable repositories or another small public repo:

```bash
git clone <url>
cd <repo-name>
git remote -v
git branch -vv
git log --oneline --decorate -5
```

Inspect the remote configuration:

```bash
git remote show origin
```

### TRANSITION CONDITION

You can explain the difference between local `main`, `origin/main`, and the remote GitHub branch, and you can inspect a cloned repo's remote/tracking setup.

---

## Lesson 14 — Publish your lab and understand upstream tracking

### LEARN

`git push` transfers commits/refs to a remote repository when the remote accepts them.

On the first push of a local branch, this is common:

```bash
git push -u origin main
```

`-u` / `--set-upstream` records the tracking relationship. After that, plain `git push` and `git pull` usually know which branch to use.

Before pushing, ask:

- Did I inspect my commits?
- Am I pushing the intended branch?
- Is the remote URL correct?
- Could this contain credentials/private data?

### DO

Create an **empty** GitHub repository for your lab. Do not initialize it with files if your local lab already has history.

Inside `git-github-lab`:

```bash
git remote add origin <your-empty-repo-url>
git remote -v
git branch -vv
git log --oneline --decorate -5
```

Push:

```bash
git push -u origin main
```

Inspect tracking again:

```bash
git branch -vv
git status
```

Make one small local commit and push again:

```bash
git push
```

### DEBUG CHECK

If `git remote add origin ...` says `origin already exists`, do **not** keep adding random remotes. Inspect first:

```bash
git remote -v
```

If the URL is wrong, change it deliberately:

```bash
git remote set-url origin <correct-url>
```

### TRANSITION CONDITION

From memory, connect a local repo to an empty GitHub repo, set upstream on the first push, and use `git branch -vv` to explain the tracking relationship.

---

## Lesson 15 — Fetch first: inspect before integrating

### LEARN

`git fetch` contacts the remote and updates remote-tracking refs such as `origin/main` **without integrating those commits into your current branch**.

`git pull` performs a fetch and then integrates according to configuration/options. A common default is merge, but repositories/users may configure rebase or fast-forward-only behavior.

So the durable mental model is:

> **fetch = update knowledge of the remote**
>
> **pull = fetch + integrate into the current branch according to the chosen pull strategy**

When uncertain, fetching first gives you a chance to inspect.

### DO

On GitHub, edit a harmless file in your lab repo and create a commit there.

Back locally, before fetching:

```bash
git status
git log --oneline --decorate --graph --all -8
```

Fetch:

```bash
git fetch origin
```

Inspect again:

```bash
git status
git log --oneline --decorate --graph --all -8
git log main..origin/main --oneline
git diff main..origin/main
```

If your local `main` has not independently diverged, integrate:

```bash
git pull
```

Then inspect:

```bash
git status
git log --oneline --decorate --graph --all -8
```

### TRANSITION CONDITION

You can fetch without changing your checked-out files, inspect commits that exist on `origin/main` but not `main`, and explain why `pull` is more than “download.”

---

## Lesson 16 — Full round trip + divergence awareness

### LEARN

A healthy solo loop is often:

```text
inspect remote/local state
        ↓
fetch / pull when appropriate
        ↓
edit
        ↓
status + diff
        ↓
stage deliberately
        ↓
diff --staged
        ↓
commit
        ↓
push
```

But Git becomes interesting when both sides changed. If local `main` and remote `main` contain different new commits, the histories have **diverged**. Blindly repeating `push`, `pull`, or force commands is not the solution; inspect the graph first.

### CLOSED-GUIDE ROUND TRIP

Perform this from memory:

1. fetch and verify your lab is up to date
2. make and push a local commit
3. create a different browser-side GitHub commit
4. fetch it locally
5. inspect the graph and remote-tracking ref
6. integrate it safely
7. make another local commit and push

### DIVERGENCE SIMULATION

Create one local commit but **do not push it yet**.

Then create a separate commit on GitHub through the browser.

Back locally:

```bash
git fetch
git status
git log --oneline --graph --decorate --all -10
```

You should now see local and remote tips that are not identical.

Do not use force push. For this course, integrate conservatively:

```bash
git pull --no-rebase
```

If Git creates a normal merge or reports a conflict, inspect carefully. Module 6 covers conflict handling in depth.

Then:

```bash
git push
git log --oneline --graph --decorate --all -10
```

### TRANSITION CONDITION

You can complete a local↔GitHub round trip, recognize divergence in the graph, and explain why force-pushing is not a beginner fix for rejected pushes.

---

## Module 3 gate

You are ready for collaboration when you can:

- [ ] explain remotes and why `origin` is only a name
- [ ] distinguish `main`, `origin/main`, and the remote branch
- [ ] inspect remotes with `git remote -v` / `git remote show origin`
- [ ] publish a branch and set upstream
- [ ] use `fetch` to inspect before integrating
- [ ] describe `pull` accurately as fetch + configured integration
- [ ] recognize diverged local/remote history
- [ ] complete a safe round trip without force-pushing

Then complete **Gate 3 — Remote Round Trip** in [`../ASSESSMENTS.md`](../ASSESSMENTS.md) before Module 4.