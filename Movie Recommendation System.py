import pickle
import pandas as pd
import streamlit as st

#Loading the data
data = pickle.load(open('data.pkl',mode='rb'))
data = pd.DataFrame(data)

similarity = pickle.load(open('similarity.pkl',mode='rb'))

#Recommendation
def recommend(movie):
    recommended = []
    movie_index = data[data['title'] == movie].index(0)
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended.append(data.iloc[i[0]].title)
    return recommended

#Streamlit Web Application
st.title('Movie Recommendation System')
selected = st.selectbox('Select your Movie: ',data['title'].values)

btn = st.button('Recommend')

if btn:
    recommended_movies = recommend(selected)

    for i in recommended_movies:
        st.write(i)