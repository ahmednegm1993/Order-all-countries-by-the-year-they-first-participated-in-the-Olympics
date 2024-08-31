import pandas as pd

df=pd.read_excel(r'E:\\Data_analysis_projects\\Order all countries by the year they first participated in the Olympics\\\dataset\\olympics_athletes_events_varied_years.xlsx')
df1=df.groupby('noc').agg({
    'year':'min'
})
print(df1.sort_values('year',ascending=True))