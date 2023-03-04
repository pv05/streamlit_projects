# `Book Recommandation System`

# <h1 style="text-align: center;">This is a heading</h1>

### Problem Statement
With the ever-increasing amount of information available online, it can be difficult for book enthusiasts to discover new books based on their interests. A personalized book recommendation system can solve this problem by suggesting books that match the user's preferences. However, developing such a system requires a large amount of data and advanced machine learning techniques.
The problem statement for this project is to develop a Book Recommendation System that can suggest five similar books based on a user's selected book. The system should use clustering and content-based techniques to provide personalized recommendations to users.

### Description

The Book Recommendation System is a Clustering-Content Based Project that uses the K-Nearest Neighbor (KNN) algorithm to provide book recommendations to users. The system is developed using Python programming language and various libraries such as TensorFlow, NumPy, Pandas, and Matplotlib.

### Data collection
The project is divided into several stages, starting with data collection from Kaggle.com. The dataset contains information about books such as their rating, title, author, year of publishing, publisher name, and number of ratings. 

### Data Preprocessing & Feature engineering 
The data is then preprocessed by performing feature engineering techniques and cleaning the data to remove any irrelevant or incomplete information.

### Exploratory Data Analysis (EDA)
the system performs Exploratory Data Analysis (EDA) to gain insights into the data and identify any patterns or trends. This step is crucial for understanding the data and selecting the appropriate features for clustering and content-based techniques.

### Machine Learning Model apply
the KNN algorithm is applied to build the recommendation system. The algorithm works by finding the K-nearest neighbors of a given book and recommending books that are similar to it. The system uses a combination of clustering and content-based techniques to provide personalized recommendations to users.

### Model Deployment
Once the model is built, it is saved in pickle format. A Streamlit website is then created where users can enter the name of a book, and the model will recommend five similar books. The website is hosted for free and can be accessed by anyone.
 
### Visit website
[http://bookrecommad.streamlit.app](https://bookrecommand.streamlit.app)