# MODULE 4 — Collaboration (Lessons 17-20)

**Goal:** Work with others (and your future self) the way real teams do: forks, Pull Requests, code review, and Issues. This is the part of GitHub that gets you hired.

**Resources:**
- GitHub Docs — About Pull Requests: https://docs.github.com/en/pull-requests
- GitHub Docs — About forks: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks
- First Contributions (practice repo): https://github.com/firstcontributions/first-contributions

---

## Lesson 17 — Forks vs Clones

### LEARN
- **Clone** = copy a repo to your computer.
- **Fork** = make your OWN copy of someone else's repo *on GitHub*, under your account. You fork when you want to contribute to a project you don't own.
- Typical flow: **Fork** (on GitHub) → **Clone** your fork (to your computer) → work → push to your fork → open a Pull Request to the original.

### DO
1. Go to https://github.com/firstcontributions/first-contributions
2. Click **Fork** (top right). Now there's a copy under `your-username/first-contributions`.
3. Clone YOUR fork:
```bash
git clone <url-of-your-fork>
cd first-contributions
```

### TRANSITION CONDITION
You can explain the difference between fork and clone, and you've forked + cloned a repo.

---

## Lesson 18 — Creating a Pull Request

### LEARN
A **Pull Request (PR)** says: *"I made some changes on a branch — please review and merge them."* It's the standard way to propose changes. Always work on a branch, not directly on `main`.

### DO
```bash
git switch -c add-my-name
# edit the Contributors file to add your name (follow the repo's README)
git add .
git commit -m "Add <your-name> to contributors"
git push -u origin add-my-name
```
Then on GitHub: you'll see a **"Compare & pull request"** button → click it → write a title and description → **Create pull request**.

### TRANSITION CONDITION
You can push a branch and open a Pull Request from it on GitHub.

---

## Lesson 19 — Code Review + Merging a PR

### LEARN
On a PR, reviewers leave **comments** on specific lines, request changes, or approve. When approved, someone **merges** it. You respond to comments by pushing more commits to the same branch — the PR updates automatically.

### DO
1. On your own PR (or a practice repo), explore the **Files changed** tab.
2. Add a comment on a line.
3. Make another commit on the branch and push — watch the PR update.
4. If it's your repo, click **Merge pull request** to merge it.

### TRANSITION CONDITION
You can read a PR's diff, leave a review comment, update a PR with a new commit, and merge it.

---

## Lesson 20 — Issues + Linking PRs

### LEARN
**Issues** are tickets: bug reports, feature ideas, tasks. You can link a PR to an issue so merging the PR auto-closes the issue (write `Closes #12` in the PR description).

### DO
1. In one of your repos, open the **Issues** tab → **New issue** → describe a small task.
2. Create a branch, make the change, open a PR, and write `Closes #1` in the description.
3. Merge the PR → watch the issue close automatically.

### TRANSITION CONDITION
You can open an Issue and close it automatically by merging a linked PR.

---

## Module 4 Complete When...
- [ ] You understand fork vs clone and the contribution flow
- [ ] You can open a Pull Request
- [ ] You can review, update, and merge a PR
- [ ] You can use Issues and link them to PRs
- [ ] **All Transition Conditions passed → start Module 5**
