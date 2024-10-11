#!/usr/bin/env sh
#
# AGPL-3.0 license
# Copyright (c) 2024 Asger Jon Vistisen
#

if [ "$(id -u)" = "0" ]; then
  echo "This script should not be run as root. \
  Please remove 'sudo' from your command."
  exit 1
fi

DIR="$(cd "$(dirname "$0")" && pwd)"

# Path to the Python script
PYTHON_SCRIPT="$DIR/test.py"

# Check if the Python script exists
if [ ! -f "$PYTHON_SCRIPT" ]; then
  echo "Unable to locate file '$PYTHON_SCRIPT'."
  exit 10
fi

# Check if the Python script is executable
if [ ! -x "$PYTHON_SCRIPT" ]; then
  echo "The file '$PYTHON_SCRIPT' is not executable."
  exit 20
fi

# Run the Python script
python "$PYTHON_SCRIPT" "$@"
pythonExit=$?
echo "Testing arguments"
echo "$@"
echo "Testing complete"
if [ $pythonExit -ne 0 ]; then
  echo "Python script failed with exit code $pythonExit."
  exit 30
fi

exit 0