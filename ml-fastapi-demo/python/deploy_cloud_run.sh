#!/usr/bin/env sh

set -ex

REGION="asia-southeast1"
PROJECT="ultra-syntax-327916"
GCR_PROJECT="asia.gcr.io/ultra-syntax-327916"
MIN_INSTANCE=1
CPU=1.0
MEMORY="4Gi"
# type your service name
SERVICE_NAME="ml-fastapi-demo"

DOCKER_IMG="$GCR_PROJECT/$SERVICE_NAME"
echo "Build & push the docker image $DOCKER_IMG"

CR_SERVICE_NAME=$(echo "$SERVICE_NAME" | sed -e "s/\_//g")
#
echo "Deploy gcloud ...$CR_SERVICE_NAME"
gcloud run deploy $CR_SERVICE_NAME \
  --project "$PROJECT" \
  --image "$DOCKER_IMG" \
  --platform managed \
  --region $REGION \
  --cpu $CPU \
  --memory "$MEMORY" \
  --min-instances $MIN_INSTANCE \
  --allow-unauthenticated

SERVICE_URL=$( \
  gcloud run services describe "$CR_SERVICE_NAME" \
  --project "$PROJECT" \
  --platform managed \
  --region $REGION \
  --format "value(status.url)" \
)

echo SERVICE_URL
echo "Done"
