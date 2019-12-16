# basic context manager framework
from contextlib import contextmanager

@contextmanager
def simple_context_manager(obj):
    try:
        # do something
        obj.some_property += 1
        yield
    finally:
        # wrap up
        obj.some_property -= 1


class Some_obj(object):
    def __init__(self, arg):
        self.some_property = arg


obj = Some_obj(5)
print(obj.some_property)

with simple_context_manager(obj):
    print(obj.some_property)

print(obj.some_property)
