import numpy as np 

def medal_tally(df):

    medal_tally = df.drop_duplicates(subset=['Year','Sport','Event','Medal','Team','NOC','City','Games'])

    medal_tally = medal_tally.groupby('region').sum()[['Gold','Bronze','Silver']].sort_values('Gold',ascending=False).reset_index()
    
    medal_tally['Gold'] = medal_tally['Gold'].astype('int')
    medal_tally['Bronze'] = medal_tally['Bronze'].astype('int')
    medal_tally['Silver'] = medal_tally['Silver'].astype('int')

    medal_tally['Total'] = medal_tally['Gold'] + medal_tally['Bronze'] + medal_tally['Silver']

    return medal_tally


def country_year_list(df):

    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0,'Overall')

    country = np.unique(df['region'].dropna().values).tolist() # we droped NAN values
    country.sort()
    country.insert(0,'Overall')

    return years,country

def fetch_medal_tally(df,years,country):
    medal_df = df.drop_duplicates(subset=['Year','Sport','Event','Medal','Team','NOC','City','Games'])
    
    flag = 0
    if years == 'Overall' and country == 'Overall':
        temp_df = medal_df # all data 
        
    if years == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[(medal_df['region'] == country)] # show specific country with all year data
    
    if years != 'Overall' and country == 'Overall':
        temp_df = medal_df[(medal_df['Year'] == int(years))] # show specific year with all country data
    
    if years != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == int(years)) & (medal_df['region'] == country)] # show specific year and country both data

    
    if flag == 1:
        a = temp_df.groupby('Year').sum()[['Gold','Bronze','Silver']].sort_values('Year').reset_index()
    else:
        a = temp_df.groupby('region').sum()[['Gold','Bronze','Silver']].sort_values('Gold',ascending=False).reset_index()
    

    a['Total'] = a['Gold'] + a['Bronze'] + a['Silver']
    a
    
    return a



def data_over_time(df,col):
    col_over_time = df.drop_duplicates(['Year',col])['Year'].value_counts().reset_index().sort_values('index')
    col_over_time.rename(columns={'index':'Editon','Year':f'No of {col}'},inplace=True)

    return col_over_time


def most_successful(df,sports):
    temp_df = df.dropna(subset=['Medal'])
    
    if sports == 'Overall':
        temp_df = temp_df['Name'].value_counts()[0:15].reset_index()
    else:
        temp_df = temp_df[temp_df['Sport'] == sports]['Name'].value_counts()[0:15].reset_index()
    
    x = temp_df.merge(df,left_on='index',right_on='Name').drop_duplicates('index')[['index','Name_x','Sport','region']]              
    x.rename(columns={'index':'Player','Name_x':'Medals'},inplace=True)

    x = x.reset_index(drop=True)
    x.index = x.index+1
    
    return x 


def year_wise_medaltally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(subset = ['Team','NOC','Games','City','Sport','Event','Medal','Year'])
    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()
    final_df.index = final_df.index+1 # for index start with 1

    return final_df

def country_event_heatmap(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df = temp_df.drop_duplicates(subset = ['Team','NOC','Games','City','Sport','Event','Medal','Year'])
    temp_df.groupby('Year').count()['Medal'].reset_index() # overall medals win
    new_df = temp_df[temp_df['region'] == country]
    new_df_pivot = new_df.pivot_table(index='Sport',columns='Year',values='Medal',aggfunc='count').fillna(0).astype('int16')

    return new_df_pivot

def most_successful_country(df,country):
    temp_df = df.dropna(subset=['Medal'])
    
    temp_df = temp_df[temp_df['region'] == country]['Name'].value_counts()[0:10].reset_index()
    
    x = temp_df.merge(df,left_on='index',right_on='Name')[['index','Name_x','Sport','region']].drop_duplicates('index')           
    x.rename(columns={'index':'Player','Name_x':'Medals'},inplace=True)
    x = x.reset_index(drop=True)
    x.index = x.index+1
                                                  
    return x 

def weight_vs_height(df,sports):
    athlete_df = df.drop_duplicates(subset=['Name','region'])
    athlete_df['Medal'].fillna('No Medal',inplace=True)
    temp_df = athlete_df[athlete_df['Medal'] != 'No Medal']

    if sports != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sports]

    return temp_df

def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name','region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women,on='Year',how='left')
    final.rename(columns={'Name_x':'Male','Name_y':'Female'},inplace=True)
    final.fillna(0,inplace=True)

    return final
