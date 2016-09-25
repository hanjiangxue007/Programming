#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author    : Bhishan Poudel
# Date      : May 23, 2016
# Ref       : http://www.gregreda.com/2013/10/26/working-with-pandas-dataframes/


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# pass in column names for each CSV
u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('ml-100k/u.user', sep='|', names=u_cols,
                    encoding='latin-1')

r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv('ml-100k/u.data', sep='\t', names=r_cols,
                      encoding='latin-1')

# the movies file contains columns indicating the movie's genres
# let's only load the first five columns of the file with usecols
m_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'imdb_url']
movies = pd.read_csv('ml-100k/u.item', sep='|', names=m_cols, usecols=range(5),
                     encoding='latin-1')

# get info
print('{} {} {} {}'.format('info', movies.info(),'','\n'))
print('{} {} {} {}'.format('movies datatype :\n', movies.dtypes,'','\n'))
print('{} {} {} {}'.format('users.describe() \n', users.describe(),'','\n'))
print('{} {} {} {}'.format('movies.head()\n', movies.head(3),'','\n'))
print('{} {} {} {}'.format('movies[20:22]\n', movies[20:22],'','\n'))


print('{} {} {} {}'.format('users[occupation].head()\n', users['occupation'].head(),'','\n'))

print(users[['age', 'zip_code']].head())
print('\n')

# can also store in a variable to use later
columns_you_want = ['occupation', 'sex']
print(users[columns_you_want].head())

# users older than 25
print(users[users.age > 25].head(3))
print('\n')

# users aged 40 AND male
print(users[(users.age == 40) & (users.sex == 'M')].head(3))
print('\n')

# users younger than 30 OR female
print(users[(users.sex == 'F') | (users.age < 30)].head(3))

print(users.set_index('user_id').head())
print('\n')

print(users.head())
print("\n^^^ I didn't actually change the DataFrame. ^^^\n")

with_new_index = users.set_index('user_id')
print(with_new_index.head())
print("\n^^^ set_index actually returns a new DataFrame. ^^^\n")

users.set_index('user_id', inplace=True)
print(users.head())

# Notice that we've lost the default pandas 0-based index and moved the
# user_id into its place. We can select rows by position using the iloc method.

print(users.iloc[99])
print('\n')
print(users.iloc[[1, 50, 300]])


# And we can select rows by label with the loc method.

print(users.loc[100])
print('\n')
print(users.loc[[2, 51, 301]])

# If we realize later that we liked the old pandas default index,
# we can just reset_index. The same rules for inplace apply.

users.reset_index(inplace=True)
print(users.head())
