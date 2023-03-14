from numpy.core.numeric import indices
import streamlit as st
import os
import pickle
from PIL import Image
import tensorflow
import numpy as np
from numpy.linalg import norm
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import GlobalMaxPooling2D
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input
from sklearn.neighbors import NearestNeighbors
import pandas as pd
import urllib.request
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

st.title('Fashion recommander system')
st.text('( It will take some time to open almost 2 minute beacause it based on deeplearning )')

#feature_list = np.array(pickle.load(open(r'C:\Users\91798\projetcs_deeplearning_based\fashion-product-images-small\embeddings_highRES.pkl', 'rb')))
#filenames = pickle.load(open(r'C:\Users\91798\projetcs_deeplearning_based\fashion-product-images-small\filenames_highRES.pkl', 'rb'))

feature_list = np.array(pickle.load(urllib.request.urlopen(r'https://www.googleapis.com/drive/v3/files/1n9yHjmIiUTmFZb8Cm-5cwKVrlMkquDkH?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k')))
filenames = pickle.load(urllib.request.urlopen(r'https://www.googleapis.com/drive/v3/files/1mdqfwxltwQpsNflTFmQdUic44uSWBX-Q?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k'))

model = ResNet50(weights='imagenet', include_top=False,
                 input_shape=(224, 224, 3))
model.trainable = False


model = tensorflow.keras.Sequential([
    model,
    GlobalMaxPooling2D()
])


def save_upploaded_file(uploaded_file):
    try:
        with open(os.path.join('uploads', uploaded_file.name), 'wb') as f:
            f.write(uploaded_file.getbuffer())
            return 1
    except:

        return 0


def feature_extraction(img_link, model):
    img = image.load_img(img_link, target_size=(224, 224))
    img_array = image.img_to_array(img)
    expanded_img_array = np.expand_dims(img_array, axis=0)
    preprocessed_img = preprocess_input(expanded_img_array)
    result = model.predict(preprocessed_img).flatten()
    normalized_result = result / norm(result)

    return normalized_result


def recommand(featrues, feature_list):
    neighbors = NearestNeighbors(
        n_neighbors=5, algorithm='brute', metric='euclidean')
    neighbors.fit(feature_list)
    distances, indices = neighbors.kneighbors([featrues])

    return indices


def display_with_link():
    recomand_jpg = []
    for i in indices[0]: 
        a = filenames[i]
        a = a.replace('/content/fashion-dataset/images/','')
        recomand_jpg.append(a)

    img_csv = pd.read_csv('final_df.csv')

    final_img = []
    final_product_name = []
    final_img_product_gender = []
    for i in recomand_jpg:
        a = img_csv[img_csv['filename'] == i]['link'].values[0]
        b = img_csv[img_csv['filename'] == i]['productDisplayName'].values[0]
        c = img_csv[img_csv['filename'] == i]['gender'].values[0]
        final_img.append(a)
        final_product_name.append(b)
        final_img_product_gender.append(c)
    
    return final_img,final_product_name,final_img_product_gender


uploaded_file = st.file_uploader('Choose an image',type=['jpg','png'])
with st.spinner('Please wait....AI is at work!!!'):
    if uploaded_file is not None:
        save_upploaded_file(uploaded_file)
        try:
            display_img = Image.open(uploaded_file)
            st.image(display_img, width=None)

            features = feature_extraction(os.path.join('uploads',uploaded_file.name), model)
            st.header('Recommanded Products')
            
            try:
                os.remove(os.path.join('uploads',uploaded_file.name))
            except FileNotFoundError:
                pass 

            indices = recommand(features, feature_list)

            final_img,final_product_name,final_img_product_gender = display_with_link()

            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                # st.image(filenames[indices[0][0]])
                st.write("For- "+final_img_product_gender[0])
                st.image(final_img[0])
                st.caption(final_product_name[0])
            with col2:
                # st.image(filenames[indices[0][1]])
                st.write("For- "+final_img_product_gender[1])
                st.image(final_img[1])
                st.caption(final_product_name[1])
            with col3:
                # st.image(filenames[indices[0][2]])
                st.write("For- "+final_img_product_gender[2])
                st.image(final_img[2])
                st.caption(final_product_name[2])
            with col4:
                # st.image(filenames[indices[0][3]])
                st.write("For- "+final_img_product_gender[3])
                st.image(final_img[3])
                st.caption(final_product_name[3])
            with col5:
                # st.image(filenames[indices[0][4]])
                st.write("For- "+final_img_product_gender[4])
                st.image(final_img[4])
                st.caption(final_product_name[4])
 
        except:
            os.remove(os.path.join('uploads',uploaded_file.name))
            st.header('Sorry!! File should be Image')
