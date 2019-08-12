
# Basic Commands
- `status` : git status
- `add file` : git add `<fileName>`
- `add all` : git add .
- `commit` : git commit -m "message"
- `push` : git push  `<REMOTENAME> <BRANCHNAME>`
- `init a repository` : git init
- `push existing new repo into remote`:
	- git remote add origin `<remote url>`
	- git push -u origin master
	
- `pull`: git pull origin `<branch>` [--allow-unrelated-histories]
- `renaming a repository` : https://help.github.com/en/articles/renaming-a-repository
- `branching` : 
    - `new branch`: git checkout -b `<childbranch> <parentbranch>`
    - `switch branch`: git checkbout `<branch name>`
- `remove file`: git rm [-f] `<fileName>`
- `stashing` : 
   - `stash without name` : git stash
   - `stash with name`: git stash push -m "name"
   - `apply` : git stash apply [index]
   - `see list` : git stash list
   - `delete`: git stash drop [index]
   - `apply before delete` : git stash pop [index]

- `merge` `<branch_from>` to `<branch_to>`
    - `Option #1`:
                    git checkout `<branch_to>`
                    git merge `<branch_from>`
    
    - `Option #2` : git merge `<branch_from>` `<branch_to>`

- `rebase`
    Consider the following scenario - 
    
    `master branch` : `commit1` - `commit2` - `commit3`
    
    `feature branch`:  `commit1` - `commit2` - `feature_commit1` - `feature_commit2`
    
    Now you want to update your `feature` branch with the `master` branch. So merging will     squash all the changes that `master` has into one commit and then commit that into feature     branch.
    
    If you want a linear commit history, then `rebase` is your friend by doing -
    ```
    git checkout feature // you are on feature branch
    git rebase master // perform rebase
    ```
    
    so your `feature` branch now will have the following commits -
    `commit1` - `commit2` - `commit3` - `feature_commit1` - `feature_commit2`
    
    **Do not perform rebase on public branch or on branches that other people may also be     working on**. why? - rebasing will create linear commit history on your local branch. then     if you push that, and other people do a merge, then both the merge commit and linear     commits because of your rebasing will be exactly same. It's unnecessary problems for     further tracking.
