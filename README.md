# packtree

packtree is a Python package that makes ASCII tree representation of a
package's varables or a folder's content.

## Table of Contents:
* [Author](#author)
* [Install and Compile](#install-and-compile)
* [Using packtree](#using-packtree)
* [Be Kind](#be-kind)
* [License](#license)


## Author:
* [Patricio Cubillos](https://github.com/pcubillos/),  Space Research Institute, Graz, Austria.  <patricio.cubillos@oeaw.ac.at>


## Install and Compile

### From pip
TBD

### From Github
Clone the repository to your local machine and install it:

Clone the repository to your working directory:  
```shell
git clone https://github.com/pcubillos/packtree
python ./setup.py install
```

Note that you may need to prepend `sudo` to the previous calls.


## Using packtree

The following demo shows what packtree produces.
First start a Python interpreter session:

```code
>>> import packtree as tree

>>> # Genereate the ASCII tree representation of the packtree package:
>>> tree.packagetree(tree)

packtree
|-- filetree
`-- packagetree


>>> # Generate the ASCII tree representation of the directory that contains the packtree package:
>>> tree.filetree(".")

packtree
|-- LICENSE
|-- README.md
|-- packtree
|   |-- __init__.py
|   `-- tree.py
`-- setup.py
```

## Be Kind:

Please, be kind and acknowledge and/or refer to the packtree site
([github.com/pcubillos/packtree](https://github.com/pcubillos/packtree))
if it was useful for you.


## License:

Copyright (c) 2016 Patricio Cubillos and contributors.
packtree is open-source software under the MIT license (see LICENSE).
