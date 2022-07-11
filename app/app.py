import json
from flask import Flask, render_template, request
import uuid
from module import search, get_articles

app = Flask(__name__)

articles = get_articles()

for article in articles:
  article['_id'] = uuid.uuid4().hex

@app.route("/", methods = ['GET', 'POST'])
def index():
  if request.method == "POST":
    keyword = request.form.get("th_search")
    list_article = search(keyword, articles)
    return render_template('index.html', th_articles = list_article)
  return render_template('index.html', th_articles = articles)

@app.route("/article/<id>")
def article(id):
  article = {}
  for art in articles:
    if art['_id'] == id:
      article = art
      break
  return render_template("article.html", th_article = article)


if __name__ == '__main__':
  app.run(debug = True)