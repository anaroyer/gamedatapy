import csv
from gamedatapy.data import *

# Qual o percentual de jogos gratuitos e pagos na plataforma?
f'Jogos gratuitos: {(generalInfo.freeGames() / generalInfo.amount()) * 100}%'
f'Jogos pagos: {(generalInfo.paidGames() / generalInfo.amount()) * 100}%'

# Qual o ano com o maior número de novos jogos? Em caso de empate, retorne uma lista com os anos empatados.

releases = generalInfo.gameReleasesByYear()
mostReleases = []
for key, value in releases.items():
    most = max(releases.values())
    if value == most:
        mostReleases.append(key)
        
print(mostReleases)

# Quais jogos possuem a melhor pontuação no Metacritic versus quais jogos possuem a melhor pontuação na avaliação dos usuários?


