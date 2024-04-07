from utils.fetchData import fetchData

class Location():
  def __init__(self, obj):
    self.id = obj['id']
    self.name = obj['name']
    self.type = obj['type']
    self.dimension = obj['dimension']
    self.residents = obj['residents'][0:3]
    self.url = obj['url']
    self.created = obj['created']

  def getData(self):
    return {
      "id": self.id,
      "name": self.name,
      "type": self.type,
      "dimension": self.dimension,
      "residents": self.residents,
      "url": self.url,
      "created": self.created
    }
    
  def printData(self):
    print('Name:', self.name, "\n"
          'Type:', self.type, "\n"
          'Dimension:', self.dimension, "\n"
          'Residents:', self.residents, "\n"
          'URL:', self.url, "\n"
          'Created:', self.created)

