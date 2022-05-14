#!/bin/bash

# Build and push the image
echo "Build and push the image"
docker buildx build --platform=linux/amd64  -t asia.gcr.io/ultra-syntax-327916/ml-fastapi-demo -f ml-fastapi-demo/python/Dockerfile .
docker push asia.gcr.io/ultra-syntax-327916/ml-fastapi-demo

# cleaning up
echo "Cleaning up"