"""
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatisticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a media dos dados utilizando a função mean()

media = statistics.mean(dados)
print(f'Média: {media}')

# Obs: Assim como a função map(), a filter() recebe dois parametros, sendo
# uma função e um iteravel.

res = filter(lambda x: x > media, dados)
print(list(res))

# OBS: Assim como na função map(), após serem utilizados os dados de filter(),
# eles são excluidos da memoria.

paises = ["", "Argentina", "", "Chile", "", "Colombia", "", "Equador", "", "", "Venezuela"]

print(list(filter(lambda x: x, paises)))
"""


