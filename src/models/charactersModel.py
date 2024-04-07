class Character:
  def __init__(self, obj):
    self.id = obj['id']
    self.name = obj['name']
    self.status = obj['status']
    self.origin = obj['origin']
    self.location = obj['location']
    self.image = obj['image']
    self.episode = obj['episode'][0:2]
    self.url = obj['url']
    self.created = obj['created']
    
  def getData(self):
    return {
      "name": self.name,
      "status": self.status,
      "origin": self.origin,
      "location": self.location,
      "image": self.image,
      "episode": self.episode,
      "url": self.url,
      'created': self.created
    }
    
  def printData(self):
    print(
      "Name:" + self.name + "\n"
      "Status:", self.status, "\n"
      "Origin:", self.origin, "\n"
      "Location:", self.location, "\n"
      "Image:", self.image, "\n"
      "Episode:", self.episode, "\n"
      "URL:", self.url, "\n"
      "Created:", self.created, "\n"
      )