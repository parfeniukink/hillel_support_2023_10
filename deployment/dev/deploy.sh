#!/bin/bash

set -e

cd ~/hillel_support_2023_10
# git fetch origin --tags --force
git pull
docker compose build
docker compose down
docker compose up -d

echo "🚀 Successfully deployed