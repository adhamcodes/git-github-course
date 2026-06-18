# MODULE 1 — The Daily Core Loop (Lessons 4-8)

**Goal:** Master the everyday Git cycle you'll use thousands of times: see what changed, stage it, commit it, review history. This is 90% of daily Git.

**Resources:**
- Git book Ch.2 "Git Basics": https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository
- GitHub Docs — committing: https://docs.github.com/en/get-started/using-git

> Do all of this inside your `git-practice` repo (or the `Exercises/` folder). Make junk files freely — this is a playground.

---

## Lesson 4 — The Three Areas + `git status`

### LEARN
Git has three "places" a change can be:
1. **Working directory** — your actual files, where you edit.
2. **Staging area** — a "loading dock" where you gather the changes you want in your next commit.
3. **Repository** — the permanent history of commits.

The flow: edit → **add** (stage) → **commit** (save to history).
`git status` is your map — it tells you which area things are in. Run it constantly.

### DO
```bash
echo "hello" > notes.txt   # create a file
git status                 # see notes.txt as "untracked"
```

### TRANSITION CONDITION
You can name the three areas and explain what `git status` tells you.

---

## Lesson 5 — `add`, `commit`, and Good Messages

### LEARN
- `git add` moves changes to the staging area.
- `git commit` saves a snapshot of staged changes, with a message.
- A good commit message says **what changed and why**, briefly. Use the present tense: *"Add login form"*, not *"added stuff"*.

### DO
```bash
git add notes.txt
git status                       # notes.txt is now "staged"
git commit -m "Add notes file"
git status                       # clean! nothing to commit
```
Now edit the file and do it again:
```bash
echo "second line" >> notes.txt
git add .
git commit -m "Add a second line to notes"
```

### TRANSITION CONDITION
**From memory:** create a file, stage it, and commit it with a clear message. Then change it and commit again.

---

## Lesson 6 — Viewing History: `log`, `diff`, `show`

### LEARN
- `git log` shows your commit history (newest first).
- `git log --oneline` is the compact version.
- `git diff` shows changes you haven't staged yet.
- `git show <commit>` shows what a specific commit changed.

### DO
```bash
git log
git log --oneline
echo "third line" >> notes.txt
git diff                  # see the unstaged change
git show HEAD             # HEAD = your most recent commit
```
(Press `q` to exit the log/diff viewer.)

### TRANSITION CONDITION
You can read your commit history with `git log --oneline` and explain what `git diff` is showing you.

---

## Lesson 7 — `.gitignore`

### LEARN
Some files should NEVER be tracked: secrets (`.env`), dependencies (`node_modules/`), system junk (`.DS_Store`). A `.gitignore` file lists patterns Git should ignore.

### DO
1. Create a file named `.gitignore` with these lines:
```
node_modules/
.env
*.log
.DS_Store
```
2. Make a file that should be ignored and confirm Git skips it:
```bash
echo "secret" > .env
git status        # .env should NOT appear (it's ignored)
git add .
git commit -m "Add gitignore"
```

### TRANSITION CONDITION
You can create a `.gitignore`, add a pattern, and confirm a matching file no longer shows up in `git status`.

---

## Lesson 8 — Core Loop Checkpoint

### LEARN
You now know the full local loop: **status → add → commit → log**. This is what you'll do every working day.

### DO
In your Exercises folder, run a full cycle from scratch with no guide:
- make 2 files, stage one, commit it
- edit it, view the diff, commit again
- add a `.gitignore` that hides a junk file
- view your history with `git log --oneline`

### TRANSITION CONDITION
**The big one:** run the entire core loop (create → status → add → commit → diff → log → .gitignore) from memory, no guide open, explaining each step out loud.

---

## Module 1 Complete When...
- [ ] You understand the three areas
- [ ] You can stage and commit confidently with good messages
- [ ] You can read history and diffs
- [ ] You can use `.gitignore`
- [ ] **All Transition Conditions passed → start Module 2**
