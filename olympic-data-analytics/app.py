import streamlit as st 
import pandas as pd 
import preprocessor,helper # own create module
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.figure_factory as ff


# for indian number format **** start ****
def formatINR(number):
    s, *d = str(number).partition(".")
    r = ",".join([s[x-2:x] for x in range(-3, -len(s), -2)][::-1] + [s[-3:]])
    return "".join([r] + d)
# for indian number format **** end ****

# hide setting button start
st.markdown(""" <style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style> """, unsafe_allow_html=True)
# hide setting button end

df = pd.read_csv('athlete_events.csv')
region_df = pd.read_csv('noc_regions.csv')

df = preprocessor.preprocess(df,region_df) # self create object our own module

st.sidebar.title('Olympics Games Analaysis')
st.sidebar.image(r'https://cdn.pixabay.com/photo/2016/08/20/17/58/olympic-games-1608127_960_720.png')

user_menu = st.sidebar.radio(
    'Select an Option',
    ('Medal Tally','Overall Analysis','Country-wise Analysis','Athlete-wise Analysis')
)

st.dataframe(df)

if user_menu == 'Medal Tally':

    st.sidebar.header('Medal Tally')

    years,country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox('Select Year',years)
    selected_country = st.sidebar.selectbox('Select Country',country)


    medal_tally = helper.fetch_medal_tally(df,selected_year,selected_country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title('Overall Olympic Data')
        st.dataframe(medal_tally) # for long data

    if selected_year != 'Overall' and selected_country == 'Overall':
       st.title(f'Olympic {selected_year} Data')
       st.dataframe(medal_tally) # for long data

    if selected_year == 'Overall' and selected_country != 'Overall':
       st.title(f'{selected_country} Olympic Data') 
       st.table(medal_tally)  # for short data

    if selected_year != 'Overall' and selected_country != 'Overall':
       st.title(f'{selected_country} Olympic {selected_year} Data')
       st.table(medal_tally) # for short data

if user_menu == 'Overall Analysis':
    editons=df['Year'].unique().shape[0]-1      # we done -1 coz, olympic commeti does not consider 1906 olympic coz, that year does not follow 4 year cycle
    cities=df['City'].unique().shape[0]
    sports=df['Sport'].unique().shape[0]
    events=df['Event'].unique().shape[0]
    athelets=df['Name'].unique().shape[0]
    nations=df['region'].unique().shape[0]

    st.title('Top Overall Statistics')

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Editons')
        st.title(editons)
    with col2:
        st.header('Hosts')
        st.title(cities)
    with col3:
        st.header('Sports')
        st.title(sports)

    col1,col2,col3 = st.columns(3)
    with col1:
        st.header('Events')
        st.title(events)
    with col2:
        st.header('Nations')
        st.title(nations)
    with col3:
        st.header('Athelets')
        # st.title(athelets)
        st.title(formatINR(athelets))

    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time, x="Editon", y="No of region",markers=True)
    st.title('Nations perform by year')    
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig = px.line(events_over_time, x="Editon", y="No of Event",markers=True)
    st.title('Events perform by year')
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df,'Name')
    fig = px.line(athlete_over_time, x="Editon", y="No of Name",markers=True)
    st.title("Athelete's perform by year")
    st.plotly_chart(fig)


    st.title('No of Events Over Time(Every Sports)')

    fig,ax = plt.subplots(figsize=(15,15))
    year_unique_sports = df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(year_unique_sports.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int16'),annot=True)
    st.pyplot(fig)


    st.title('Most Successfull Atheletes')
    sports_list = df['Sport'].unique().tolist()
    sports_list.sort()
    sports_list.insert(0,'Overall')
    selected_sports = st.selectbox('Select a Sports',sports_list)
    x = helper.most_successful(df,selected_sports)
    st.table(x)


if user_menu == 'Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')

    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country = st.sidebar.selectbox('Select a Country',country_list)

    country_df = helper.year_wise_medaltally(df,selected_country)
    fig = px.line(country_df, x="Year", y="Medal",markers=True)
    st.title(f"{selected_country}'s Medals over the year")
    st.plotly_chart(fig)

    
    st.title(f"{selected_country}'s Medals over the Sports and Year")
    country_ht_mp = helper.country_event_heatmap(df,selected_country)

    fig,ax = plt.subplots(figsize=(15,15))
    ax = sns.heatmap(country_ht_mp,annot=True)
    st.pyplot(fig)


    st.title(f"Top 10 Atheletes of {selected_country}")
    top10_df = helper.most_successful_country(df,selected_country)
    st.table(top10_df)


if user_menu == 'Athlete-wise Analysis':

    athlete_df = df.drop_duplicates(subset=['Name','region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal'] == 'Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal'] == 'Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal'] == 'Bronze']['Age'].dropna()

    fig = ff.create_distplot([x1,x2,x3,x4],['Age-distibution','Gold-distribution','Silver-distribution','Bronze-distribution'],show_hist=False,show_rug=False, colors=['green',' #C3CA01','#C0C0C0','#CD7F32'])           
    fig.update_layout(xaxis=dict(title="Athelete's Age"),yaxis=dict(title="Winning medal probability respect of age"),autosize=False,width=1000,height=600)

    st.title('Age Distibution Chart')
    st.plotly_chart(fig)



    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics', 'Swimming', 'Badminton', 'Sailing', 'Gymnastics', 'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling', 'Water Polo', 'Hockey', 'Rowing', 'Fencing', 'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing', 'Tennis', 'Golf', 'Softball', 'Archery', 'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball', 'Rhythmic Gymnastics', 'Rugby Sevens', 'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
    athlete_df = df.drop_duplicates(subset=['Name','region'])

    x = [] 
    name  = [] 
    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x,name,show_hist=False,show_rug=False)           
    fig.update_layout(xaxis=dict(title="Athelete's Age"),yaxis=dict(title="Winning GOLD probability wrt of age"),autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    st.title('Height Vs Weight Analysis of Athletes')
    sports_list = df['Sport'].unique().tolist()
    sports_list.sort()
    sports_list.insert(0,'Overall')
    selected_sports = st.selectbox('Select a Sports',sports_list)

    temp_df = helper.weight_vs_height(df,selected_sports)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(temp_df['Weight'],temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=40)
    st.pyplot(fig)


    st.title('Men vs Women Participation Over a year')
    final = helper.men_vs_women(df)
    fig = px.line(final,x = 'Year', y = ['Male','Female'],markers=True)
    fig.update_layout(xaxis=dict(title="Year"),yaxis=dict(title="Number of Players"),autosize=False, width=1000, height=600)
    st.plotly_chart(fig)



