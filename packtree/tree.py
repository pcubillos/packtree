# Copyright (c) 2016 Patricio Cubillos and contributors.
# packtree is open-source software under the MIT license (see LICENSE).

import os

def filetree(root, path="", exep=[".pyc", ".so"]):
  """
  Make an ASCII representation of the file in a folder (recursively).

  Parameters
  ----------
  root:  String
     Path to the folder to make the tree.
  path:  String
     String representing the path to current files.
  exep:  List of strings
     List of files extensions to ignore.

  Example
  -------
  >>> # Generate the ASCII tree representation of the directory that contains
  >>> # packtree (supposing you ARE at the folder that contains packtree):
  >>> import packtree as tree
  >>> tree.filetree(".")

  packtree
  |-- LICENSE
  |-- README.md
  |-- packtree
  |   |-- __init__.py
  |   `-- tree.py
  `-- setup.py
  """
  # Stop if this is not a folder:
  if not os.path.isdir(root):
    return

  # Print root name if this is the first call:
  if path == "":
    print("")
    print(os.path.realpath(root).split("/")[-1])

  # Get files in current folder:
  files = sorted(os.listdir(root))
  files = [item for item in files if (not item.startswith(".") and
                                      not os.path.splitext(item)[1] in exep)]
  nfiles = len(files)

  # Print the content of the current folder:
  newpath = path + "|   "
  arrow   = "|-- "
  for i in range(nfiles):
    if i == nfiles - 1:
      newpath = path + "    "
      arrow = "`-- "
    print("{:s}{:s}{:s}".format(path, arrow, files[i]))
    # Recursive call to print the content of sub-folders:
    filetree("{:s}/{:s}".format(root, files[i]), newpath, exep)


def packagetree(package, path=""):
  """
  Make an ASCII tree representation of the variables of a package.
  The tree will only consider the variables listed in the __all__
  variable of each package.

  Parameters
  ----------
  package: Python package
     Package of which to generate the tree.
  path: String
     String representing the path to current variables.

  Example
  -------

  >>> import packtree as tree
  >>> tree.packagetree(tree)
  packtree
  |-- filetree
  `-- packagetree
  """
  # Print the package name if this is the initial call:
  if path == "":
    print("")
    print(package.__name__)

  # Get branches of package:
  if hasattr(package, "__all__"):
    bran = package.__all__
  else:
    bran = []
  nbranches = len(bran)

  # Print the variables contained in the current package:
  newpath = path + "|   "
  arrow   = "|-- "
  for i in range(nbranches):
    if i == nbranches - 1:
      newpath = path + "    "
      arrow = "`-- "
    print("{:s}{:s}{:s}".format(path, arrow, bran[i]))
    # Recursive call to print the content of sub-packages:
    packagetree(package.__dict__[bran[i]], newpath)
