from flask import Blueprint, render_template
from utils.createData import createCharacterData

main = Blueprint('characters', __name__, template_folder='templates')

@main.route('/')
def characters():
  characters = createCharacterData()
  return render_template('list.html', list=characters, path='Characters')

@main.route('/<string:id>')
def character(id):
  character = createCharacterData(id).getData()
  print(character)
  return render_template('detail.html', data=character)