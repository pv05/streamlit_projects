# `Laptop Price Prediction`

### Introduction  : 

The goal of this machine learning project is to develop a Random Forest Regressor model to predict the price of a laptop based on its specifications. The project uses a dataset gathered from Kaggle, containing information such as laptop company name, laptop type, screen size, screen resolutions, CPU, RAM, ROM, GPU, operating system, weight, and price. The model has been developed using the Python programming language and various tools such as TensorFlow, NumPy, Pandas, and Matplotlib. The final model has been saved in the pickle format and deployed on a Streamlit website.

### Problem Statement : 
The objective of this project is to develop a machine learning model that can accurately predict the price of a laptop based on its specifications. This will be achieved by using a Random Forest Regressor algorithm on a dataset containing laptop specifications and prices. The final model will be deployed on a Streamlit website, allowing users to input laptop specifications and receive an estimated price.
Detailed Description : 
The laptop price prediction project involves several steps, which are detailed below.
### Data Gathering : 

The first step in the project was to gather a suitable dataset for training the machine learning model. The dataset was obtained from Kaggle and contained information such as laptop company name, laptop type, screen size, screen resolutions, CPU, RAM, ROM, GPU, operating system, weight, and price. The dataset was then imported into a Python environment using the Pandas library.

### Data Cleaning : 

After importing the dataset, the next step was to perform data cleaning. This involved identifying and handling missing or inconsistent values, as well as removing any irrelevant columns. The cleaned dataset was then used for further analysis.

### Feature Engineering : 

Feature engineering was performed on the dataset to transform the existing features and create new ones that would improve the accuracy of the model. This involved encoding categorical variables and creating new features such as screen density and storage type.

### Exploratory Data Analysis (EDA) : 

EDA was performed on the dataset to gain insights into the relationship between the different variables and the price of the laptop. This involved visualizing the data using various techniques such as scatter plots, histograms, and box plots.

### Model Development : 

Several regression algorithms were applied to the dataset, including Linear Regression, Ridge Regression, Lasso Regression, K-Neighbors Regressor, Decision Tree Regressor, Random Forest Regressor, Gradient Boosting Regressor, Ada Boost Regressor, Extra Trees Regressor, and Support Vector Regression. The Random Forest Regressor algorithm was selected as it provided the best accuracy of 88.73%.

### Model Deployment :

The final model was saved in the pickle format and deployed on a Streamlit website. The website allows users to input the laptop specifications, and the model predicts the price of the laptop.



### Conclusion : 

The laptop price prediction project demonstrates the use of machine learning algorithms to predict the price of a laptop based on its specifications. The Random Forest Regressor algorithm provides a high degree of accuracy, making it a suitable choice for this type of prediction problem. The final model has been deployed on a user-friendly Streamlit website, making it easily accessible to anyone who wishes to use it.

### Visit website :
[https://predictlaptop.streamlit.app](https://predictlaptop.streamlit.app)
