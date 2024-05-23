import csv
import datetime

dataDict = {}

with open('gamedatapy/dataset/amostra.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        dataDict.update({row[0]: row[1:]})


class gameInfo:
    """Returns info about the specified game ID"""

    def basicInfo(gameId):
        """Returns game name, release date, price and about"""
        return f'Name: {dataDict.get(f'{gameId}')[0]} \nRelease date: {dataDict.get(f'{gameId}')[1]} \nPrice: ${dataDict.get(f'{gameId}')[5]} \nAbout: {dataDict.get(f'{gameId}')[7]}'
    
    def name(self, gameId):
        """Returns the game name"""
        return dataDict.get(f'{gameId}')[0]
    
    def releaseDate(gameId):
        """Returns the game's release date"""
        #use datetime format
        stringDate = str(dataDict.get(f'{gameId}')[1])
        listDate = stringDate.split(' ')
        year = int(listDate[2])
        day = int(listDate[1][:-1])
        if listDate[0] == 'Jan':
            month = 1
        elif listDate[0] == 'Feb':
            month = 2
        elif listDate[0] == 'Mar':
            month = 3
        elif listDate[0] == 'Apr':
            month = 4
        elif listDate[0] == 'May':
            month = 5
        elif listDate[0] == 'Jun':
            month = 6
        elif listDate[0] == 'Jul':
            month = 7
        elif listDate[0] == 'Aug':
            month = 8
        elif listDate[0] == 'Sep':
            month = 9
        elif listDate[0] == 'Oct':
            month = 10
        elif listDate[0] == 'Nov':
            month = 11
        elif listDate[0] == 'Dec':
            month = 12

        releaseDate = datetime.date(year, month, day)
        return releaseDate


    def reqAge(self, gameId):
        """Returns the required age to play the game"""
        #return int
        return int(dataDict.get(f'{gameId}')[4])

    def price(self, gameId):
        """Returns the game's price"""
        #return float
        return float(dataDict.get(f'{gameId}')[5])

    def about(self, gameId):
        """Returns the game's description"""
        return dataDict.get(f'{gameId}')[7]
        
    def languages(self, gameId):
        """Returns the game's supported and full audio languages"""
        return f'Supported languages: {dataDict.get(f'{gameId}')[8]} \nFull audio languages: {dataDict.get(f'{gameId}')[9]}'
    
    def reviews(self, gameId):
        """Returns the game reviews"""
        return dataDict.get(f'{gameId}')[10]

    def urls(self, gameId):
        """Returns urls for the game"""
        #12, 13, 14, 19
        pass

    def osSupport(self, gameId):
        """Returns which operating systems the game supports"""
        supported = []
        if dataDict.get(f'{gameId}')[15] == 'True':
            supported.append('Windows')
        if dataDict.get(f'{gameId}')[16] == 'True':
            supported.append('Mac')
        if dataDict.get(f'{gameId}')[17] == 'True':
            supported.append('Linux')

        return f'Supported OS: {supported}'

    def notes(self, gameId):
        """Returns extra notes for the game"""
        return dataDict.get(f'{gameId}')[26]

    def publishing(self, gameId):
        """Returns the game's developers and publishers"""
        return f'Developers: {dataDict.get(f'{gameId}')[31]} \nPublishers: {dataDict.get(f'{gameId}')[32]}'

    def classification(self, gameId):
        """Returns the game's categories, genres and tags"""
        return f'Categories: {dataDict.get(f'{gameId}')[33]} \nGenres: {dataDict.get(f'{gameId}')[34]} \nTags: {dataDict.get(f'{gameId}')[35]}'


class gameStats:
    """Returns statistics about the specified game ID"""
    def __init__(self):
        pass
    def __str__(self):
        pass
  
    pass


class generalInfo:
    """Returns info about the general sample"""
    
    def amount():
        """Returns the number of games in the sample"""
        return len(dataDict.keys()) 
    
    def freeGames():
        """Returns the amount of free games in the sample"""
        freeGames = 0
        for values in dataDict.values():
            if float(values[5]) == 0.0:
                freeGames += 1
        return freeGames
    
    def paidGames():
        """Returns the amount of paid games in the sample"""
        paidGames = 0
        for values in dataDict.values():
            if float(values[5]) != 0.0:
                paidGames += 1
        return paidGames
    
    def gameReleasesByYear():
        """Returns a dictionary with the number os games released each year"""
        releases = {}
        for value in dataDict.values():
            value = value[1]
            year = value[-4:]
            if year not in releases.keys():
                releases.update({year: 1})
            if year in releases.keys():
                newValue = releases.get(year) + 1
                releases.update({year: newValue})  
        
        return releases



class generalStats:
    """Returns statistics about the general sample"""
    pass
