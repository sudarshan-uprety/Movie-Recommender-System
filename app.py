import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=c5bc87518260a2911807fb0ab754193d&language=en-US".format(movie_id)
    data=requests.get(url)
    data=data.json()
    poster_path=data['poster_path']
    full_path="https:/image.tmdb.org/t/p/w500" + data['poster_path']
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in distances[1:6]:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

st.header('Movie Recommender System')
movies=pickle.load(open('movies.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movies_list=movies['title'].values
selected_movie=st.selectbox(
    'Type or select a movie from the dropdown',
    movies_list
)


if st.button("Recommend"):
    recommended_movies,recommended_movies_poster= recommend(selected_movie)

    col1, col2, col3, col4, col5 = st.beta_columns(5)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_poster[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_poster[1])

    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_poster[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_poster[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_poster[4])
