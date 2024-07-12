import streamlit as st
import pickle
from dotenv import load_dotenv
import requests
import os
load_dotenv()
API_KEY=os.getenv('API_KEY')

st.title('Movie Recommendation System')
df=pickle.load(open('movie_list.pkl','rb'))
similarity=pickle.load(open('similarity_score.pkl','rb'))


def fetch_data(movie_id):
    url=f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response=requests.get(url)
    return "https://image.tmdb.org/t/p/original/"+response.json().get('poster_path')


def recommend_movie(movie_name):
    try:
        movie_index=df[df['title']==movie_name].index[0]
        distances=similarity[movie_index]
        movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
        recomendation_list=[]
        image=[]
        
        for movie in movies_list:
            recomendation_list.append(df.iloc[movie[0]].title)
            
            image.append(fetch_data(df.iloc[movie[0]].id))
        return recomendation_list,image
    except:
        print("Movie Not Found")



selected_movie = st.selectbox(
    "Select Your Favourite Movie:",
    (df['title']))



if st.button("Show Recommendation"):
    name,image=recommend_movie(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)

    
    with col1:
        st.image(image[0])
        st.write(name[0])

    with col2:
        st.image(image[1])
        st.write(name[1])

    with col3:
        st.image(image[2])
        st.write(name[2])
    with col4:
        st.image(image[3])
        st.write(name[3])
    with col5:
        st.image(image[4])
        st.write(name[4])
         
            
  
        
