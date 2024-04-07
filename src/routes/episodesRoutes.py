from flask import Blueprint, render_template
from models.episodesModel import Episode
from utils.fetchData import fetchData, createData

main = Blueprint('episodes', __name__, template_folder='templates')

@main.route('/')
def episodes():
  episodes = fetchData('https://rickandmortyapi.com/api/episode')['results']
  return render_template('list.html', list=episodes, path='Episodes')

@main.route('/<string:id>')
def episode(id):
  link = "https://rickandmortyapi.com/api/episode/" + id
  episode = createData(link, Episode).getData()
  return render_template('detail.html', name=episode['name'])