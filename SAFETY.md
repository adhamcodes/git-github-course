# Git Safety Rules

Git is powerful because it lets you rewrite or discard state. That also means some commands deserve a pause.

## Before destructive or history-rewriting work

Run:

```bash
git status
git diff
git diff --staged
git log --oneline --decorate -10
```

Ask:

1. Is the work committed?
2. Is the commit already pushed/shared?
3. Am I trying to undo content, undo history, or merely unstage something?
4. Do I know which branch I am on?

## Lower-risk recovery tools

These usually preserve history or uncommitted work when used correctly:

```bash
git restore --staged <file>   # unstage, keep working-tree edit
git stash                     # temporarily save tracked changes
git revert <commit>           # make a new commit that undoes an old commit
git reflog                    # inspect recent HEAD/reference movements
```

These are not magic. Read the command output and inspect afterward.

## Commands that can discard or rewrite work

Pause before using:

```bash
git restore <file>
git reset --hard <commit>
git clean -fd
git push --force
```

`git restore <file>` can permanently discard uncommitted edits. `reset --hard` can overwrite both the index and working tree. `clean -fd` removes untracked files/directories. Force-pushing can rewrite shared remote history.

## Safer recovery habit

If you find a commit in `git reflog` that you want to preserve, prefer creating a recovery branch first:

```bash
git switch -c recovery-branch <commit-hash>
```

Now the commit has a named branch pointing to it while you inspect what happened.

## Shared-history rule

Rewriting your own unpublished commits can be useful. Rewriting commits other people may already depend on requires coordination.

Do not use the simplistic rule "rebase is always dangerous." The real boundary is **shared history**.

## The recovery mindset

When something looks wrong:

1. Stop typing commands.
2. Run `git status`.
3. Inspect the graph: `git log --oneline --graph --decorate --all`.
4. Check `git reflog` if a commit seems missing.
5. Create a recovery branch before experimenting further.

Panic causes more damage than Git does.
