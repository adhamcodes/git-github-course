# MODULE 6 — Real-World Git (Lessons 25–28)

**Goal:** Handle the situations that make beginners hesitate in real projects: conflicts, diverged history, rebasing, releases, and automation awareness.

**Resources:**
- Git book — Basic Merge Conflicts: https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
- Git book — Rebasing: https://git-scm.com/book/en/v2/Git-Branching-Rebasing
- GitHub Docs — Releases: https://docs.github.com/en/repositories/releasing-projects-on-github
- GitHub Docs — Actions: https://docs.github.com/en/actions

---

## Lesson 25 — Merge conflicts: create one correctly, then resolve it calmly

### LEARN
A conflict happens when Git cannot automatically combine competing changes. A common case is when two branches change the same lines after they have diverged.

A conflict is not corruption. Git stops and asks you to choose the final content.

### DO — create a real conflict on purpose

Start from `main` with a committed baseline:

```bash
git switch main
echo "Color: blue" > color.txt
git add color.txt
git commit -m "Add baseline color"
```

Create a feature branch and change the same line:

```bash
git switch -c change-color
echo "Color: red" > color.txt
git add color.txt
git commit -m "Change color to red"
```

Now **make main diverge** by changing that same line differently:

```bash
git switch main
echo "Color: green" > color.txt
git add color.txt
git commit -m "Change color to green"
```

Now merge:

```bash
git merge change-color
```

Git should stop with a conflict because both branches changed the same line differently.

Inspect:

```bash
git status
```

Open `color.txt`. You will see conflict markers like:

```text
<<<<<<< HEAD
Color: green
=======
Color: red
>>>>>>> change-color
```

Edit the file into the final content you actually want, remove the markers, then:

```bash
git add color.txt
git status
git commit -m "Resolve color conflict"
```

Inspect the result:

```bash
git log --oneline --graph --decorate --all
```

### TRANSITION CONDITION
Without the guide, deliberately create two diverging edits to the same line, trigger a conflict, explain the markers, resolve it, and verify a clean working tree.

---

## Lesson 26 — Rebase basics and the real shared-history rule

### LEARN
Rebase takes a series of commits and replays them onto a new base. That can make a feature branch easier to review and produce a linear history.

Rebase creates new commit identities for the replayed commits. Therefore the important rule is not simply "never rebase anything pushed." The real rule is:

> **Do not rewrite history that other people may already depend on unless the workflow explicitly expects it and you coordinate the rewrite.**

Rebasing your own feature/PR branch is common in many teams. Rebasing a shared stable branch is a very different risk.

### DO
Create divergence:

```bash
git switch main
git switch -c feature-rebase
echo "feature" > feature.txt
git add feature.txt
git commit -m "Add feature work"

git switch main
echo "main update" > main-update.txt
git add main-update.txt
git commit -m "Add main update"
```

Inspect first:

```bash
git log --oneline --graph --decorate --all
```

Then replay the feature branch on top of current `main`:

```bash
git switch feature-rebase
git rebase main
git log --oneline --graph --decorate --all
```

Notice that the feature commit now has a different commit hash.

### TRANSITION CONDITION
You can explain what rebase changes, identify when rewriting history is safe vs risky, and rebase your own disposable feature branch onto `main`.

---

## Lesson 27 — Tags, versions, and GitHub Releases

### LEARN
A Git tag gives a stable name to a particular commit. Version tags such as `v1.0.0` are commonly used to mark releases.

A GitHub Release is a GitHub object built around a tag, usually with release notes and optional downloadable artifacts.

### DO
Check the commit you intend to tag:

```bash
git status
git log --oneline -5
```

Create an annotated tag:

```bash
git tag -a v1.0.0 -m "First release"
git show v1.0.0
git push origin v1.0.0
```

On GitHub, create a Release from that tag and write brief release notes describing what changed.

### TRANSITION CONDITION
You can explain commit vs tag vs GitHub Release, create an annotated tag, inspect it, push it, and create release notes.

---

## Lesson 28 — GitHub Actions awareness + professional repository signals

### LEARN
GitHub Actions runs automated workflows in response to repository events. Common uses include tests, linting, packaging, and deployment.

A workflow normally lives under:

```text
.github/workflows/*.yml
```

At this stage you do not need to become a CI engineer. You need to be able to open a workflow and identify:

- what triggers it (`on`)
- its jobs (`jobs`)
- the steps each job performs (`steps`)
- whether a failed check should stop a merge

A professional GitHub profile is useful too, but profile cosmetics are not evidence of engineering ability. Strong repositories, clear READMEs, useful commits, and real contributions matter more.

### DO
1. Open a workflow from one of your own or a reputable public repository.
2. Identify the trigger, jobs, and major steps.
3. Find a commit or pull request with automated checks and inspect what passed/failed.
4. If you want a profile README, create a public repo named exactly your username and add a truthful README. Do not claim technologies you have not actually used.

### TRANSITION CONDITION
You can explain what CI/Actions does, locate a workflow, identify its trigger/jobs/steps, and explain why a green check is useful but does not prove software correctness by itself.

---

## Module 6 Complete When...

- [ ] You can deliberately create and resolve a real merge conflict
- [ ] You understand divergence rather than treating conflicts as random errors
- [ ] You can rebase your own branch and explain the shared-history boundary
- [ ] You can tag and release a version deliberately
- [ ] You can read a basic GitHub Actions workflow
- [ ] **All Transition Conditions passed → start the Capstone**
