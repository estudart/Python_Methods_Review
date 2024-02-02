"""
List Comprehension

Nós podemos adicionar estruturas condicionais lógicas às nossas List Comprehension
"""

# Exemplos

# 1

numeros = [1, 2, 3, 4, 5, 6]

print([numero for numero in numeros if numero % 2 == 0])
print([numero for numero in numeros if numero % 2 != 0])

print([numero for numero in numeros if not numero % 2])
print([numero for numero in numeros if numero % 2])