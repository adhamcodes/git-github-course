# MODULE 6 — Real-World Git (Lessons 25-28)

**Goal:** Handle the situations that scare beginners in real projects — merge conflicts, rebasing, releases — plus polish your GitHub presence.

**Resources:**
- Git book "Basic Merge Conflicts": https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
- Git book "Rebasing": https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- GitHub Docs — managing releases: https://docs.github.com/en/repositories/releasing-projects-on-github
- GitHub Docs — profile README: https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile

---

## Lesson 25 — Merge Conflicts (and How to Stay Calm)

### LEARN
A **conflict** happens when two branches change the SAME lines and Git can't decide which to keep. It's normal, not an error. Git marks the spot; you choose what stays.

### DO
1. Create a conflict on purpose:
```bash
git switch main
echo "Color: blue" > color.txt
git add . && git commit -m "Set color blue"

git switch -c change-color
echo "Color: red" > color.txt
git add . && git commit -m "Set color red"

git switch main
git merge change-color        # CONFLICT!
```
2. Open `color.txt`. You'll see conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
3. Delete the marker lines, keep the line you want, then:
```bash
git add color.txt
git commit               # completes the merge
```

### TRANSITION CONDITION
**The big fear-killer:** create a merge conflict on purpose and resolve it cleanly, with no guide open.

---

## Lesson 26 — Rebase Basics (+ the Golden Rule)

### LEARN
`git rebase` replays your branch's commits on top of another branch, giving a cleaner, linear history than a merge. Powerful but has one rule:
- 🔴 **GOLDEN RULE:** never rebase commits you've already pushed/shared. It rewrites history and confuses everyone.

### DO
```bash
git switch -c feature
echo "feature work" > f.txt
git add . && git commit -m "Feature work"

git switch main
echo "main update" > m.txt
git add . && git commit -m "Main moved on"

git switch feature
git rebase main          # replay feature's commits on top of updated main
git log --oneline --graph --all
```

### TRANSITION CONDITION
You can rebase a local branch onto `main` and state the golden rule of rebasing.

---

## Lesson 27 — Tags & Releases

### LEARN
A **tag** marks a specific commit as a version (e.g. `v1.0.0`). On GitHub, a tag can become a **Release** with notes and downloadable files — how projects ship versions.

### DO
```bash
git tag -a v1.0.0 -m "First release"
git tag                       # list tags
git push origin v1.0.0        # push the tag to GitHub
```
Then on GitHub: **Releases** → **Draft a new release** → pick your tag → write notes → publish.

### TRANSITION CONDITION
You can create an annotated tag, push it, and turn it into a GitHub Release.

---

## Lesson 28 — Profile README + GitHub Actions Intro

### LEARN
- A **profile README** is a special repo named exactly like your username (`adhamcodes/adhamcodes`) — its README shows on your GitHub profile page. Great first impression.
- **GitHub Actions** automate tasks (run tests, deploy) when you push. You don't need to master it now — just understand it exists and recognize a workflow file.

### DO
1. Create a repo named exactly your username. Add a `README.md` introducing yourself. Watch it appear on your profile.
2. Look at a `.github/workflows/*.yml` file in any popular repo to see what an automated workflow looks like. Read the top-level keys (`on`, `jobs`, `steps`).

### TRANSITION CONDITION
You have a profile README live on your GitHub profile, and you can explain in one sentence what GitHub Actions does.

---

## Module 6 Complete When...
- [ ] You can resolve a merge conflict calmly
- [ ] You can rebase and you know the golden rule
- [ ] You can tag a version and publish a Release
- [ ] You have a profile README and understand Actions at a high level
- [ ] **All Transition Conditions passed → start the Capstone**
