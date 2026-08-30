# MODULE 0 — Setup (Lessons 1–3)

**Goal:** Understand what Git and GitHub actually are, install/configure Git safely, and create the disposable student lab used throughout this course.

**Primary references:**
- [Pro Git — Getting Started](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control)
- [GitHub Docs — Get started](https://docs.github.com/en/get-started)
- [Download Git](https://git-scm.com/downloads)

> Before Lesson 1, read [`../../STUDENT_LAB.md`](../STUDENT_LAB.md) if you have not already. This curriculum repo is the textbook; your separate `git-github-lab` repo is where you experiment.

---

## Lesson 1 — Git, GitHub, repositories, and installation

### LEARN

**Git** is a distributed version-control system. It records versions of a project as commits and lets you inspect, compare, branch, combine, and recover those versions locally.

**GitHub** is a hosting/collaboration platform built around Git repositories. It adds remote hosting, Pull Requests, Issues, code review, Actions, Releases, permissions, and social/project features.

A **repository** is a project whose Git metadata and history live in a hidden `.git` directory at its root. Git does not magically upload or back up every edit you make. You deliberately select changes and create commits.

A useful first mental model:

```text
files on your computer
        ↓
      Git
(local history and branches)
        ↓ push / ↑ fetch
     GitHub
(remote copy + collaboration)
```

Git can work without GitHub. GitHub can host Git repositories created with Git.

### DO

Install Git from <https://git-scm.com/downloads>, then open a terminal and run:

```bash
git --version
```

You should see a Git version.

Then answer without looking:

1. Could you commit while offline?
2. Does editing a file automatically create a commit?
3. Is GitHub the same program as Git?

Expected ideas: **yes, no, no**.

### INSPECT

Run:

```bash
git help -a
```

You do not need to understand the list. The point is to notice that Git is a command-line program with many operations; this course will teach the small subset you need first.

### TRANSITION CONDITION

Without the guide open, explain Git, GitHub, commit, and repository in your own words, and show that `git --version` works.

---

## Lesson 2 — Identity, configuration, and privacy

### LEARN

Every commit records an author name and email. These are **commit metadata**, not your GitHub password and not necessarily your login email.

Git has configuration at several scopes. In this course you will mostly use:

- `--global` — your user-level defaults
- `--local` — settings for only the current repository

GitHub can associate commits with your account when the commit email matches a verified account email. If you do not want your personal email exposed in public commit history, GitHub provides a `noreply` address in account email settings.

### DO

Set your identity deliberately:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-chosen-commit-email@example.com"
git config --global init.defaultBranch main
```

Inspect the values and where they came from:

```bash
git config --global --list
git config --show-origin --get user.name
git config --show-origin --get user.email
```

Optional: if you want a different identity in one repository later, use `git config user.name ...` and `git config user.email ...` **without** `--global` while inside that repo.

### TRANSITION CONDITION

You can explain the difference between global and local Git configuration, and you can show your configured name, email, and default branch.

---

## Lesson 3 — Create the student lab and understand `.git`

### LEARN

`git init` creates a new repository by adding a hidden `.git` directory. That directory contains Git's local metadata, refs, object database, and configuration.

Your working files remain ordinary files. Git begins with **no commits**. You will decide what becomes history in Module 1.

For this course, use a disposable practice repository rather than modifying the curriculum repository.

### DO

Create your lab in a convenient location:

```bash
mkdir git-github-lab
cd git-github-lab
git init
git status
```

You should see that you are on `main` with no commits yet.

Create a tiny marker file:

```bash
echo "Git/GitHub student lab" > README.md
git status
```

Notice that Git reports the file as **untracked**. Do not commit it yet; Module 1 starts there.

### GitHub authentication — prepare, do not overcomplicate it

You need a GitHub account before the remote modules. You **do not** need to memorize authentication internals now.

For HTTPS on modern Git for Windows/macOS, Git Credential Manager can normally open a browser sign-in when Git first needs credentials. GitHub CLI (`gh auth login`) and SSH keys are valid alternatives, but neither is required for understanding local Git.

If you already have working GitHub authentication, leave it alone.

### INSPECT

Run:

```bash
git status
git rev-parse --show-toplevel
git config --local --list
```

The first tells you repository state. The second tells you the repository root. The third shows repository-specific configuration.

### TRANSITION CONDITION

From memory, create a new disposable folder, initialize it with Git, create an untracked file, and use `git status` to explain the state. You can also state what the `.git` directory is for.

---

## Module 0 gate

You are ready for Module 1 when you can:

- [ ] distinguish Git from GitHub
- [ ] explain what a repository and commit are at a high level
- [ ] show Git is installed
- [ ] identify your configured commit identity
- [ ] create and inspect a repository with `git init` and `git status`
- [ ] keep course content separate from your disposable student lab

Then continue to **Module 1 — Daily Core**.