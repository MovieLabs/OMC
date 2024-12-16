# Publish A Branch to Public Repository

This script synchronizes changes from a source branch in the current git repository to a target branch in a target git repository, applying all changes as a single commit to ensure a clean commit history.

## How It Works

* The script creates a temporary git repository by first cloning the source repository and then adding the target repository as a remote. 
* In this temporary repository, the script fetches the target branch from the target repository if one exists or creates a new branch if it does not exist.
* The script finds out files that no longer exist in the source branch but are present in the target branch. The script stages these deletions.
* The script dumps all changes from the source branch to the target branch and lets git CLI do the work by figuring out what has been added or changed.
* The script deletes the .github directory and the scripts directory to keep the public repository clean of internal script and workflow files.
* All these changes are staged and committed as a single commit using the user provided commit message. Commit is pushed to the target repository.
* The script tags the HEAD on the source branch as well as the HEAD (i.e., the pushed commit) on the target branch with the user provided tag name, ensuring traceability between the two repositories. Existing tags with the same name are updated.

## How To Use It

* Source and target repository URLs: **these URLs are hardcoded into the script. Change them to the correct values**.
* Source and target branch names: these branch names are passed as the first and second arguments to the script.
* Commit message: this message is passed as the third argument to the script.
* Tag name: this tag name is passed as the fourth argument to the script.

### On Unix:

```bash
chmod +x publish-branch.sh
./publish-branch.sh <source-branch> <target-branch> <commit-message> <tag-name>
# Example
./publish-branch.sh Dev-v2.6 Prod-v2.6 "Updates for v2.6" "tag-v2.6"
```

### On Windows:

```powershell
.\publish-branch.ps1 <source-branch> <target-branch> <commit-message> <tag-name>
```
