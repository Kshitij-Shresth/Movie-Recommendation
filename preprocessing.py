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
#converting movies overview to list to make concantenation easier (we will be making a tags column)
movies['overview'] = movies['overview'].apply(lambda x:x.split())

#removing spaces is good for reccomender system, people with same first name might confuse the system

movies['genres'] = movies['genres'].apply(
    lambda x: [i.replace(" ", "") for i in x] if x else []
)

movies['keywords'] = movies['keywords'].apply(
    lambda x: [i.replace(" ", "") for i in x] if x else []
)

movies['cast'] = movies['cast'].apply(
    lambda x: [i.replace(" ", "") for i in x] if x else []
)

movies['crew'] = movies['crew'].apply(
    lambda x: [i.replace(" ", "") for i in x] if x else []
)

#creating tags column in a new dataframe
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

df = movies[['movie_id', 'title', 'tags']]
