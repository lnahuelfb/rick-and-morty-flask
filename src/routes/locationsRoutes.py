from flask import Blueprint, render_template
from models.locationsModel import Location
from utils.fetchData import createData, fetchData

main = Blueprint('locations', __name__, template_folder='templates')

@main.route('/')
def locations():
  locations = fetchData('https://rickandmortyapi.com/api/location')['results']
  return render_template('list.html', list=locations, path='Locations')

@main.route('/<string:id>')
def location(id):
  link = 'https://rickandmortyapi.com/api/location/' + id 
  location = createData(link, Location).getData()
  return render_template('detail.html', name=location['name'])