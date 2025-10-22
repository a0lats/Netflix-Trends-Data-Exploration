#Author: Adeoluwa (Ade) Olateru-Olagbegi
#Project: Netflix Trends Data Exploration
#Date: 10/07/2025
#Description: this program analyzes netflix titles data to find top genres, release year trends, and leading production countries.
#it uses pandas for data wrangling and matplotlib for visualizing global content insights.

import pandas as pd
import matplotlib.pyplot as plt

#load dataset
data=pd.read_csv("netflix_titles.csv")

#preview first 5 rows
print(data.head())

#drop missing values for relevant columns
data=data.dropna(subset=['type','country','release_year','listed_in'])

#extract the first genre if multiple exist
data['main_genre']=data['listed_in'].apply(lambda x:x.split(',')[0])

#count top 10 genres
top_genres=data['main_genre'].value_counts().head(10)
print("top 10 genres:")
print(top_genres)

#plot top genres
top_genres.plot(kind='bar',title='top 10 genres on netflix',xlabel='genre',ylabel='number of titles')
plt.tight_layout()
plt.show()

#count number of releases per year
releases_per_year=data['release_year'].value_counts().sort_index()

#plot release trend
releases_per_year.plot(kind='line',marker='o',title='netflix releases per year',xlabel='year',ylabel='number of titles')
plt.grid(True)
plt.tight_layout()
plt.show()

#count top 5 countries producing content
top_countries=data['country'].value_counts().head(5)
print("top 5 producing countries:")
print(top_countries)

#plot top countries
top_countries.plot(kind='bar',title='top 5 countries by content production',xlabel='country',ylabel='number of titles')
plt.tight_layout()
plt.show()

#save summary
summary=pd.DataFrame({
    'top_genres':top_genres.index,
    'genre_count':top_genres.values
})
summary.to_csv("netflix_summary.csv",index=False)
print("summary report saved as netflix_summary.csv")

#test place
#you can test filters here, for example: show only movies released after 2018
recent_movies=data[(data['type']=='Movie')&(data['release_year']>2018)]
print("recent movies count:",len(recent_movies))