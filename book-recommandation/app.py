import streamlit as st 
import pickle
import pandas as pd 
import numpy as np
import urllib.request

# model = pickle.load(open('modelpkl.pkl','rb'))
# book_pivot = pickle.load(open('book_pivotpkl.pkl','rb'))
# final_img_url = pd.read_csv('final_img_url.csv')

model = pickle.load(urllib.request.urlopen('https://www.googleapis.com/drive/v3/files/1oE7rVB8Kw9Q1dT9aiLJ0ERiKt7WqSZ77?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k'))
book_pivot = pickle.load(urllib.request.urlopen('https://www.googleapis.com/drive/v3/files/1x7g-uMesHi-YwRINjhGkOgcEhhlK3W5-?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k'))

final_img_url = pd.read_csv('https://raw.githubusercontent.com/pv05/streamlit_projects/main/book-recommandation/final_img_url.csv')

github_repo_link = "https://github.com/pv05/project_ML/tree/main/Book-recommender-clustring-ContentBased"
fulllink = f'[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)]({github_repo_link})'
st.title(f"Book Recommandation System {fulllink}")

selected_book = st.selectbox('Select Book',sorted(final_img_url['title'].values))

def recommand_book1(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1,-1),n_neighbors=6)
    book_recommnd = []
    for i in suggestions[0]: # coz its 2d array [[like]]
#         if suggestions[0][0] != i:   # we don't want print 1st book coz it itself
        book_recommnd.append(book_pivot.index[i])
#     return book_recommnd
    
    book_name = []
    book_link = []
    for bookname in book_recommnd:
        if bookname != book_recommnd[0]: # we don't want print 1st book coz it itself
            book_name.append(bookname)
            book_link.append(final_img_url[final_img_url['title'] == bookname]['url'].values[0])

    return book_name,book_link



if st.button('Recommand'):
    st.header('Recommanded Suggestions')
    book,link = recommand_book1(selected_book)

    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        link[0] = link[0].replace('http://images.amazon.com/','https://m.media-amazon.com/')
        link[0] = link[0].replace('https://dummyimage.com/200x200/000000/fff.png&text=No+Image+Preview','https://dummyimage.com/305x500/000000/fff.png&text=Dummy+Image+Preview')

        st.text(book[0])
        st.image(link[0])
    with col2:
        link[1] = link[1].replace('http://images.amazon.com/','https://m.media-amazon.com/')
        link[1] = link[1].replace('https://dummyimage.com/200x200/000000/fff.png&text=No+Image+Preview','https://dummyimage.com/305x500/000000/fff.png&text=Dummy+Image+Preview')

        st.text(book[1]) 
        st.image(link[1])
    with col3:
        link[2] = link[2].replace('http://images.amazon.com/','https://m.media-amazon.com/')
        link[2] = link[2].replace('https://dummyimage.com/200x200/000000/fff.png&text=No+Image+Preview','https://dummyimage.com/305x500/000000/fff.png&text=Dummy+Image+Preview')

        st.text(book[2]) 
        st.image(link[2])
    with col4:
        link[3] = link[3].replace('http://images.amazon.com/','https://m.media-amazon.com/')
        link[3] = link[3].replace('https://dummyimage.com/200x200/000000/fff.png&text=No+Image+Preview','https://dummyimage.com/305x500/000000/fff.png&text=Dummy+Image+Preview')

        st.text(book[3]) 
        st.image(link[3])
    with col5:
        link[4] = link[4].replace('http://images.amazon.com/','https://m.media-amazon.com/')
        link[4] = link[4].replace('https://dummyimage.com/200x200/000000/fff.png&text=No+Image+Preview','https://dummyimage.com/305x500/000000/fff.png&text=No+Image+Preview')

        st.text(book[4]) 
        st.image(link[4])
