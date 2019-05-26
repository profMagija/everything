
class module:
    def __init__(self, mod):
        self.__mod = mod
        self.__import = None

    def __getattr__(self, name):
        
        try:
            return getattr(__import__(self.__mod + '.' + name), name)
        except ModuleNotFoundError:
            pass

        if not self.__import:
            self.__import = __import__(self.__mod)

        return getattr(self.__import, name)
            

    def __str__(self):
        return self.__getattr__('__str__')()

    def __repr__(self):
        return self.__getattr__('__repr__')()

def __getattr__(name):
    return module(name)

import sys
import os
from os.path import join, isdir, isfile

__all__ = []
__path__ = None

for p in sys.path:
    p = p or '.'
    if not isdir(p): 
        continue
    for l in os.listdir(p):
        if l.startswith('_'): 
            continue
        if (isfile(join(p, l)) and l.endswith('.py')):
            __all__.append(l[:-3])
        if (isdir(join(p, l)) and isfile(join(p, l, '__init__.py'))):
            __all__.append(l)