# !/bin/bash

# Variables
SOURCE_REPO_URL="https://github.com/MovieLabs/Prodtech-OMC-Data-Model.git"
TARGET_REPO_URL="https://github.com/MovieLabs/test-OMC.git"

SOURCE_BRANCH="${1:-Dev-v2.6}"
TARGET_BRANCH="${2:-Prod-v2.6}"
COMMIT_MESSAGE="${3:-Updates for v2.6}"
END_TAG_NAME="${4:-tag-v2.6}"

# Clone the source repository
git clone $SOURCE_REPO_URL source-repo
cd source-repo
git checkout $SOURCE_BRANCH

# Add the remote for the target repository
git remote add source $SOURCE_REPO_URL
git remote add target $TARGET_REPO_URL

# Check if the target branch exists in the target repository
if git ls-remote --heads target $TARGET_BRANCH | grep $TARGET_BRANCH; then
  TARGET_BRANCH_EXISTS=true
else
  TARGET_BRANCH_EXISTS=false
fi

# If the target branch does not exist, initialize it
if [ "$TARGET_BRANCH_EXISTS" = false ]; then
  git checkout --orphan $TARGET_BRANCH
  git reset --hard
  git commit --allow-empty -m "Initialize branch $TARGET_BRANCH"
  git push target $TARGET_BRANCH
fi

# Fetch the target branch if it exists
if [ "$TARGET_BRANCH_EXISTS" = true ]; then
  git fetch target $TARGET_BRANCH:$TARGET_BRANCH
fi

# Switch to the target branch
git checkout $TARGET_BRANCH

# Handle deletions
# Identify files in the target branch that do not exist in the source branch
for file in $(git ls-tree -r --name-only HEAD); do
  if ! git ls-tree -r --name-only $SOURCE_BRANCH | grep -qx "$file"; then
    git rm "$file" # Stage deletions
  fi
done

# Bring over changes from the source branch
git checkout $SOURCE_BRANCH -- .
if [ -d ".github" ]; then
  rm -rf .github  # Remove the .github directory
fi
if [ -d "scripts" ]; then
  rm -rf scripts  # Remove the scripts directory
fi
git add .

# Commit the changes as a single commit
git commit -m "$COMMIT_MESSAGE"

# Push the changes to the target repository
git push target $TARGET_BRANCH

# Add the end tag name if provided
if [ -n "$END_TAG_NAME" ]; then
  # Tag the source branch in the source repository
  git tag -f $END_TAG_NAME
  git push source refs/tags/$END_TAG_NAME --force

  # Tag the target branch in the target repository
  git tag -f $END_TAG_NAME
  git push target refs/tags/$END_TAG_NAME --force
fi
