# Variables
$SOURCE_REPO_URL = "https://github.com/MovieLabs/Prodtech-OMC-Data-Model.git"
$TARGET_REPO_URL = "https://github.com/MovieLabs/test-OMC.git"

$SOURCE_BRANCH = $args[0] -or "Dev-v2.6"
$TARGET_BRANCH = $args[1] -or "Prod-v2.6"
$COMMIT_MESSAGE = $args[2] -or "Updates for v2.6"
$END_TAG_NAME = $args[3] -or "tag-v2.6"

# Clone the source repository
git clone $SOURCE_REPO_URL source-repo
Set-Location source-repo
git checkout $SOURCE_BRANCH

# Add the remote for the target repository
git remote add source $SOURCE_REPO_URL
git remote add target $TARGET_REPO_URL

# Check if the target branch exists in the target repository
$TARGET_BRANCH_EXISTS = git ls-remote --heads target $TARGET_BRANCH | Select-String -Pattern $TARGET_BRANCH

# If the target branch does not exist, initialize it
if (-not $TARGET_BRANCH_EXISTS) {
    git checkout --orphan $TARGET_BRANCH
    git reset --hard
    git commit --allow-empty -m "Initialize branch $TARGET_BRANCH"
    git push target $TARGET_BRANCH
}

# Fetch the target branch if it exists
if ($TARGET_BRANCH_EXISTS) {
    git fetch target $TARGET_BRANCH:$TARGET_BRANCH
}

# Switch to the target branch
git checkout $TARGET_BRANCH

# Handle deletions
# Identify files in the target branch that do not exist in the source branch
$files = git ls-tree -r --name-only HEAD
foreach ($file in $files) {
    if (-not (git ls-tree -r --name-only $SOURCE_BRANCH | Select-String -Pattern "^$file$")) {
        git rm $file # Stage deletions
    }
}

# Bring over changes from the source branch
git checkout $SOURCE_BRANCH -- .
if (Test-Path -Path .github) {
    Remove-Item -Recurse -Force .github  # Remove the .github directory
}
if (Test-Path -Path scripts) {
    Remove-Item -Recurse -Force scripts  # Remove the scripts directory
}
git add .

# Commit the changes as a single commit
git commit -m $COMMIT_MESSAGE

# Push the changes to the target repository
git push target $TARGET_BRANCH

# Add the end tag name if provided
if ($END_TAG_NAME) {
    # Tag the source branch in the source repository
    git tag -f $END_TAG_NAME
    git push source refs/tags/$END_TAG_NAME --force

    # Tag the target branch in the target repository
    git tag -f $END_TAG_NAME
    git push target refs/tags/$END_TAG_NAME --force
}