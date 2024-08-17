def recommend():
    movie = input("Enter a movie title: ")
    
    if movie not in df['title'].values:
        print("Movie not found in the dataset.")
        return
    
    movie_index = df[df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    print(f"Movies similar to '{movie}':")
    for i in movie_list:
        print(df.iloc[i[0]].title)
