from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

import json

with open('db.json') as json_file:
    dbrooms = json.load(json_file)

MAX_ITEMS = 15

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route("/districts")
@cross_origin()
def districts():
    return jsonify(["pechersky", "svytoshinsky", "desnyansky"])


@app.route("/rooms/<string:id>")
@cross_origin()
def rooms_by_district(id):
    filtered = [x for x in dbrooms if x['district'] == id]
    return jsonify(filtered[:MAX_ITEMS])


@app.route("/rooms")
@cross_origin()
def rooms():
    return jsonify(dbrooms[:MAX_ITEMS])
