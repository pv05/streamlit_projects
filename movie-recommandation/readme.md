# `MOVIE RECOMMANDATION SYSTEM`

### Problem Statement :
The aim of this project is to create a movie recommendation system using clustering and content-based approaches. The system will take a user-selected movie and recommend five other movies that are most similar in terms of their content. This project will use machine learning algorithms such as CountVectorizer, NLP, and cosine similarity to create a model that will make recommendations based on the movie's features such as genres, keywords, and overview. The dataset for this project is obtained from Kaggle and includes information such as budget, revenue, release date, and cast. The project will be implemented in Python, using tools such as TensorFlow, NumPy, Pandas, and Matplotlib. The final result will be a web application that is hosted for free and allows users to select a movie from a dropdown menu and receive recommendations for similar movies.

### Detailed Description:
The movie industry is constantly growing, and there are thousands of new movies released every year. However, it can be challenging to decide what to watch next, especially when you are not familiar with the movie titles. To solve this problem, we will create a movie recommendation system that will provide movie suggestions to users based on their preferences.
Our movie recommendation system will use a clustering and content-based approach to suggest similar movies to the one that the user has selected. We will use machine learning algorithms such as CountVectorizer, NLP, and cosine similarity to create a model that will make recommendations based on the movie's features such as genres, keywords, and overview.
### Data gathering  : 
The dataset for this project is obtained from Kaggle, and it includes information such as budget, revenue, release date, and cast. The main dataset is the tmdb_5000_movies.csv, which has columns such as budget, genres, homepage, movie id, keywords, original language, original title, overview, popularity, production companies, production countries, release date, revenue, runtime, spoken languages, status, tagline, title, vote_average, and vote_count. We will also use the tmdb_5000_credits.csv, which includes information about the cast and crew for each movie.
### Data Cleaning & Feature Engineering  :
The first step in this project is data cleaning, where we will remove any duplicate or irrelevant data. Next, we will perform feature engineering, where we will select the relevant features that will be used to train our model. 
### Model Development : 
We will then use machine learning algorithms such as CountVectorizer and cosine similarity to create a model that can make recommendations based on the selected features.
### Model Deployment :
Once the model is trained, we will save it in pickle format so that it can be used in our web application. We will create a streamlit website where users can select a movie from a dropdown menu and receive recommendations for similar movies. The website will be hosted for free so that anyone can use it.
### Conclusion :
In conclusion, our movie recommendation system using clustering and content-based approaches is a valuable tool for anyone looking for movie suggestions. By using machine learning algorithms and a well-curated dataset, we can provide accurate and personalized recommendations to users. With the creation of our streamlit website, we have made it easy and accessible for everyone to use our movie recommendation system.


### Visit website :
[https://movie.streamlit.app](https://movie.streamlit.app)