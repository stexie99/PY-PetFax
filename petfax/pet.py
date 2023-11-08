from flask import ( Blueprint, render_template )
import json

bp = Blueprint('pet', __name__, url_prefix="/pets", static_folder='static')
pets = json.load(open('pets.json'))
print(pets)


@bp.route('/')
def index():
    return render_template('pets/index.html', pets=pets)

@bp.route('facts/<int:id>')
def show(id):
    pet= pets[id-1]
    return render_template('pets/show.html', pets=pet)

@bp.route('/new')
def new():
    return render_template('facts/new.html')