#!/usr/bin/env python
# vim: set ts=2 sw=2 tw=99 et: 
import sys
from distutils.core import setup

scripts = [
  'scripts/ambuild'
]

if sys.platform == 'win32':
  scripts.append('scripts/ambuild.bat')

setup(
  name = 'AMBuild',
  version = '2.0',
  description = 'AlliedModders Build System',
  author = 'David Anderson',
  author_email = 'dvander@alliedmods.net',
  url = 'http://www.alliedmods.net/ambuild',
  packages = [
    'ambuild',
    'ambuild2',
    'ambuild2.frontend',
    'ambuild2.ipc',
    'ambuild2.frontend.amb2'
  ],
  scripts = scripts
)


