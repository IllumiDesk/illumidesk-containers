#!/bin/bash

set -e

# no need to build and tag images for pull requests.
docker_login () {
    echo "Logging into DockerHub..."
    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
}

main () {
  echo "Build and push images..."
  tag_and_push
}

main