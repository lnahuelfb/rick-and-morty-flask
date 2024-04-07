from flask import Blueprint, render_template
from models.charactersModel import Character
from utils.fetchData import fetchData, createData

main = Blueprint('characters', __name__, template_folder='templates')

@main.route('/')
def characters():
  characters = fetchData('https://rickandmortyapi.com/api/character')['results']
  return render_template('list.html', list=characters, path='Characters')

@main.route('/<string:id>')
def character(id):
  link = 'https://rickandmortyapi.com/api/character/'+id
  character = createData(link, Character).getData()
  return render_template('detail.html', name=character['name'])