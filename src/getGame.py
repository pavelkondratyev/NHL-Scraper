from lxml import html
import requests
import numpy as np


#AvailableSeason

#Gets url for a given game
#Takes season formatted as yearStart yearEnd concatenated
#Takes 4 digit game number
def getURL(season, gameNumber):
    url = "http://www.nhl.com/scores/htmlreports/"
    if season[0:4] != str(int(season[4:8]) - 1):
        raise ValueError('Incorrect season formatting')
    url += season
    url += "/PL02"
    if len(gameNumber) != 4:
        raise ValueError('Incorrect game number formatting')
    url += gameNumber
    url += ".HTM"
    return url

def getPreseasonURL(season, gameNumber):
    url = "http://www.nhl.com/scores/htmlreports/"
    if season[0:4] != str(int(season[4:8]) - 1):
        raise ValueError('Incorrect season formatting')
    url += season
    url += "/PL01"
    if len(gameNumber) != 4:
        raise ValueError('Incorrect game number formatting')
    url += gameNumber
    url += ".HTM"
    return url

#TODO
#Figure out what the pattern for playoff games is
def getPlayoffURL(season, gameNumber):
    url = "http://www.nhl.com/scores/htmlreports/"
    if season[0:4] != str(int(season[4:8]) - 1):
        raise ValueError('Incorrect season formatting')
    url += season
    url += "/PL03"
    if len(gameNumber) != 4:
        raise ValueError('Incorrect game number formatting')
    url += gameNumber
    url += ".HTM"
    return url

def getHTMLContent(url):
    page = requests.get(url)
    if page.status_code == 404:
        return None
    html_content = html.fromstring(page)
    return html_content

def getGame(season, gameNumber):
    url = getURL(season, gameNumber)
    page = requests.get(url)
    #Checks if URL points to a real game
    if page.status_code == 404:
        return None
    html_content = html.fromstring(page)
    return html_content

#returns an array of urls for games for the season
def getSeason(season):
    #TODO
    #Perform check for season
    gameURLs = []
    gameIterator = 1
    url = getURL(season, '%04d' % gameIterator)
    page = requests.get(url)
    #Instead of this make dictionary of how man games in a season
    while(page.status_code != 404):
        gameURLs.append(url)
        gameIterator += 1
        url = getURL(season, '%04d' % gameIterator)
        page = requests.get(url)
    return gameURLs
    
if __name__ == "__main__":
    print(getSeason('20162017'))
    print(getURL('20162017', '0156'))
    print(getURL('20172015', '01442'))
    print(getURL('20162017', '011115'))
