import os, re, sys
from numpy import get_include
from setuptools import setup, Extension

setup(name         = "packtree",
      version      = "0.0.1",
      author       = "Patricio Cubillos",
      author_email = "patricio.cubillos@oeaw.ac.at",
      url          = "https://github.com/pcubillos/packtree",
      packages     = ["packtree"],
      license      = ["MIT"],
      description  = "packtree makes ASCII tree representation of Python packages.",
      #scripts      = ['MCcubed/mccubed.py'],
      #entry_points={"console_scripts": ['foo = MCcubed.mccubed:main']},
      )
