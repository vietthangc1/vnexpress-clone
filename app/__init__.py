from flask import Flask
from pymongo import MongoClient
import urllib

def create_app():
  app = Flask(__name__)
  client = MongoClient("mongodb+srv://vietthangc1:"+urllib.parse.quote_plus('f2bdx@*-uLAZz!f')+"@cluster0.le7ea.mongodb.net/test")
  app.db = client.vnexpress
  return app
