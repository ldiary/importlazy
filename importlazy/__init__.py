from types import ModuleType
import sys
import importlib
import pprint


def initpkg(pkgname, exportdefs):
    oldmod = sys.modules.get(pkgname)
    attr = {
        '__file__': getattr(oldmod, '__file__', None),
        '__loader__': getattr(oldmod, '__loader__', None),
        '__path__': getattr(oldmod, '__path__', None),
        '__version__': getattr(oldmod, '__version__', None),
    }
    lazymodule = SleepingModule(pkgname, exportdefs,prefix=pkgname, attr=attr)
    sys.modules[pkgname] = lazymodule


def import_now(modpath, attrname):
    # print("Modpath: {}, attrname: {}".format(modpath, attrname))
    # Use import_module() instead of __import__(), https://docs.python.org/3.6/library/functions.html#__import__
    module = importlib.import_module(modpath)
    if not attrname:
        return module
    return getattr(module, attrname)


class SleepingModule(ModuleType):

    def __init__(self, name, sleepingroom, prefix=None, attr=None):
        # print("SM name: {}, sleepingroom: {}, prefix: {}, attr: {}".format(name, sleepingroom, prefix, attr))

        self.__name__ = name
        self.__prefix__ = prefix or name
        self.__map__ = {}


        if attr:
            for key, value in attr.items():
                setattr(self, key, value)

        # http://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems
        for key, value in sleepingroom.items():
            if isinstance(value, dict):
                # Nested sleeping modules
                submodname = "{}.{}".format(self.__name__, key)
                sleeping_module = SleepingModule(submodname, value, prefix)
                sys.modules[submodname] = sleeping_module
                setattr(self, key, sleeping_module)
            else:
                parts = value.split(":")
                modpath = parts.pop(0)

                if modpath[0] == '.':
                    modpath = prefix + modpath


                attrname = parts and parts[0] or ""
                self.__map__[key] = (modpath, attrname)

    def __repr__(self):
        return '<SleepingModule {}>'.format(self.__name__)

    def __makeattr(self, name):
        try:
            modpath, attrname = self.__map__[name]
        except KeyError:
            raise AttributeError(name)
        result = import_now(modpath, attrname)
        setattr(self, name, result)
        return result

    __getattr__ = __makeattr
