# Movie Recommender System
![image](https://github.com/user-attachments/assets/e68c86df-9281-4d2d-9c0b-e90077b3547c)

A Flask-based web application that recommends movies based on user input. The recommendation system is built using the TMDB dataset and employs TF-IDF vectorization and cosine similarity to find similar movies. The system uses natural language processing techniques to analyze the text features of movies and identify similarities.

## Features
### Movie Similarity: 
Recommends movies based on text similarity using TF-IDF and cosine similarity.

### Search Functionality:
Type in a movie title to get recommendations.

### Simple Web Interface:
Built with Flask and Jinja2 templates.

### Extensible Codebase:
Easily extendable for more complex recommendation algorithms.

## Installation

 ``` git clone https://github.com/your-username/movie-recommender-system.git```
```cd movie-recommender-system```
```python app.py```

## Dataset
The movie data is sourced from the TMDB dataset, which contains metadata for thousands of movies.

## How It Works

### Text Processing: 
The overview, genres, keywords, cast, and director of each movie are combined and processed into a single text feature.
### TF-IDF Vectorization: 
The text features are converted into numerical vectors using TF-IDF.
### Cosine Similarity: 
The system calculates the cosine similarity between movie vectors to find the most similar movies.
