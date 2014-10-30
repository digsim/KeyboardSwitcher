# KeyboardSwitcher

Reassigns modifiers keys differently for different physical keyboars. When working with laptops and especially mac, the arrangement of the modifier keys is different for the latop keyboard the external white mac keyboard and standard keyboards. This scripts allows to reassign them so that they are consitent between different keyboards. The script does not change the layout (en,fr,de).

# Installation

from a terminal launch

sudo python setup.py install

this will compile and install the project to the pyhton libraries (eg. /usr/local/lib/python2.7/dist-packages/KeyboardSwitcher-1.1-py2.7.egg/). Furthermore it will install three scripts in /usr/local/bin/:
* keyboardswitcher
The configuration and logging.conf are copied into /etc/KeyboardSwitcher/ but it is possible to overwrite them either by placing a file with the same name (but prefixed with a dot eg. .logging.conf) in the user home directory or a file with the same name in the current working directory.

Different keyboards can be configured in the /etc/KeyboardSwitcher/keyboardswitcher.conf file. Actually there are already a few keyboards defined.
