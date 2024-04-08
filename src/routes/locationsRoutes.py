from flask import Blueprint, render_template
from utils.createData import createLocationData

main = Blueprint('locations', __name__, template_folder='templates')

@main.route('/')
def locations():
  locations = createLocationData()
  return render_template('list.html', list=locations, path='Locations')

@main.route('/<string:id>')
def location(id):
  location = createLocationData(id).getData()
  return render_template('detail.html', name=location['name'])