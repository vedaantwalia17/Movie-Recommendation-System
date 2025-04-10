# Movie-Recommendation-System
This project is a content-based movie recommendation system built using Python, Pandas, Scikit-learn, and Streamlit. It helps users discover similar movies based on genre, cast, crew, keywords and the movie overview.

### Features
- Cleans and transforms the TMDB dataset to extract relevant features like genres, cast, crew, keywords, and movie overview from a TMBD dataset taken from Kaggle.
- Cosine Similarity for recommending Top 5 similar movies.
- Streamlit Web Application for a cleaner and better user experience.

### Files
- tmdb_5000_credits.csv, tmdb_5000_movies.csv : Kaggle Datasets
- Data_Cleaning.py : Cleans and processes the datasets then saves data and similarity objects
- Movie_Recommendation_System.py : Streamlit Web Applications for Movie Recommendations
- data.pkl, similarity.pkl : Saved data and similarity objects
