from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app,
  template= {
    "swagger": "3.0",
    "openapi": "3.0.0",
    "info": {
        "title": "imbor",
        "version": "0.0.1",
    },
    "components": {
      "schemas": {
        "Collecties": {
          "properties": {
            "naam": {
              "type": "string"
            }
          }
        },
        "Vakdisciplines": {
          "properties": {
            "naam": {
              "type": "string"
            }
          }
        }
      }
    }
  }
)

@app.route("/collecties")
def get_collections():
  """
  Get all collecties
  ---
  description: Get all collecties.
  tags:
    - collecties
  responses:
    200:
      description: List of all collecties.
      content:
        application/json:
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Collecties'

  """
  return jsonify([{
    'name': 'aap',
    'task': 'noot'
  }]), 200

@app.route("/vakdisciplines")
def get_vakdisciplines():
  """
  Get all valdisciplines
  ---
  description: Get all valdisciplines.
  tags:
    - collecties
  responses:
    200:
      description: List of all valdisciplines.
      content:
        application/json:
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Valdisciplines'

  """
  return jsonify([{
    'name': 'wegen',
    'task': 'groen'
  }]), 200

@app.route("/collectie/<string:naam>")
def get_todo(naam):

    return jsonify({ 'error': 'not implemented yet.' }), 400