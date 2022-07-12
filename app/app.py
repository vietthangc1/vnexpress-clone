from flask import Flask, render_template, request
from pymongo import MongoClient
import urllib
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb+srv://vietthangc1:"+urllib.parse.quote_plus('f2bdx@*-uLAZz!f')+"@cluster0.le7ea.mongodb.net/test")
app.db = client.vnexpress
articles = app.db.articles.find({})

@app.route("/", methods = ['GET', 'POST'])
def index():
  articles = app.db.articles.find({})
  if request.method == "POST":
    keyword = request.form.get("th_search")
    list_article = app.db.articles.find({"title": {"$in": keyword}})
    return render_template('index.html', th_articles = list_article)
  return render_template('index.html', th_articles = articles)

@app.route("/article/<id>")
def article(id):
  article = app.db.articles.find({"_id": ObjectId(id)})[0]
  return render_template("article.html", th_article = article)


if __name__ == '__main__':
  app.run(debug = True)