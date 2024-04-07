from flask import Blueprint, render_template
from utils.fetchData import fetchData
from models.charactersModel import Character

main = Blueprint('home', __name__, template_folder='templates')

@main.route('/')
def home():
  character = Character(fetchData('https://rickandmortyapi.com/api/character/1'))
  name = character.getData()
  return render_template('index.html', name=name['name'])