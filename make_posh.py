def make_posh(func):
    def wrapper():
        '''Making the posh'''
        print('+---------+' + "\n" + "|         |" + "\n" + func() + "\n" + "|         |" + "\n" + "+=========+")
        return func()
    return wrapper
 
@make_posh
def pfib():
    '''Print out Fibonacci'''
    return ' Fibonacci '

pfib()