# MODULE 3 — Remotes: Connecting to GitHub (Lessons 13-16)

**Goal:** Move your work between your computer and GitHub — clone, push, pull, fetch. This is how your code gets backed up and shared.

**Resources:**
- Git book Ch.2 "Working with Remotes": https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes
- GitHub Docs — push to remote: https://docs.github.com/en/get-started/using-git/pushing-commits-to-a-remote-repository

---

## Lesson 13 — Remotes Concept + Clone

### LEARN
A **remote** is a version of your repo hosted elsewhere (usually GitHub). The default remote is named **`origin`**.
- `git clone <url>` copies a GitHub repo (and its full history) to your computer.

### DO
1. On GitHub, find any small public repo (or one of your own) and click the green **Code** button → copy the HTTPS URL.
2. Clone it:
```bash
git clone <paste-the-url>
cd <repo-name>
git remote -v        # shows 'origin' pointing at the URL
```

### TRANSITION CONDITION
You can clone a repo from GitHub and show its remote with `git remote -v`.

---

## Lesson 14 — Push (Send Your Work Up)

### LEARN
`git push` sends your local commits to GitHub. The first time on a new branch, use `-u` to set the "upstream" so future pushes are just `git push`.

### DO
1. On GitHub, create a NEW empty repo (no README). Copy its URL.
2. In your local `git-practice` repo:
```bash
git remote add origin <paste-the-url>   # link local repo to GitHub
git push -u origin main                 # first push, sets upstream
```
3. Refresh the GitHub page — your files are there!
4. Make a change locally, commit it, then:
```bash
git push        # no -u needed now
```

### TRANSITION CONDITION
You can link a local repo to a GitHub repo and push commits so they appear on GitHub.

---

## Lesson 15 — Pull vs Fetch (Get Work Down)

### LEARN
- `git fetch` downloads new commits from GitHub but does NOT change your files yet (safe look).
- `git pull` = `fetch` + `merge` — downloads AND updates your files in one step.

### DO
1. On GitHub, edit a file directly in the browser (pencil icon) and commit it.
2. Back in your terminal:
```bash
git fetch        # downloads the change, your files unchanged yet
git status       # tells you you're "behind"
git pull         # now your local files update
```

### TRANSITION CONDITION
You can explain the difference between `fetch` and `pull`, and use `pull` to bring GitHub changes to your computer.

---

## Lesson 16 — The Full Local/Remote Loop

### LEARN
The everyday remote loop: `pull` (get latest) → work → `add`/`commit` → `push`. Pull before you start, push when you're done.

### DO
From scratch, with no guide:
- create a new GitHub repo
- connect a local folder to it
- push some commits
- edit on GitHub, then pull the change down
- make a local change and push it back

### TRANSITION CONDITION
**From memory:** complete a full round trip — local commit → push → edit on GitHub → pull → push again.

---

## Module 3 Complete When...
- [ ] You can clone a repo
- [ ] You can connect a local repo to GitHub and push
- [ ] You understand and can use fetch vs pull
- [ ] You can do a full local/remote round trip
- [ ] **All Transition Conditions passed → start Module 4**
