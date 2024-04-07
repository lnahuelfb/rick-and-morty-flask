from flask import Blueprint, render_template

main = Blueprint('contact', __name__, template_folder='templates')

@main.route('/')
def contact():
  return render_template('contact.html', name='Contacto')