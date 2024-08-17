ps = PorterStemmer()
def stem(text):
    y = []
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)
movies['tags'] = movies['tags'].apply(stem)
#reducing words to their root form 

tfidf = TfidfVectorizer(max_features=5000, stop_words='english')
vectors = tfidf.fit_transform(movies['tags']).toarray()

similarity = cosine_similarity(vectors)
#Performing vectorization using TF-IDF
