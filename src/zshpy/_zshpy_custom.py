"""ZshpyCustom provides a class representation of a custom zshpy script."""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os

from worktoy.base import BaseObject
from worktoy.desc import CoreDescriptor


class _CustomDirectory(CoreDescriptor):
  """_CustomDirectory provides a way to get the path to the custom directory
  for zshpy scripts."""

  def __set_name__(self, owner: type, name: str) -> None:
    CoreDescriptor.__set_name__(self, owner, name)
    zshpyCustomDirectory = os.environ.get('ZSHPY_CUSTOM', None)


class ZshpyCustom(BaseObject):
  """ZshpyCustom provides a class representation of a custom zshpy script."""
