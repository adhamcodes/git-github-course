# MODULE 5 — Fixing Mistakes (Lessons 21-24)

**Goal:** Kill the fear. Learn to undo almost anything in Git. After this module you'll feel safe experimenting, because you'll know how to get back.

**Resources:**
- Git book "Undoing Things": https://git-scm.com/book/en/v2/Git-Basics-Undoing-Things
- GitHub blog — how to undo (concepts): https://github.blog/open-source/git/how-to-undo-almost-anything-with-git/

> 🟢 Safe anytime: `restore`, `stash`, `revert`, `reflog`, `reset --soft`
> 🔴 Can delete work: `reset --hard`. Pause before using it.

---

## Lesson 21 — Undo Before Committing: `restore` + `stash`

### LEARN
- `git restore <file>` throws away unstaged edits to a file (back to last commit).
- `git restore --staged <file>` unstages a file but keeps your edits.
- `git stash` shelves your current changes so you have a clean slate; `git stash pop` brings them back. Great when you need to switch branches mid-edit.

### DO
```bash
echo "oops" >> notes.txt
git restore notes.txt        # change discarded
git status                   # clean

echo "wip" >> notes.txt
git stash                    # changes shelved, working dir clean
git stash pop                # changes return
```

### TRANSITION CONDITION
You can discard an unstaged change with `restore`, and shelve/restore work with `stash`.

---

## Lesson 22 — Fix the Last Commit: `amend` + soft reset

### LEARN
- `git commit --amend` rewrites your LAST commit — fix a typo in the message, or add a forgotten file.
- `git reset --soft HEAD~1` undoes the last commit but KEEPS the changes staged (as if you never committed).
- ⚠️ Only amend/rewrite commits you have NOT pushed/shared yet.

### DO
```bash
echo "line" >> notes.txt
git add . && git commit -m "Add lien"      # oops, typo
git commit --amend -m "Add line"           # fixed message

git reset --soft HEAD~1                     # undo the commit, keep changes staged
git status                                  # changes are staged again
```

### TRANSITION CONDITION
You can fix a bad commit message with `--amend` and undo a commit (keeping the work) with `reset --soft`.

---

## Lesson 23 — `revert` vs `reset` (Safe vs Sharp)

### LEARN
- `git revert <commit>` creates a NEW commit that undoes an old one. **Safe** — history is preserved. Use this for commits you've already pushed.
- `git reset` moves your branch pointer back. `--soft` keeps changes, `--hard` **deletes** them. Powerful but sharp.

### DO
```bash
git log --oneline                 # pick a commit hash to undo
git revert <hash>                 # makes a new "undo" commit (safe)

# Compare (in a throwaway test):
git reset --soft HEAD~1           # undo commit, keep work
# git reset --hard HEAD~1         # undo commit AND delete work — careful
```

### TRANSITION CONDITION
You can explain when to use `revert` (shared/pushed) vs `reset` (local), and you've used `revert` to undo a commit.

---

## Lesson 24 — Recover Lost Work: `reflog`

### LEARN
`git reflog` is your time machine. It logs every place `HEAD` has been — even commits you "lost" via a hard reset. As long as you committed at some point, you can almost always get it back.

### DO
```bash
git reflog                        # see your full history of moves
# find the hash from before your mistake, then:
git checkout <hash>               # look at that state
# or to bring a lost commit back to a branch:
git reset --hard <hash>           # (only when you're sure)
```

### TRANSITION CONDITION
**The fear-killer:** intentionally "lose" a commit with `reset --hard`, then recover it using `reflog`. Once you do this, Git stops being scary.

---

## Module 5 Complete When...
- [ ] You can undo uncommitted changes (restore, stash)
- [ ] You can fix/undo your last commit (amend, reset --soft)
- [ ] You know when to use revert vs reset
- [ ] You can recover lost work with reflog
- [ ] **All Transition Conditions passed → start Module 6**
