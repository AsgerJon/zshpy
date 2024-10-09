"""Main Tester Script"""
#  AGPL-3.0 license
#  Copyright (c) 2024 Asger Jon Vistisen
from __future__ import annotations

import os
import sys
import time
from typing import Callable

from icecream import ic
from pyperclip import copy

from moreworktoy import findEnvNames, testLOL
from yolo import yolo


def tester00() -> int:
  """Hello world"""
  stuff = [os, sys, ic, 'hello world!', ]
  for item in stuff:
    print(item)
  return 0


def tester01() -> int:
  """Testing find env names without regex"""
  torture_string = """
  $VALID_VAR $123INVALID $Another_Valid_One$Together $noSpace 
  $But$Next$OneValid 
  $Multiple$Concatenated$Vars $Single$Valid $123AND$INVALID_TOO 
  $_UnderscoreFirst $WITH_NUM123 $Symbols_Are$Here $Mixed_Case123 
  Surrounded$VarInText$With$Random$Characters $EdgeCase $Almost_$Valid 
  $WITH_SPACES $TRAILING_ $AtTheEnd $WITH123NUMBERS $A123B 
  and some tricky ones $WITH_MIXED_Case123andNumbers $ALL_CAPS 
  $small_lower $WITH_special$char_inside 
  """
  torture_names = findEnvNames(torture_string)
  expected_names = [
      "VALID_VAR",
      "Another_Valid_One",
      "Together",
      "noSpace",
      "But",
      "Next",
      "OneValid",
      "Multiple",
      "Concatenated",
      "Vars",
      "Single",
      "Valid",
      "INVALID_TOO",
      "_UnderscoreFirst",
      "WITH_NUM123",
      "Symbols_Are",
      "Here",
      "Mixed_Case123",
      "VarInText",
      "With",
      "Random",
      "Characters",
      "EdgeCase",
      "Almost_",
      "Valid",
      "WITH_SPACES",
      "TRAILING_",
      "AtTheEnd",
      "WITH123NUMBERS",
      "A123B",
      "WITH_MIXED_Case123andNumbers",
      "ALL_CAPS",
      "small_lower",
      "WITH_special",
      "char_inside"
  ]

  print('Found the following names:')
  print('_' * 50)
  for name in torture_names:
    if name not in expected_names:
      print('Unexpected name:', name)
      break
  else:
    for name in expected_names:
      if name not in torture_names:
        print('Expected name not found:', name)
        break
    else:
      print('All expected names found!')
  print('¨' * 50)
  return 0


def tester02() -> int:
  """Testing getNotice"""
  print(testLOL())
  return 0


def tester03() -> int:
  """Letters and their 'ord' values"""
  for letter in 'abcdefghijklmnopqrstuvwxyz':
    print(f'{letter} = {ord(letter)}')
  for letter in 'abcdefghijklmnopqrstuvwxyz'.upper():
    print(f'{letter} = {ord(letter)}')
  for letter in '0123456789':
    print(f'{letter} = {ord(letter)}')
  #  inverse of ord:
  for number in range(65, 91):
    print(f'{chr(number)} = {number}')
  for i in range(256):
    print('chr(%d): %s' % (i, chr(i)))
  return 0


if __name__ == '__main__':
  yolo(tester01)
