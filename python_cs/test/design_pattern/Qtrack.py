import abc
import collections
import errno
import functools
import os
import sys

# def has_methods(*methods):
#     def decorator(Base):
#         def __subclasshook__(Class, Subclass):
#             if Class is Base:
#                 needed = set(methods)
#                 for Superclass in Subclass.__mro__:
#                     for meth in needed.copy():
#                         if meth in Superclass.__dict__:
#                             needed.discard(meth)
#                     if not needed:
#                         return True
#             return NotImplemented
#         Base.__subclasshook__ = classmethod(__subclasshook__)
#         return Base
#     return decorator

def has_methods(*methods):
    def decorator(Base):
        def __subclasshook__(Class, Subclass):
            if Class is Base:
                attributes = collections.ChainMap(*(Superclass.__dict__
                        for Superclass in Subclass.__mro__))
                if all(method in attributes for method in methods):
                    return True
            return NotImplemented
        Base.__subclasshook__ = classmethod(__subclasshook__)
        return Base
    return decorator

class Requirer(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook__(Class, Subclass):
        methods = set()
        for Superclass in Subclass.__mro__:
            if hasattr(Superclass, "required_methods"):
                methods |= set(Superclass.required_methods)
        attributes = collections.ChainMap(
            *(Superclass.__dict__ for Superclass in Class.__mro__)
        )
        if all(method in attributes for method in methods):
            return True
        return NotImplemented