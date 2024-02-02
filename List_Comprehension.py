"""
List Comprehension

- Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro
iterável.

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero*10 for numero in numeros]
print(res)

Para entender melhor o que esta aconcetendo devemos dividir a experessão em duas partes, sendo elas:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

res = [numero/2 for numero in numeros]
print(res)


def funcao(valor):
    return valor * valor


res = [funcao(numero) for numero in numeros]

print(res)
"""

# Outros exemplos

# 1

nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([amigo[0].upper() + amigo[1:] for amigo in amigos])
