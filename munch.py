from functools import wraps
from time import perf_counter

def munch(start, end):
    def do_munch(func):
        @wraps(func)
        def wrapper():
            result = func()
            result = f'{result[0:start]}' + f'{"x"*(end-start)}' + f'{result[end:]}'
            return result
        return wrapper
    return do_munch

@munch(1, 6)
def fibonacci():
    """
    Returns a text
    """
    return 'Fibonacci'

print(fibonacci())