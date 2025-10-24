# Perform exploratory data analysis on the netflix_data.csv data to understand more about movies from the 1990s decade.
# What was the most frequent movie duration in the 1990s? Save an approximate answer as an integer called duration (use 1990 as the decade's start year).
# A movie is considered short if it is less than 90 minutes. Count the number of short action movies released in the 1990s and save this integer as short_movie_count.


# Importing pandasm matplotlib and numpy
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("/home/tk-lpt-648/my-work/Personal/Projects/python/00_datasets/netflix_data.csv")

# print(netflix_df)
shows_as_per_year = netflix_df['release_year']
shows_filter = np.logical_and(shows_as_per_year >= 1990, shows_as_per_year < 2000)
shows_in_1990_decade = netflix_df[shows_filter]
# print(shows_in_1990_decade)

shows_duration = shows_in_1990_decade['duration']

plt.hist(shows_duration)
plt.show()

duration = 109 # estimated duration hardcoded from histogram

short_shows_check = shows_in_1990_decade['duration'] < 90
short_shows = shows_in_1990_decade[short_shows_check]

short_movie_count = 0
for label, row in short_shows.iterrows():
    # instead of filtering duration on top, it could also be filtered here. In this case, instead of looping on short_shows, it will be on shows_in_1990_decade
    if row['type'] == 'Movie' and row['genre'] == 'Action':
        short_movie_count = short_movie_count + 1

print(short_movie_count)
