from models.episodesModel import Episode
from models.charactersModel import Character
from models.locationsModel import Location
from utils.fetchData import fetchData

def createCharacterData(id = None):
  urlCharacters = 'https://rickandmortyapi.com/api/character/'
  
  if id == None:
    data = fetchData(urlCharacters)
    return data['results']
  
  data = Character(fetchData(urlCharacters + id))
  return data

def createLocationData(id = None):
  urlLocations = 'https://rickandmortyapi.com/api/location/'

  if id == None:
    data = fetchData(urlLocations)
    return data['results']

  data = Location(fetchData(urlLocations + id))
  return data

def createEpisodeData(id = None):
  urlEpisodes = 'https://rickandmortyapi.com/api/episode/'
  
  if id == None:
    data = fetchData(urlEpisodes)
    return data['results']
  
  data = Episode(fetchData(urlEpisodes + id))
  return data