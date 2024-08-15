movies = movies.merge(credits, on = 'title')
#merging the two datasets on the basis of title
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
#dropping unnecessary features that are of no use or skew the prediction 
movies.dropna(inplace = True)
def dlist(x):
  list = []
  for i in ast.literal_eval(x):
    list.append(i['name'])
    return list
movies['genres']=movies['genres'].apply(dlist)
#originally genres was in a dictionary format, we changed it to list     
movies['keywords'] = movies['keywords'].apply(dlist)
movies['cast'] = movies['cast'].apply(dlist)
movies['crew'] = movies['crew'].apply(dlist)
