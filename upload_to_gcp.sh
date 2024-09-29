#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Set variables
PROJECT_ID=""
REGION=""
REPOSITORY=""
IMAGE_NAME=""
IMAGE_TAG="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPOSITORY}/${IMAGE_NAME}:v1.0.0"

# Authenticate with GCP
echo "Authenticating with Google Cloud..."
gcloud auth login

# Set the project ID
echo "Setting project ID to ${PROJECT_ID}..."
gcloud config set project ${PROJECT_ID}

# Configure Docker to use the gcloud command-line tool as a credential helper
echo "Configuring Docker to use gcloud as a credential helper..."
gcloud auth configure-docker ${REGION}-docker.pkg.dev

# Submit the Docker image to Google Cloud Build
echo "Submitting the Docker image to GCP Artifact Registry..."
gcloud builds submit -t ${IMAGE_TAG} ./

echo "Docker image successfully uploaded to GCP Artifact Registry!"
