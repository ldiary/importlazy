import sys
import pathlib


def import_parent_folders(parent, subfolder=None):
    current = pathlib.Path.cwd()
    while current.name != parent:
        current = current.parent
    if subfolder:
        located_parent = str(pathlib.PurePath(current, subfolder))
    else:
        located_parent = str(current)
    sys.path.insert(0, located_parent)
    return current, located_parent

import_parent_folders('importlazy')


from importlazy import initpkg


initpkg(__name__, {
    'path': {
        'ClassOne': ".a_module:AModuleClassOne"
    }
})