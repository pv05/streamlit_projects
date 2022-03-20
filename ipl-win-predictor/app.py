import pickle
import streamlit as st
import pandas as pd  
import urllib.request

teams = [
    'Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Rajasthan Royals',
    'Delhi Capitals'
]

cites = ['Hyderabad', 'Pune', 'Rajkot', 'Indore', 'Bangalore', 'Mumbai',
       'Kolkata', 'Delhi', 'Chandigarh', 'Kanpur', 'Jaipur', 'Chennai',
       'Cape Town', 'Port Elizabeth', 'Durban', 'Centurion',
       'East London', 'Johannesburg', 'Kimberley', 'Bloemfontein',
       'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala', 'Kochi',
       'Visakhapatnam', 'Raipur', 'Ranchi', 'Abu Dhabi', 'Sharjah',
       'Mohali', 'Bengaluru']

#pipe = pickle.load(open('pipe.pkl','rb'))
pipe = pickle.load(urllib.request.urlopen(("https://www.googleapis.com/drive/v3/files/10ml5J_qQBPimLu30WbxjXJ05oxqco2-g?alt=media&key=AIzaSyCUpIPtvM6lJw65WnZoM-Xxn7Xo6xytJ3k")))

st.title('IPl Win Predictor')

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team',sorted(teams))

with col2:
    bowling_team = st.selectbox('Select the bowling teams',sorted(teams))

selected_cites = st.selectbox('Select the hosted city',sorted(cites))

target = st.number_input('Target')

col3,col4,col4 = st.columns(3)
with col3:
    score = st.number_input('Score')

with col3:
    overs = st.number_input('Over completed')

with col3:
    wickets = st.number_input('wickets out')

if st.button('Predict Wining Probabity'):
    try:
        runs_left = target - score
        balls_left = 120 - (overs*6)
        wickets = 10 - wickets
        crr = score/overs
        rrr = (runs_left*6)/balls_left

        input_df = pd.DataFrame({
            'batting_team':[batting_team],
            'bowling_team':[bowling_team],
            'city':[selected_cites],
            'runs_left':[runs_left],
            'balls_left':[balls_left],
            'wickets_left':[wickets],
            'total_runs_x':[target],
            'crr':[crr],
            'rrr':[rrr],
        })

        result = pipe.predict_proba(input_df)
        loss = result[0][0]
        win = result[0][1]
        st.header(batting_team + " is - " + str(round(win*100)) + "%")
        st.header(bowling_team + " is - " + str(round(loss*100)) + "%")
        
    except:
        st.error('Opps Error!! Please make sure , you enterd right information')