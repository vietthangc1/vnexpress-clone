from flask import render_template, request
from bson.objectid import ObjectId
import pymongo
from . import create_app

app = create_app()
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