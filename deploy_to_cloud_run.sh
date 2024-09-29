#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Set variables

# Project Related Variables
PROJECT_ID=""

# Cloud Storage Related Variables
BUCKET_NAME=""

# Cloud Run Related Variables
REGION=""
REPOSITORY=""
SERVICE_NAME=""
IMAGE_TAG="${REGION}-docker.pkg.dev/${PROJECT_ID}/$REPOSITORY}/${SERVICE_NAME}:v1.0.0"

# Cloud SQL Related Variables
CLOUD_SQL_CONNECTION_NAME=""
MYSQL_UNIX_SOCKET=''
MYSQL_USER=""
MYSQL_PASSWORD=""
MYSQL_DB=""
MYSQL_CURSORCLASS='DictCursor'

# Flask Related Variables
SECRET_KEY="\x15\xd5\xafG?\x1cc?\xbe\x9b\xa9\x84<z\x92E+\xcbGW\x18\xddv\xb2"

# Authenticate with GCP
echo "Authenticating with Google Cloud..."
gcloud auth login --no-launch-browser

# Set the project ID
echo "Setting project ID to ${PROJECT_ID}..."
gcloud config set project ${PROJECT_ID}

# Enable necessary services
echo "Enabling necessary Google Cloud services..."
gcloud services enable run.googleapis.com
gcloud services enable sqladmin.googleapis.com

# Deploy to Cloud Run
echo "Deploying the Docker image to Cloud Run..."
gcloud run deploy ${SERVICE_NAME} \
  --image ${IMAGE_TAG} \
  --region ${REGION} \
  --platform managed \
  --allow-unauthenticated \
  --add-cloudsql-instances ${CLOUD_SQL_CONNECTION_NAME} \
  --set-env-vars MYSQL_UNIX_SOCKET=${MYSQL_UNIX_SOCKET} \
  --set-env-vars MYSQL_USER=${MYSQL_USER} \
  --set-env-vars MYSQL_PASSWORD=${MYSQL_PASSWORD} \
  --set-env-vars MYSQL_DB=${MYSQL_DB} \
  --set-env-vars SECRET_KEY=${SECRET_KEY} \
  --set-env-vars JWT_SECRET_KEY=${JWT_SECRET_KEY} \
  --set-env-vars PROJECT_ID=${PROJECT_ID} \
  --set-env-vars BUCKET_NAME=${BUCKET_NAME}

echo "Service successfully deployed to Cloud Run!"
