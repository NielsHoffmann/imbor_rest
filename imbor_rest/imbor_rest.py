from flask import Flask, request, jsonify
from flasgger import Swagger
from flask_talisman import Talisman
from .sparql_queries import  ImnborOtl
import json

app = Flask(__name__)
#Talisman(app)

imborotl = ImnborOtl(
  #connection_data=json.load(open("~/Stuff/config.json"))
)

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



def get_auth(request):
  headers = request.headers
  auth = headers.get("X-Api-Key")
  if auth == 'asoidewfoef':
    return True
  else:
    return False


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
  if get_auth(request):
    q = """PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
            PREFIX groep: <http://linkeddata.crow.nl/imbor/def/groepering/>

          SELECT (?memberLabel as ?collecties)
          WHERE {
              groep:IMBORHierarchischeCollectie skos:member ?member .
              ?member skos:prefLabel ?memberLabel .
          } order by ?member"""
    res = imborotl.run_query(q)

    return jsonify([{
      res
    }]), 200
  else:
    return jsonify({"message": "ERROR: Unauthorized"}), 401

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
  q = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX groep: <http://linkeddata.crow.nl/publication-v2/ns/crow/imbor/def/groepering/>

    SELECT ?VakdisciplineURI ?VakdisciplineLabel
      WHERE {
        groep:IMBORVakdisciplineCollectie skos:member ?VakdisciplineURI .
        ?VakdisciplineURI skos:prefLabel ?VakdisciplineLabel .
      }
  """
  res = imborotl.run_query(q)
  print("result: " + str(res))
  #return jsonify([{
  #  res
  #}]), 200
  return res, 200

@app.route("/collectie/<string:naam>")
def get_todo(naam):

    return jsonify({ 'error': 'not implemented yet.' }), 400