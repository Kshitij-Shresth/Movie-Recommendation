cv = CountVectorizer(max_features = 5000, stop_words = 'english')
df['tags_str'] = df['tags'].apply(lambda x: ' '.join(x))
vectors = cv.fit_transform(df['tags_str']).toarray()
