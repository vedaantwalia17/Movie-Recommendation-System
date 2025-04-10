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
    movie_index = data[data['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)),reverse=True,key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommended.append(data.iloc[i[0]].title)
    return recommended

#Streamlit Web Application
st.markdown("""
    <style>
    .stApp {
        background-color: #e0f2ff;
    }

    .custom-title {
        color: #003366;
        text-align: center;
        font-size: 2.5em;
        margin-bottom: 30px;
        font-weight: bold;
    }

    .custom-label {
        color: black;
        font-size: 1.3em;
        font-weight: bold;
        margin-bottom: -100px;
        margin-top: -15px;
        display: block;
    }
            
    .recommended {
        color: black;
        font-size: 1.1em;
        margin-top: 10px;
    }
            
    
    </style>
    """, unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="custom-box">', unsafe_allow_html=True)

    st.markdown('<div class="custom-title">🎬 Movie Recommendation System</div>', unsafe_allow_html=True)

    st.markdown('<label class="custom-label">Select your Movie:</label>', unsafe_allow_html=True)
    selected = st.selectbox('', data['title'].values) 

    # Button
    btn = st.button('Recommend')

    if btn:
        st.markdown('<hr style="margin-top: -15px; margin-bottom: 10px;">', unsafe_allow_html=True)
        st.markdown('<h3 style="color: black;">Recommended Movies</h3>', unsafe_allow_html=True)

        recommended_movies = recommend(selected)
        for movie in recommended_movies:
            st.markdown(f'<div class="recommended">{movie}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)