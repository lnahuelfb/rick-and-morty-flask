from flask import Flask
from routes import charactersRoutes, episodesRoutes, locationsRoutes, homeRoutes, contactRoutes

app = Flask(__name__)

app.register_blueprint(homeRoutes.main, url_prefix='/')

app.register_blueprint(charactersRoutes.main, url_prefix='/characters')

app.register_blueprint(episodesRoutes.main, url_prefix='/episodes')

app.register_blueprint(locationsRoutes.main, url_prefix='/locations')

app.register_blueprint(contactRoutes.main, url_prefix='/contact')

if __name__ == '__main__':
  app.run()