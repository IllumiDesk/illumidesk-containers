#!/bin/bash

set -e

# no need to build and tag images for pull requests.
docker_login () {
  echo "${DOCKERHUB_TOKEN}" | docker login --username "${DOCKERHUB_USERNAME}" --password-stdin
}

tag_and_push () {
  if [ "${TRAVIS_PULL_REQUEST}" == "false" ]; then
    if [ "${TRAVIS_BRANCH}" == "main" ]; then
      export TAG="${TRAVIS_BUILD_NUMBER}"
      make build-all
      make push-all
      export TAG="latest"
      make build-all
      make push-all
    fi
  fi
}

main () {
  echo "Docker login"
  docker_login
  echo "Build and push images..."
  tag_and_push
}

main