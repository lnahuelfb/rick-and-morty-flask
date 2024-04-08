import requests as req
import json

def fetchData(link):
  res = req.get(link)
  response = json.loads(res.text)
  return response