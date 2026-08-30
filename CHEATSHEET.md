# Git & GitHub Cheatsheet

> Quick reference for this course. Use it to remember syntax—not to skip understanding repository state.
>
> `<thing>` means “replace this with your own value.” Do not type the angle brackets.

## First response when confused

```bash
git status
git branch -vv
git log --oneline --graph --decorate --all -12
```

Then inspect before changing anything.

---

## Setup

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "your-commit-email@example.com"
git config --global init.defaultBranch main
git config --global --list
git config --show-origin --get user.email
```

## Create / copy a repository

```bash
git init
git clone <url>
git rev-parse --show-toplevel
```

## Daily local workflow

```bash
git status                     # overall repository state
git status --short             # compact state
git diff                       # unstaged changes
git add <path>                 # stage intended path
git diff --staged              # inspect next commit snapshot
git commit -m "Useful message"
git log --oneline --decorate
git show HEAD
```

`git add .` is valid, but inspect first. Do not use it reflexively in a messy working tree.

## `.gitignore`

Example:

```text
.env
*.log
node_modules/
scratch/
```

```bash
git check-ignore -v <path>
```

`.gitignore` normally affects untracked files. It does not remove an already tracked secret from history.

## Branching

```bash
git branch
git branch -vv
git switch <branch>
git switch -c <new-branch>
git diff main..<branch>
git merge <branch>             # merges INTO your current branch
git branch --merged
git branch --no-merged
git branch -d <merged-branch>
```

History graph:

```bash
git log --oneline --graph --decorate --all
```

## Remotes and GitHub

```bash
git remote -v
git remote show origin
git remote add origin <url>
git remote set-url origin <url>
git fetch origin
git branch -vv
git log main..origin/main --oneline
git diff main..origin/main
git push -u origin main
git push
git pull
```

Mental model:

- `main` = your local branch
- `origin/main` = your local record of remote `main` from the last fetch
- `origin` = conventional remote name, not magic
- `fetch` = update remote knowledge without integrating into current branch
- `pull` = fetch + integrate using the selected/configured strategy

## Fork workflow

Typical external contribution setup:

```bash
git clone <your-fork-url>
cd <repo>
git remote add upstream <original-repo-url>
git remote -v
git fetch upstream
```

Common convention:

```text
origin   → your fork
upstream → original project
```

## Undo / recovery — choose by state

### Unstage while keeping your edits

```bash
git restore --staged <file>
```

### Discard unstaged file edits — DESTRUCTIVE TO THOSE UNCOMMITTED EDITS

```bash
git diff <file>                 # inspect first
git restore <file>
```

### Temporarily shelve work

```bash
git stash push -m "description"
git stash list
git stash pop
```

### Fix the latest local/unshared commit

```bash
git commit --amend
```

This rewrites that commit. Be careful if it has already been shared.

### Undo a shared commit while preserving history

```bash
git revert <commit>
```

### Move branch history locally

```bash
git reset --soft HEAD~1         # move branch back, keep changes staged
git reset --mixed HEAD~1        # move back, keep changes unstaged (default mode)
```

### Destructive reset

```bash
git reset --hard <commit>
```

This can destroy uncommitted working-tree/index changes. Use only in a disposable/recovery exercise when you understand the target.

### Recover displaced committed work

```bash
git reflog
git switch -c recovery <commit-from-reflog>
```

Creating a recovery branch is usually safer for a learner than immediately hard-resetting onto a found hash.

## Merge conflicts

When a merge conflicts:

```bash
git status
```

Open conflicted files and resolve the marked regions, then:

```bash
git add <resolved-file>
git status
git commit
```

Abort a merge **before completing it** if you want to return to the pre-merge state:

```bash
git merge --abort
```

## Rebase

```bash
git rebase main
```

Rebase rewrites commits. Avoid rewriting shared history unless you understand the consequences and the project workflow expects it.

Useful abort command during a troubled rebase:

```bash
git rebase --abort
```

## Push rejection / divergence

Do **not** jump straight to force push.

Inspect:

```bash
git fetch
git status
git log --oneline --graph --decorate --all -15
```

Then choose the appropriate integration/recovery strategy.

## Force push — advanced boundary

If a workflow intentionally requires rewriting a branch you own, `--force-with-lease` is generally safer than raw `--force` because it checks that the remote has not moved unexpectedly:

```bash
git push --force-with-lease
```

This is still history rewriting. It is **not** a generic fix for push errors.

## Tags and releases

```bash
git tag
git tag -a v1.0.0 -m "Release v1.0.0"
git show v1.0.0
git push origin v1.0.0
```

A Git tag points at a Git object/commit. A GitHub Release is a GitHub product object commonly built around a tag with release notes/assets.

## Helpful inspection

```bash
git log --oneline --graph --decorate --all
git show <commit>
git blame <file>
git reflog
git remote -v
git branch -vv
```

---

## GitHub vocabulary

- **Repository** — a Git repository hosted on GitHub.
- **Branch** — a movable Git reference used for a line of development.
- **Commit** — a recorded project snapshot with metadata and parent history.
- **Remote** — a saved name for another repository URL.
- **Fork** — a GitHub repository created under another namespace from an existing GitHub repository.
- **Pull Request** — a GitHub review/discussion workflow proposing branch changes for integration.
- **Issue** — a repository discussion/tracking object; projects use them for bugs, tasks, proposals, and more.
- **Merge** — integrate histories/changes from another branch into the current branch.
- **Tag** — a Git reference commonly used to mark versions.
- **Release** — GitHub release metadata/notes/assets commonly associated with a tag.

## The small set worth developing muscle memory for

```bash
git status
git diff
git add <path>
git diff --staged
git commit -m "message"
git log --oneline --graph --decorate --all
git fetch
git pull
git push
```

You do **not** need every Git command memorized. You need to inspect state, understand the operation you are about to perform, and know where to look when you forget syntax.