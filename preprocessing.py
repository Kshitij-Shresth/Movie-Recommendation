movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')
movies = movies.merge(credits, on = 'title')
#merging the two datasets on the basis of title
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)
#dropping unnecessary features that are of no use or skew the prediction 

def dlist(x):
    list_ = []
    try:
        for i in ast.literal_eval(x):
            list_.append(i['name'])
    except (ValueError, SyntaxError):
        return []
    return list_

movies['genres'] = movies['genres'].apply(dlist)
movies['keywords'] = movies['keywords'].apply(dlist)
movies['cast'] = movies['cast'].apply(dlist)
movies['crew'] = movies['crew'].apply(dlist)

#originally genres was in a dictionary format, we changed it to list     
def get_director(x):
    try:
        for i in ast.literal_eval(x):
            if i['job'] == 'Director':
                return i['name']
    except (ValueError, SyntaxError):
        return ''
    return ''
movies['director'] = movies['crew'].apply(get_director)
#extracting the directors name from crew
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['director'] = movies['director'].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else '')

movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['director'].apply(lambda x: [x])
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))
#Concantenating features after stemming and removing spaces
