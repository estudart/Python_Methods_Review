"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função em Python

def funcao(x):
    return 3 * x + 1

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
print(nome_completo('  éRico', 'sTuDaRt'))

# Ex:

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

autores.sort(key=lambda autor: autor.split(' ')[-1].lower())
print(autores)
"""

