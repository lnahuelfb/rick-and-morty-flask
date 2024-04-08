from flask import Blueprint, render_template
from utils.createData import createEpisodeData

main = Blueprint('episodes', __name__, template_folder='templates')

@main.route('/')
def episodes():
  episodes = createEpisodeData()
  return render_template('list.html', list=episodes, path='Episodes')

@main.route('/<string:id>')
def episode(id):
  episode = createEpisodeData(id).getData()
  return render_template('detail.html', name=episode['name'])