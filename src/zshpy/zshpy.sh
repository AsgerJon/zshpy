#!/usr/bin/env sh
#
# AGPL-3.0 license
# Copyright (c) 2024 Asger Jon Vistisen
#

scriptDir="$ZSHPY_CUSTOM/$1";

if ! ./mamba_check.sh "$scriptDir"; then
  exit 1
fi
# shellcheck disable=SC2034
mambaPy="$MAMBA_ENVS_PATH/mamba/bin/python";
# shellcheck disable=SC2034
mainFid="$scriptDir/main.py";

if [ ! -f "$mainFid" ]; then
  echo "No main.py found in $scriptDir. Skipping..."
  exit 2
fi

if "$mambaPy" "$mainFid" "$@"; then
  exit 1
fi

exit 0
