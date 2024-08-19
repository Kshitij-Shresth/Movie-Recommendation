app = Flask(__name__)

movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')
movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
movies.dropna(inplace=True)

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

def get_director(x):
    try:
        for i in ast.literal_eval(x):
            if i['job'] == 'Director':
                return i['name']
    except (ValueError, SyntaxError):
        return ''
    return ''
movies['director'] = movies['crew'].apply(get_director)
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['genres'] = movies['genres'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['keywords'] = movies['keywords'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['cast'] = movies['cast'].apply(lambda x: [i.replace(" ", "") for i in x])
movies['director'] = movies['director'].apply(lambda x: x.replace(" ", "") if isinstance(x, str) else '')
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['director'].apply(lambda x: [x])
movies['tags'] = movies['tags'].apply(lambda x: " ".join(x))

ps = PorterStemmer()
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

movies['tags'] = movies['tags'].apply(stem)
df = movies[['movie_id', 'title', 'tags']]

tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(df['tags']).toarray()
similarity = cosine_similarity(vectors)

def recommend(movie):
    if movie not in df['title'].values:
        return []

    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommendations = []
    for i in movie_list:
        recommendations.append(df.iloc[i[0]].title)
    return recommendations

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def get_recommendations():
    movie = request.form['movie']
    recommendations = recommend(movie)
    return render_template('index.html', movie=movie, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)

