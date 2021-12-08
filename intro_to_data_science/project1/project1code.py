# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 15:21:49 2021

@author: jason
"""

import numpy as np
from scipy import stats

data = np.genfromtxt('movieReplicationSet.csv', delimiter = ',', skip_header = 1)
movie_data = data[:,0:400]

movie_median_data = np.zeros(400)
for i in range(400):
     movie_median_data[i] = np.median(movie_data[np.isfinite(movie_data[:,i]), i])

movies_isfinite = np.sum(np.isfinite(movie_data), axis = 0)

median_popularity = np.median(movies_isfinite)
less_popular_indices = np.where(movies_isfinite < median_popularity)
more_popular_indices = np.where(movies_isfinite > median_popularity)

less_popular_movie_medians = movie_median_data[less_popular_indices[0]]
more_popular_movie_medians = movie_median_data[more_popular_indices[0]]
u1, p1 = stats.mannwhitneyu(more_popular_movie_medians, less_popular_movie_medians, alternative = 'greater')

header = np.genfromtxt('movieReplicationSet.csv', delimiter = ',', dtype = str, max_rows = 1)
movie_header = header[0:400]
dates = np.zeros(len(movie_header))
for i, name in enumerate(movie_header):
    temp1 = name.split('(')
    temp2 = temp1[1].split(')')
    dates[i] = int(temp2[0])

median_date = np.median(dates)
older_indices = np.where(dates < median_date)
newer_indices = np.where(dates > median_date)

older_movie_medians = movie_median_data[older_indices[0]]
newer_movie_medians = movie_median_data[newer_indices[0]]
u2, p2 = stats.mannwhitneyu(older_movie_medians, newer_movie_medians)

shrek = movie_data[:,87]
gender = data[:,474]

shrek_mask = np.isfinite(shrek)
shrek = shrek[shrek_mask]
shrek_gender = gender[shrek_mask]

male_indices = np.where(shrek_gender == 2)
female_indices = np.where(shrek_gender == 1)
shrek_male_ratings = shrek[male_indices]
shrek_female_ratings = shrek[female_indices]
u3, p3 = stats.mannwhitneyu(shrek_male_ratings, shrek_female_ratings, alternative = 'two-sided')

q4_proportion = 0
for col in movie_data.T:
    temp_mask = np.isfinite(col)
    temp_col = col[temp_mask]
    temp_gender = gender[temp_mask]
    temp_male_indices = np.where(temp_gender == 2)
    temp_female_indices = np.where(temp_gender == 1)
    temp_col_male_ratings =  temp_col[temp_male_indices]
    temp_col_female_ratings =  temp_col[temp_female_indices]
    tempu4, tempp4 = stats.mannwhitneyu( temp_col_male_ratings, temp_col_female_ratings)
    if tempp4 < 0.005:
        q4_proportion += 1/np.shape(movie_data)[1]
        
lk = movie_data[:,220]
oc = data[:,475]

lk_mask = np.isfinite(lk)
lk = lk[lk_mask]
lk_oc = oc[lk_mask]

oc_indices = np.where(lk_oc == 1)
not_oc_indices = np.where(lk_oc == 0)
lk_oc_ratings = lk[oc_indices]
lk_not_oc_ratings = lk[not_oc_indices]
u5, p5 = stats.mannwhitneyu(lk_oc_ratings, lk_not_oc_ratings, alternative = 'greater')

q6_proportion = 0
for col in movie_data.T:
    temp_mask = np.isfinite(col)
    temp_col = col[temp_mask]
    temp_oc = oc[temp_mask]
    temp_oc_indices = np.where(temp_oc == 1)
    temp_not_oc_indices = np.where(temp_oc == 0)
    temp_col_oc_ratings =  temp_col[temp_oc_indices]
    temp_col_not_oc_ratings =  temp_col[temp_not_oc_indices]
    tempu6, tempp6 = stats.mannwhitneyu( temp_col_oc_ratings, temp_col_not_oc_ratings)
    if tempp6 < 0.005:
        q6_proportion += 1/np.shape(movie_data)[1]
        
wows = movie_data[:,357]
alone = data[:,476]

wows_mask = np.isfinite(wows)
wows = wows[wows_mask]
wows_alone = alone[wows_mask]

alone_indices = np.where(wows_alone == 1)
not_alone_indices = np.where(wows_alone == 0)
wows_alone_ratings = wows[alone_indices]
wows_not_alone_ratings = wows[not_alone_indices]
u7, p7 = stats.mannwhitneyu(wows_alone_ratings, wows_not_alone_ratings, alternative = 'less')

q8_proportion = 0
for col in movie_data.T:
    temp_mask = np.isfinite(col)
    temp_col = col[temp_mask]
    temp_alone = alone[temp_mask]
    temp_alone_indices = np.where(temp_alone == 1)
    temp_not_alone_indices = np.where(temp_alone == 0)
    temp_col_alone_ratings =  temp_col[temp_alone_indices]
    temp_col_not_alone_ratings =  temp_col[temp_not_alone_indices]
    tempu8, tempp8 = stats.mannwhitneyu(temp_col_alone_ratings, temp_col_not_alone_ratings, alternative = 'less')
    if tempp8 < 0.005:
        q8_proportion += 1/np.shape(movie_data)[1]
        
ha = movie_data[:,285]
fn = movie_data[:,138]
temp = np.array([np.isnan(ha),np.isnan(fn)],dtype=bool)
temp2 = temp*1
temp2 = sum(temp2)
missingData = np.where(temp2>0)
ha = np.delete(ha,missingData)
fn = np.delete(fn,missingData)
ks9, p9 = stats.wilcoxon(ha,fn)

h10 = np.zeros(8)
p10 = np.zeros(8)
for i, series in enumerate(['Star Wars', 'Harry Potter', 'The Matrix', 'Indiana Jones', 'Jurassic Park', 'Pirates of the Caribbean', 'Toy Story', 'Batman']):
    series_indices = np.where(np.char.find(header, series) != -1)
    series_data = movie_data[:,series_indices[0]]
    series_data = series_data[~np.isnan(series_data).any(axis=1)]
    h10[i],p10[i] = stats.friedmanchisquare(*series_data.T)
    print(np.shape(series_data)[0])
            
emotional = data[:,470]
q11_proportion = 0
emotional_names = np.array([])
for i, col in enumerate(movie_data.T):
    temp_mask = np.isfinite(col)
    temp_col = col[temp_mask]
    temp_emotional = emotional[temp_mask]
    temp_emotional_indices = np.where((temp_emotional == 6) | (temp_emotional == 5) | (temp_emotional == 4))
    temp_not_emotional_indices = np.where((temp_emotional == 1) | (temp_emotional == 2) | (temp_emotional == 3))
    temp_col_emotional_ratings =  temp_col[temp_emotional_indices]
    temp_col_not_emotional_ratings =  temp_col[temp_not_emotional_indices]
    tempu11, tempp11 = stats.mannwhitneyu(temp_col_emotional_ratings, temp_col_not_emotional_ratings, alternative = 'greater')
    if tempp11 < 0.005:
        q11_proportion += 1/np.shape(movie_data)[1]
        emotional_names = np.append(emotional_names,header[i])
    