from nltk.stem.porter import PorterStemmer
cv = CountVectorizer(max_features = 5000, stop_words = 'english')
df['tags_str'] = df['tags'].apply(lambda x: ' '.join(x))
vectors = cv.fit_transform(df['tags_str']).toarray()
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()

def stem(text):
  y = []
  for i in text.split():
    y.append(ps.stem(i))

    a = "".join(y)
    return a
