import pickle
import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()
api_key = os.getenv("TMDB_API_KEY")

# Streamlit page config
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("🎬 Movie Recommender System")
st.caption("Built with Machine Learning + Streamlit ❤️")

def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={api_key}&language=en-US"
    data = requests.get(url).json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies_name = []
    recommended_movies_poster = []
    for i in distances[1:11]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies_name.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies_name, recommended_movies_poster

# Load data
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))
similarity = pickle.load(open('artifacts/similarity.pkl', 'rb'))

# UI
movie_list = movies['title'].values
selected_movie = st.selectbox('Type or select a movie to get recommendation', movie_list)

if st.button('Show Recommendation'):
    recommended_movies_name, recommended_movies_poster = recommend(selected_movie)

    # Baris pertama: 5 film
    cols1 = st.columns(5)
    for i in range(5):
        with cols1[i]:
            st.markdown(
                f"""
                <div style="overflow-x:auto; white-space:nowrap; max-width:500px;">
                    {recommended_movies_name[i]}
                </div>
                """,
                unsafe_allow_html=True
            )
            st.image(recommended_movies_poster[i])

    # Baris kedua: 
    cols2 = st.columns(5)
    for i in range(5, 10):
        with cols2[i - 5]:
            st.markdown(
                f"""
                <div style="overflow-x:auto; white-space:nowrap; max-width:500px;">
                    {recommended_movies_name[i]}
                </div>
                """,
                unsafe_allow_html=True
            )
            st.image(recommended_movies_poster[i])
