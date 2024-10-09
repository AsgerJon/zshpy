"""ShellScript wraps a shell script and provides a way to run it in a
subprocess."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from worktoy.base import BaseObject
from worktoy.text import monoSpace


class ShellScript(BaseObject):
  """ShellScript wraps a shell script and provides a way to run it in a
  subprocess."""

  @classmethod
  def _parse(cls, fid: str, **kwargs) -> str:
    """Check if the file exists"""
    if os.path.isabs(fid):
      if os.path.exists(fid):
        if os.path.isdir(fid):
          e = """Received: '%s' which points to a directory instead of a 
          file. """ % fid
          raise IsADirectoryError(monoSpace(e))
        return cls._load(fid)
      e = """Received: '%s' which does not exist. """ % fid
      raise FileNotFoundError(monoSpace(e))
    #  Check if the str is the contents of a script file by looking for a
    #  hashbang.
    if fid.startswith('#!'):
      return fid
    if kwargs.get('_recursion', False):
      raise RecursionError

  @classmethod
  def _load(cls, fid: str, **kwargs) -> str:
    """Load the contents of the file"""
