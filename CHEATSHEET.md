# Git & GitHub Cheatsheet

> Every command in this course, in one place. Bookmark it. When you forget a command (you will, everyone does), come here.
> `<thing>` means "replace this with your own value." Don't type the angle brackets.

---

## Setup (one time)
```bash
git --version                                  # check Git is installed
git config --global user.name "Your Name"      # who you are
git config --global user.email "you@email.com" # your email (use your GitHub one)
git config --global init.defaultBranch main    # name the first branch "main"
git config --list                              # see your settings
```

## Start a Project
```bash
git init                  # turn the current folder into a Git repo
git clone <url>           # copy a GitHub repo to your computer
```

## The Daily Core Loop
```bash
git status                # what's changed? (run this CONSTANTLY)
git add <file>            # stage one file for the next commit
git add .                 # stage everything that changed
git commit -m "message"   # save a snapshot with a description
git log                   # see the history of commits
git log --oneline         # history, short version
git diff                  # see exact changes you haven't staged yet
git show <commit>         # see what a specific commit changed
```

## .gitignore
```
# Put this in a file named .gitignore to tell Git what to NEVER track:
node_modules/
.env
*.log
.DS_Store
```

## Branching & Merging
```bash
git branch                # list branches (the * is where you are)
git branch <name>         # create a branch
git switch <name>         # move to a branch (modern)
git switch -c <name>      # create AND move to a new branch
git checkout <name>       # older way to switch
git merge <name>          # merge <name> INTO your current branch
git branch -d <name>      # delete a merged branch
```

## Remotes (connecting to GitHub)
```bash
git remote -v                       # see your linked remotes
git remote add origin <url>         # link your repo to a GitHub repo
git push -u origin main             # first push (sets the upstream)
git push                            # send commits to GitHub
git pull                            # get + merge changes from GitHub
git fetch                           # get changes WITHOUT merging yet
```

## Fixing Mistakes (your safety net)
```bash
git restore <file>            # discard unstaged changes to a file
git restore --staged <file>   # unstage a file (keep the changes)
git stash                     # shelve changes temporarily
git stash pop                 # bring shelved changes back
git commit --amend            # fix the LAST commit (message or content)
git reset --soft HEAD~1       # undo last commit, KEEP the changes staged
git reset --hard HEAD~1       # (careful) undo last commit AND delete the changes
git revert <commit>           # safely undo a commit by making a new one
git reflog                    # see EVERYTHING you've done (recover lost work)
```

> 🟢 Safe to use anytime: `restore`, `stash`, `revert`, `reflog`, `reset --soft`
> 🔴 Can delete work: `reset --hard`, `clean -fd`, `push --force` — pause and think first.

## Merge Conflicts
```bash
# When Git can't auto-merge, it marks the file like this:
<<<<<<< HEAD
your version
=======
their version
>>>>>>> other-branch
# Edit the file, delete the <<<, ===, >>> lines, keep what you want, then:
git add <file>
git commit            # finishes the merge
```

## Rebase (advanced — use carefully)
```bash
git rebase main       # replay your branch's commits on top of main
# GOLDEN RULE: never rebase commits you've already pushed/shared.
```

## Tags & Releases
```bash
git tag                       # list tags
git tag -a v1.0.0 -m "v1.0.0" # create an annotated tag (a version marker)
git push origin v1.0.0        # push a tag to GitHub
```

## Inspecting & Recovering
```bash
git log --oneline --graph --all   # visual history of all branches
git blame <file>                  # who changed each line, and when
git reflog                        # the undo-everything safety log
```

---

## GitHub Website Words (so they're not confusing)
- **Repository (repo):** a project folder on GitHub.
- **Fork:** your own copy of someone else's repo.
- **Pull Request (PR):** "please pull my changes into your project" — how you propose changes.
- **Issue:** a ticket to report a bug or suggest a feature.
- **Commit:** one saved snapshot of your work.
- **Branch:** a separate line of work, so you don't mess up `main`.
- **Merge:** combining one branch's work into another.

---

## The 5 commands you'll use 90% of the time
```bash
git status
git add .
git commit -m "message"
git push
git pull
```
Memorize these. The rest you can look up here.
