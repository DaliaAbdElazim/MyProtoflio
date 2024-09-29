#!/usr/bin/env bash

## Complete the following steps to get Docker running locally

# Set both the image name and version tag
VERSION="v1.0.0"
IMAGE_NAME=""

# Set Google Cloud project ID (ensure this is set correctly in your environment)
# Replace this with your actual project ID or ensure it's set as an environment variable
PROJECT_ID=""

# Step 1:
# Build image and add a descriptive tag with version
docker build -t gcr.io/$PROJECT_ID/$IMAGE_NAME:$VERSION .

# Step 2:
# List docker images
docker image ls

# Step 3:
# Run flask app with version tag
docker run -it -p 8080:8080 gcr.io/$PROJECT_ID/$IMAGE_NAME:$VERSION
