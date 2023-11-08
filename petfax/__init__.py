from flask import Flask 
from flask_migrate import Migrate

def create_app(): 
    app = Flask(__name__)
    app.config['STATIC_URL_PATH'] = '/static'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False 

    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)

    @app.route('/')
    def hello(): 
        return 'Hello, PetFax!'

    from . import pet
    app.register_blueprint(pet.bp)
    
    return app
