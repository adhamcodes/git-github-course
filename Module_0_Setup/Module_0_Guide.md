# MODULE 0 — Setup (Lessons 1-3)

**Goal:** Understand what Git and GitHub actually are, get Git working on your computer, and connect it to GitHub.

**Resources:**
- Official Git book (free): https://git-scm.com/book/en/v2
- GitHub Docs — Get started: https://docs.github.com/en/get-started
- Download Git: https://git-scm.com/downloads

---

## Lesson 1 — Git vs GitHub + Install

### LEARN
- **Git** is a program on YOUR computer that records snapshots ("commits") of your files over time. It works offline.
- **GitHub** is a website that stores Git repositories online so you can back them up and share/collaborate.
- Analogy: Git is the "save with full history" tool; GitHub is the cloud where you park and share those saves.

### DO
1. Install Git from https://git-scm.com/downloads (pick your operating system).
2. Open your terminal (Windows: "Git Bash"; Mac: "Terminal"; Linux: your terminal).
3. Check it worked:
```bash
git --version
```
You should see a version number like `git version 2.x.x`.

### TRANSITION CONDITION
You can explain, in one sentence each, what Git is and what GitHub is — and `git --version` prints a version on your machine.

---

## Lesson 2 — Configure Git

### LEARN
Git stamps your name and email on every commit. You set this once. This is not a login — it's just a label on your snapshots.

### DO
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"   # use the email on your GitHub account
git config --global init.defaultBranch main
git config --list      # check your settings (press q to quit)
```

### TRANSITION CONDITION
`git config --list` shows your name, email, and `init.defaultBranch=main`.

---

## Lesson 3 — Your First Repo + Connect to GitHub

### LEARN
- A "repository" (repo) is just a folder that Git is watching.
- `git init` starts watching a folder.
- To connect to GitHub you need to **authenticate**. The easiest beginner-friendly way is the **GitHub CLI** (`gh`) or signing in when prompted. (SSH keys are an alternative you can learn later.)

### DO
1. Make a practice folder and turn it into a repo:
```bash
mkdir git-practice
cd git-practice
git init
```
You'll see: *Initialized empty Git repository*. A hidden `.git` folder now exists — that's Git's brain. Don't touch it.

2. Create a free account at https://github.com if you don't have one.
3. (Recommended) Install the GitHub CLI from https://cli.github.com and run:
```bash
gh auth login
```
Follow the prompts (choose GitHub.com → HTTPS → login with browser). This sets up authentication so pushing later "just works."

### TRANSITION CONDITION
You can create a new folder, run `git init`, and confirm it's a repo (`git status` works inside it without error). You have a GitHub account and have logged in (via `gh auth login` or a browser sign-in).

---

## Module 0 Complete When...
- [ ] Git is installed and configured with your name/email
- [ ] You can create a repo with `git init`
- [ ] You have a GitHub account and are authenticated
- [ ] **All Transition Conditions above passed → start Module 1**
