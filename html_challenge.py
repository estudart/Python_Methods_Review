from functools import wraps

def bold(func):
    '''Bolds decorator function'''
    @wraps(func)
    def wrapper():
        '''return html bold tags'''
        #print(f'<b>{func()}</b>')
        return f'<b>{func()}</b>'
    return wrapper

def italic(func):
    '''Italics decorator function'''
    @wraps(func)
    def wrapper():
        '''return html italics tags'''
        #print(f'<i>{func()}</i>')
        return f'<i>{func()}</i>'
    return wrapper

@bold
@italic
def printFib():
    '''Prints a text'''
    return 'Fibonacci'

print(printFib())
