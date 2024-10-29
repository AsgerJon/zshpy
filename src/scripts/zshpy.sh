#!/usr/bin/env sh
#
# AGPL-3.0 license
# Copyright (c) 2024 Asger Jon Vistisen
#

mambaCheck() {
if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory_path>"
  exit 1
fi

# Check for environment.yml in the given directory

if [ ! -f "$envPath" ]; then
  echo "No environment.yml found in $envPath. Skipping..."
  exit 2
fi
envName=$(grep 'name:' "$envPath" | cut -d ':' -f 2 | tr -d ' ')
if ! mamba env list | grep -q "^$envName"; then
    mamba env create -f "envPath"
    if ! mamba env list | grep -q "^$envName"; then
        echo "Failed to create environment $envName"
        return 1
    fi
fi
}
thisConda="/home/AsgerJon/miniforge3/bin/conda"
__conda_setup="$($thisConda 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/AsgerJon/miniforge3/etc/profile.d/conda.sh" ]; then
        . "/home/AsgerJon/miniforge3/etc/profile.d/conda.sh"
    else
        export PATH="/home/AsgerJon/miniforge3/bin:$PATH"
    fi
fi
unset __conda_setup

if [ -f "/home/AsgerJon/miniforge3/etc/profile.d/mamba.sh" ]; then
    . "/home/AsgerJon/miniforge3/etc/profile.d/mamba.sh"
fi
splitDot() {
  input="$1"  # Assign the first argument to a local variable

  # Use a case statement to check for a dot and split the string
  case "$input" in
    *.*)
      echo "${input%%.*}"  # Outputs everything before the first dot
      ;;
    *)
      echo "$input"  # Outputs the full input if no dot is present
      ;;
  esac
}
name=$(splitDot "$1")

scriptDir="$ZSHPY_CUSTOM/$name";
envPath="$scriptDir/environment.yml"


if ! mambaCheck "$scriptDir"; then
  exit 1
fi
# shellcheck disable=SC2034
mambaPy="$MAMBA_ENVS_PATH/$envName/bin/python";
# shellcheck disable=SC2034
mainFid="$scriptDir/main.py";

if [ ! -f "$mainFid" ]; then
  echo "No main.py found in $scriptDir. Skipping..."
  exit 2
fi

export PYTHONPATH="$scriptDir:PYTHONPATH";
export PYTHONPATH="$scriptDir/src:PYTHONPATH";
if "$mambaPy" "$mainFid" "$(pwd)" "$@"; then
  exit 1
fi

exit 0
