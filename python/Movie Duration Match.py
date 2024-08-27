import pandas as pd
df1=pd.read_excel(r'E:\\Data_analysis_projects\\New folder\dataset\\Movie_Duration_Match.xlsx',sheet_name='flight_schedule')
df2=pd.read_excel(r'E:\\Data_analysis_projects\\New folder\dataset\\Movie_Duration_Match.xlsx',sheet_name='entertainment_catalog')
df1_101 = df1[df1['flight_id'] == 101]['flight_duration'].reset_index(drop=True)
recommended_films = df2[df2['duration'] <= df1_101.values[0]][['movie_id', 'duration']]
recommended_films['flight_id']='101'
print(recommended_films)