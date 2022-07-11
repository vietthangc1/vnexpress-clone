def search(x, lst):
  if x == "":
    return lst
  list_filter = []
  for article in lst:
    if x.lower() in article['title'].lower():
      list_filter.append(article)
  return list_filter
  