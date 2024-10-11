"""ZshpyCustom provides a class representation of a custom zshpy script."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from worktoy.base import BaseObject
from worktoy.desc import CoreDescriptor, AttriBox, Field
from worktoy.text import typeMsg


class _CustomDirectory(CoreDescriptor):
  """_CustomDirectory provides a way to get the path to the custom directory
  for zshpy scripts."""

  def __set_name__(self, owner: type, name: str) -> None:
    CoreDescriptor.__set_name__(self, owner, name)
    zshpyCustomDirectory = os.environ.get('ZSHPY_CUSTOM', None)


class _CustomFile(CoreDescriptor):
  """_CustomFile provides a way to get the path to a custom zshpy script."""

  def __set_name__(self, owner: type, name: str) -> None:
    CoreDescriptor.__set_name__(self, owner, name)
    zshpyCustomFile = os.environ.get('ZSHPY_CUSTOM_FILE', None)


class ZshpyCustom(BaseObject):
  """ZshpyCustom provides a class representation of a custom zshpy script."""

  directory = _CustomDirectory()
  name = AttriBox[str]()
  fid = Field()

  def __init__(self, name: str) -> None:
    self.name = name

  @fid.GET
  def _getFid(self) -> str:
    """Getter-function for the full file path"""
    fileName = '%s.py' % self.name
    if isinstance(self.directory, str):
      fullPath = os.path.join(self.directory, fileName)
      return str(os.path.normpath(fullPath))
    e = typeMsg('directory', self.directory, str)
    raise TypeError(e)
