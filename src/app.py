"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User,Characters,Planets,Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def get_user():

    all_users = User.query.all()
    response_body = list(map(lambda x: x.serialize(), all_users))
    return jsonify(response_body), 200

@app.route('/user/<email_in>', methods=['GET'])
def get_ind_user(email_in):
    single_user = User.query.filter_by(email = email_in)
    response_body = list(map(lambda x: x.serialize(),single_user))
    return jsonify(response_body), 200

@app.route('/characters', methods=['GET'])

def get_all_character():
    all_characters = Characters.query.all()
    response_body = list(map(lambda x: x.serialize(), all_characters))
    return jsonify(response_body), 200

@app.route('/characters/<int:id>', methods=['GET'])
def get_ind_char(id):
    single_characters = Characters.query.get(id)
    response_body = single_characters.serialize()
    return jsonify(response_body), 200

@app.route('/planets', methods=['GET'])
def get_all_planets():
    all_planets = Planets.query.all()
    response_body = list(map(lambda x: x.serialize(), all_planets))
    return jsonify(response_body), 200

@app.route('/planets/<int:id>', methods=['GET'])
def get_single_planets(id):
    single_planets = Planets.query.get(id)
    response_body = single_planets.serialize()
    return jsonify(response_body), 200

@app.route('/favorites/<id>', methods=['GET'])
def get_user_favorites(id):
    user_favorites = Favorites.query.filter_by(user_id=id)
    response_body = list(map(lambda x: x.serialize(), user_favorites))
    return jsonify(response_body), 200

@app.route('/addfavorites', methods=['POST'])
def post_favs():
    request_body=request.json
    newfavoriteplanet = Favorites(user_id = request_body['user_id'] ,homeworld_id = request_body['homeworld_id'],char_name=request_body['char_Name'])
    db.session.add(newfavoriteplanet)
    db.session.commit()
    return jsonify(f"sucess"), 200

@app.route('/deletefavorite/<id>', methods=['DELETE'])
def delete_favs(id):
    persondelete = Favorites.query.get(id)
    db.session.delete(persondelete)
    db.session.commit()
    return jsonify(f"sucess"), 200

if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
