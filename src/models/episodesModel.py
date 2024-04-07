class Episode():
  def __init__(self, obj):
    self.id = obj['id']
    self.name = obj['name']
    self.air_date = obj['air_date']
    self.episode = obj['episode']
    self.characters = obj['characters']
    self.url = obj['url']
    self.created = obj['created']

  def getData(self):
    return {
      "id": self.id,
      "name": self.name,
      "air_date": self.air_date,
      "characters": self.characters,
      "episode": self.episode,
      "url": self.url,
      'created': self.created
    }

  def printData(self):
    print(
    'Name:', self.name, "\n"
    'air_date:', self.air_date, "\n"
    'episode:', self.episode, "\n"
    'characters:', self.characters, "\n"
    'url:', self.url, "\n"
    'created:', self.created, "\n"
    )
