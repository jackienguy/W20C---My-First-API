import mariadb
from flask import Flask, request, Response
import json

app = Flask(__name__)

animals = ['Elephant', 'Hippo', 'Lion', 'Tiger']

@app.route('/animals', methods=['GET'])
def get_animal_list():
    if (request.method == 'GET'):
        return Response(
            json.dumps(animals),
            mimetype="application/json",
            status=200)

@app.route('/animals', methods=['POST'])      
def add_animal():
    if (request.method == 'POST'):
        animals.append('snake')   
        return Response(
            "Successfully added animal",
            mimetype="text/plain",
            status=200)

@app.route('/animals', methods=['PATCH'])
def edit_animal():
    if (request.method == 'PATCH'):
       animals[1] = 'Giant Hippo'

@app.route('/animals', methods=['DELETE'])
def delete_animal():
    if (request.method == 'DELETE'):
        for animal in animals:
            animals.remove('snake')
        return Response(
            "Successfully deleted animal",
            mimetype="text/plain",
            status=200)
    