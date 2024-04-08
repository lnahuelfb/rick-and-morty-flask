from flask import Blueprint, render_template
from utils.createData import createCharacterData

main = Blueprint('home', __name__, template_folder='templates')

@main.route('/')
def home():
  character = createCharacterData()[0]['name']
  return render_template('index.html', name=character)