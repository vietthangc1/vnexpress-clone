import json

def get_articles():
  f = open("./data/article.json", "r", encoding='utf-8')
  articles = json.load(f)
  f.close()
  return articles

def search(x, lst):
  if x == "":
    return lst
  list_filter = []
  for article in lst:
    if x.lower() in article['title'].lower():
      list_filter.append(article)
  return list_filter
  