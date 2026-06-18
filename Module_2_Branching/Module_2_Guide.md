# MODULE 2 — Branching & Merging (Lessons 9-12)

**Goal:** Work on changes safely in separate branches and combine them back into `main`. Branching is how real teams (and smart solo devs) avoid breaking working code.

**Resources:**
- Git book Ch.3 "Branching": https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell
- Learn Git Branching (visual game): https://learngitbranching.js.org/

---

## Lesson 9 — What Branches Are + Create/Switch

### LEARN
A **branch** is a separate line of work. `main` is your stable version. You make a new branch to try something, and `main` stays safe. A branch is just a movable pointer to a commit — cheap and fast.

### DO
```bash
git branch                 # list branches; * marks where you are
git switch -c feature-x    # create AND switch to a new branch
git branch                 # now you're on feature-x
```
(Older syntax that does the same: `git checkout -b feature-x`.)

### TRANSITION CONDITION
You can create a new branch, switch to it, and confirm which branch you're on with `git branch`.

---

## Lesson 10 — Committing on a Branch

### LEARN
Commits you make on a branch stay on that branch. `main` doesn't change until you merge. This is the safety of branches.

### DO
```bash
# on feature-x:
echo "experimental feature" > feature.txt
git add .
git commit -m "Add experimental feature"

git switch main
ls            # feature.txt is GONE here — it only exists on feature-x
git switch feature-x
ls            # it's back
```

### TRANSITION CONDITION
You can make commits on a branch and demonstrate that `main` is unaffected until you merge.

---

## Lesson 11 — Merging

### LEARN
`git merge` brings a branch's commits into your current branch. Two common cases:
- **Fast-forward:** `main` hasn't changed, so Git just slides `main` forward. Clean.
- **Merge commit:** both branches changed; Git creates a new commit that ties them together.

### DO
```bash
git switch main          # go to the branch you want to merge INTO
git merge feature-x      # bring feature-x's work into main
ls                       # feature.txt is now on main
git log --oneline        # see the merged history
```

### TRANSITION CONDITION
You can merge a feature branch into `main` and confirm the work arrived.

---

## Lesson 12 — Deleting Branches + Practice

### LEARN
Once a branch is merged, delete it to keep things tidy. `git branch -d <name>` deletes a merged branch safely (it refuses if there's unmerged work, which protects you).

### DO
```bash
git branch -d feature-x
git branch                # it's gone
```
Then practice the whole flow on your own: branch → commit → switch → merge → delete.

### TRANSITION CONDITION
**From memory:** create a branch, commit on it, merge it into `main`, and delete it — explaining each step.

---

## Module 2 Complete When...
- [ ] You can create and switch branches
- [ ] You understand commits are isolated to their branch
- [ ] You can merge a branch into `main`
- [ ] You can delete a merged branch
- [ ] **All Transition Conditions passed → start Module 3**
