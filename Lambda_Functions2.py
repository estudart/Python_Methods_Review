"""
Map

Com map, fazemos mapeamento de valores para função.


import math


def area(raio):
    '''Calcula a area de um circulo com raio 'r'.'''
    return format(math.pi * (raio ** 2), '.2f')


print(area(2))
print(area(5.3))

# Forma comum
raios = [2, 5, 7.1, 0.3, 10, 44]
areas = []

for r in raios:
    areas.append(area(r))

print(areas)

# Forma 2 - Map

# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável

areas = map(area, raios)

print(areas)
print(type(areas))
print(list(areas))

# Forma 3 - Map com Lambda
print(list(map(lambda raio: format(math.pi * (raio ** 2), '.2f'), raios)))

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27),
           ('Nova York', 28), ('Londres', 22)]

print(list(map(lambda x: (x[0], format(x[1] * (9/5) + 32, '.2f')), cidades)))
"""



