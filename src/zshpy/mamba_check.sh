#!/usr/bin/env sh
#
# AGPL-3.0 license
# Copyright (c) 2024 Asger Jon Vistisen
#

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

envPath="$1/environment.yml"

# Check for environment.yml in the given directory

if [ ! -f "$envPath" ]; then
  echo "No environment.yml found in $1. Skipping..."
  exit 2
fi
envName=$(grep 'name:' "$envPath" | cut -d ':' -f 2 | tr -d ' ')

if mamba env list | grep -q "^$envName"; then
    exit 0
fi

mamba env create -f "envPath"
    exit 0