import csv
import datetime

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
    def basicInfo(self, gameId):
        """Returns game name, release date, price and about"""
        return f'Name: {dataDict.get(f'{gameId}')[0]} \nRelease date: {dataDict.get(f'{gameId}')[1]} \nPrice: ${dataDict.get(f'{gameId}')[5]} \nAbout: {dataDict.get(f'{gameId}')[7]}'
    
    def name(self, gameId):
        """Returns the game name"""
        return dataDict.get(f'{gameId}')[0]
    
    def releaseDate(self, gameId):
        pass

    def price(self, gameId):
        pass

    
    

class gameStats:
    """Returns statistics about the specified game ID"""
    pass

class generalInfo:
    """Returns info about the general sample"""
    pass

class generalStats:
    """Returns statistics about the general sample"""
    pass
