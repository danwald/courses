__all__ = ['register']

import functools
from inspect import signature

class __Registrar(dict):
    def unique_signature(self, func: callable) -> bool:
        func_name = f'{func.__name__}'
        _signature = f'{signature(func)}'
        signatures = self.get(func_name, set())
        if _signature in signatures:
            return False
        signatures.add(_signature)
        self[func_name] = signatures
        return True

__register = __Registrar()

def register(func):
    assert __register.unique_signature(func)
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__}')
        return func(*args, **kwargs)
    return wrapper
