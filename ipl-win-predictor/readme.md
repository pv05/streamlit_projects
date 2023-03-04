# `IPL win predictor`

### Problem Statement :
The Indian Premier League (IPL) is a professional Twenty20 cricket league in India, which is one of the most popular and widely watched cricket leagues in the world. In this project, we aim to build a machine learning model using Logistic Regression algorithm to predict the win probability of the 2nd innings team based on the match data from previous IPL seasons.

### Description : 
In the game of cricket, predicting the outcome of a match is always a challenging task due to various factors such as team composition, pitch conditions, weather, and form of players. The IPL Win Predictor aims to solve this problem by predicting the win probability of the 2nd innings team using machine learning algorithms. The project uses data from previous IPL seasons to build the model, which can be used to predict the outcome of future matches.

### Data collection :
The dataset used in this project is collected from Kaggle and consists of two files, matches.csv and deliveries.csv. The matches.csv file contains information about each match such as the match ID, season year, venue, date of match, team1 name, team2 name, toss winner, toss decision, result of the match, winner team name, wins by runs and win by wickets. The deliveries.csv file contains information about each delivery such as the match ID, inning, batting team, bowling team, overs, balls, batsman name, non-striker player name, is super over or not, wide runs and many more columns.

### Data Preprocessing and Feature Engineering:
The first step in any machine learning project is data preprocessing and feature engineering. In this project, we cleaned the data by removing any missing or null values and dropping unnecessary columns. We then performed feature engineering by creating new columns such as the run rate, required run rate, and current run rate for each team at each point in the match. We also created binary variables to represent the teams batting first and second.

### Exploratory Data Analysis (EDA):
EDA is an important step to understand the data and identify patterns and trends. In this project, we visualized the data using various graphs and charts to understand the relationship between different variables. We analyzed factors such as the team that won the toss, the team that batted first, and the venue where the match was played.

### Machine Learning Model:
For this project, we used a Logistic Regression algorithm to build the machine learning model. We trained the model using the data from previous IPL seasons and achieved an accuracy of 80%. We also compared the results of the Logistic Regression algorithm with the Random Forest Classifier algorithm and found that the Logistic Regression algorithm gives better accuracy.

### Model Deployment:
We deployed the trained model on a Streamlit website, which allows users to enter the 2nd inning batting team , bowling team , match scores , over completed, city,target of match, wicket and predict the win probability of the 2nd innings team. The website is hosted for free, and anyone.

### Visit website :
[https://iplwin.streamlit.app](https://iplwin.streamlit.app/)

### Conclusion:
The IPL Win Predictor project aims to predict the win probability of the 2nd innings team in the game of cricket using machine learning algorithms. We used data from previous IPL seasons to build a Logistic Regression model and achieved an accuracy of 80%. The model is deployed on a Streamlit website, which is hosted for free, and anyone can access it to predict the outcome of future IPL matches.

