import csv

dataDict = {}

with open('gamedatapy/dataset/amostra.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dataDict.update({row[0]: row[1:]})


class gameInfo:
    """Returns info about the specified game ID"""
    def __init__(self):
        pass
    def __str__(self):
        pass
    def name(self, gameId):
        return dataDict.get(gameId)[0]

class gameStats:
    """Returns statistics about the specified game ID"""
    pass

class generalInfo:
    """Returns info about the general sample"""
    pass

class generalStats:
    """Returns statistics about the general sample"""
    pass