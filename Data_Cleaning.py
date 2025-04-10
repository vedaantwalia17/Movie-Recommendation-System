import ast
import pickle

import pandas as pd
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings('ignore')

#Importing the datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

#Merging the datasets
movies = movies.merge(credits,on = 'title')

#print(movies.columns)
'''
Index(['budget', 'genres', 'homepage', 'id', 'keywords', 'original_language',
       'original_title', 'overview', 'popularity', 'production_companies',
       'production_countries', 'release_date', 'revenue', 'runtime',
       'spoken_languages', 'status', 'tagline', 'title', 'vote_average',
       'vote_count', 'movie_id', 'cast', 'crew'],
      dtype='object')
'''


# Choosing Relevant features: movie_id, title, overview, genres, keywords,cast, crew
df = movies[['movie_id','title','overview','genres','keywords','cast','crew']]

#Fetching Relevant features
def fetch_genres_keywords(text):
    lst = ast.literal_eval(text)
    l = []
    for i in lst:
        l.append(i['name'])
    return l

df['genres'] = df['genres'].apply(fetch_genres_keywords)
df['keywords'] = df['keywords'].apply(fetch_genres_keywords)

def fetch_cast(text):
    lst = ast.literal_eval(text)
    l = []
    count = 0
    for i in lst:
        count += 1
        if count < 4:
            l.append(i['name'])
        else:
            break
    return l

df['cast'] = df['cast'].apply(fetch_cast)

def fetch_director(text):
    lst = ast.literal_eval(text)
    l = []
    for i in lst:
        if i['job'] == "Director":
            l.append(i['name'])
    return l

df['crew'] = df['crew'].apply(fetch_director)

#print(df.isnull().sum())
df.dropna(inplace=True)
#print(df.isnull().sum())

df['overview'] = df['overview'].apply(lambda x: x.split())


df['tags'] = df['overview'] + df['genres'] + df['keywords'] + df['cast'] + df['crew']


#Final Dataframe
data = df[['movie_id','title','tags']]
#Removing whitespaces from the tags
data['tags'] = data['tags'].apply(lambda x: [i.replace(' ','') for i in x])
#Converting back to string
data['tags'] = data['tags'].apply(lambda x: " ".join(x))

ps = PorterStemmer()

def text_preprocessing(text):
    new_text = []
    for i in text.split():
        lower = i.lower()
        new_text.append(ps.stem(lower))
    return " ".join(new_text)

data['tags'] = data['tags'].apply(text_preprocessing)

cv = CountVectorizer(max_features=5000,stop_words='english')

vectors = cv.fit_transform(data['tags']).toarray()
similarity = cosine_similarity(vectors)

pickle.dump(data.to_dict(),open('data.pkl',mode='wb'))
pickle.dump(similarity,open('similarity.pkl',mode='wb'))