barnowl-python
==============

This module is an example of using `Inline::Python` to run Python code
from BarnOwl.  It provides commands for evaluating Python expressions.

Installing
----------

To install the module, symlink or clone the repository into
`~/.owl/modules/Python/`. You should then be able to load the module
by typing `:reload-module Python` in BarnOwl.

Commands
--------

This module provides the following commands:

* `:python [args .. ]` - evaluate a Python expression
* `:ppython [args .. ]` - evaluate a Python expression and display in a popup window
* `:epython` - open the edit window for Python code
