import streamlit as st 
import pickle
import pandas as pd 
import requests
import urllib.request


def fetch_poster(movie_id):
    respose = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=88cacc33658425acdb11fa37422eb4e2&language=en-US'.format(movie_id)).json()
    return "https://image.tmdb.org/t/p/w500/" + respose['poster_path']

def recommand(movie):
    new_df = movies
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommand_movies= []
    recommanded_poster = []
    for i in movies_list:
        recommand_movies.append(new_df.iloc[i[0]].title)
        #fetch poster from TMDB API
        recommanded_poster.append(fetch_poster(new_df.iloc[i[0]].id))
        

    return recommand_movies,recommanded_poster

# similarity = pickle.load(open('similarity.pkl','rb'))
# movie_dict = pickle.load(open('movie_dict.pkl','rb'))

#we use google drive api for large file
movie_dict =  pickle.load(urllib.request.urlopen(("https://www.googleapis.com/drive/v3/files/1nJmfC1VBVTHM5bo6hsChVXazWpU8d8tN?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k")))
similarity =  pickle.load(urllib.request.urlopen(("https://www.googleapis.com/drive/v3/files/1PGoyJzpTSkosynS8Rg-X-wTGXXnIq7fH?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k")))


movies = pd.DataFrame(movie_dict)

github_repo_link = "https://github.com/pv05/streamlit_projects/blob/main/movie-recommandation/"
fulllink = f'[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)]({github_repo_link})'
st.title(f"Movie Recommandation System {fulllink}")

selected_movie = st.selectbox('Select Movie ',movies['title'].values)

if st.button('Recommand'):
    names,poster = recommand(selected_movie)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])
