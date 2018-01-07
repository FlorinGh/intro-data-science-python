# -*- coding: utf-8 -*-
# Data Frame Data Structure
'''
Data Frames are 2D arrangements (tables with multiple columns)
to create them we first define dictionaries
all dictionaries must have the same indexes
each dictionary is line in the data frame
an index mst be defined as list if a custom index is needed
to look in the dataFrame use loc attribute as in the Series
'''

import pandas as pd

purchase_1 = pd.Series({'name':'Chris','item':'dog food','price':22.50})
purchase_2 = pd.Series({'name':'Kevin','item':'cat litter','price':12.30})
purchase_3 = pd.Series({'name':'Vinod','item':'bird seed','price':10.50})

df = pd.DataFrame([purchase_1,purchase_2,purchase_3],index=['store1','store1','store2'])
#print df.head()
#print df.loc['store2']
# an extracted line from the dataFrame is a series:
#print type(df.loc['store2'])

#print df.loc['store1']
#print df['item'] #  displays the column with this name
# an extracted column from the dataFrame is a series:
#print type(df['item'])

# the following two will return the same
# the first searches at the intersection of the two, line and column
#print df.loc['store2', 'price']
# the second extracts a series, the third line, then takes index 2
# keep in mind that the index will be in the new series and it's not the same in the 
# dataFrame
#print df.loc['store2'].iloc[2]

# if the index is used more than once, the resulted will a dataFrame also:
#print df.loc['store1']
#print type(df.loc['store1'])

# transposing the dataFrame
#print df.T.loc['item']

# take all the dataFrame and extract the following columns:
#print df.loc[:,['name', 'price']]

# copy the dataFrame an make some changes:
copy_df = df.copy()
# drop the values with index store1
#copy_df = copy_df.drop('store1')
#copy_df = copy_df.drop('name',1) # there is a parameter after the string
# by default this is 0, and the line is dropped
# if you want to drop a column, you have to set this to 1
#print copy_df

# to remove a column we can also use del
#del copy_df['item']
#print copy_df

# to create a new columns is as simple as assigning a new value
copy_df['location'] = None
#print copy_df

# changing all the values of a column
copy_df['price'] = 0.8*copy_df['price']
#copy_df['price'] *= 0.8
#print copy_df

# working on a series extracted from the dataFrame will affect the initial dataFrame:
#print df
prices = df['price']
prices += 5
#print prices
#print df
# in order to avoid this, used the copy() method

###############################################################################

add = 'D:/dataScience/introDataSciencePython/w2_dataProcessingPandas/'
data = pd.read_csv(add + 'olympics.csv', index_col=0, skiprows=1)
#print data.head()
#print data.columns

# clean up the header:
for col in data.columns:
    if col[:2] == '01':
        data.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2] == '02':
        data.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2] == '03':
        data.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1] == '№':
        data.rename(columns={col:'#'+col[4:]}, inplace=True)

#print data.head()

###############################################################################
# Boolean masking is a simple and easy way to filter
# a boolean mask is an array of true and false values
# using this array, the values that correspond to the true values are kept

# we create a mask by applying a condition of a parameter:
#print data['Gold'] > 2

# using the mask when now create the query dataFrame:
dataSummerGold = data.where(data['Gold']>0)
#print dataSummerGold['Gold'].count()
dataSummerGold = dataSummerGold.dropna(0)# 0 is default, don't need to use it
# using 0 will drop the lines with no data
# using 1 instead, will drop columns
#print dataSummerGold.head()

# another way to do this in only one line of code:
dataSummerGold2 = data[data['Gold']>0]
# this line filters out the row automatically
#print dataSummerGold2.head()

# masks can be combined to use a more complex filtering
# the result is also a boolean mask
# to combine mask we can use boolean operators

# how many counties have receive at least a gold medal in the Summer olympics?
#print len(data[data['Gold']>0])

# how many counties have receive at least a gold medal one of the olympics, S or W?
#print len(data[(data['Gold']>0) | (data['Gold.1']>0)])

# is there any country that won a gold medal in the winter but never in the summer?
#print len(data[(data['Gold']==0) & (data['Gold.1']>0)])
#print data[(data['Gold']==0) & (data['Gold.1']>0)]

### question:
# Write a query to return all of the names of the people who bought products worth
# more than $3.00
pur_1 = pd.Series({'Name': 'Chris','Item Purchased': 'Dog Food','Cost': 22.50})
pur_2 = pd.Series({'Name': 'Kevyn','Item Purchased': 'Kitty Litter','Cost': 2.50})
pur_3 = pd.Series({'Name': 'Vinod','Item Purchased': 'Bird Seed','Cost': 5.00})

# Ans1
df2 = pd.DataFrame([pur_1, pur_2, pur_3], index=['Store 1', 'Store 1', 'Store 2'])
dfCost3 = df2[df2['Cost'] > 3.00]
#print dfCost3['Name']
# Ans2
#print df2['Name'][df2['Cost']>3.0]

###############################################################################
# Set index function
# index the olimpics data by number of medals
# keep the names of the countries
data['Country'] = data.index
data = data.set_index('Gold')
data = data.reset_index()
#print data.head()

###############################################################################

# Multi indexing
census = pd.read_csv(add + 'census.csv')
#print census.head()
#print census['SUMLEV'].unique()

# US is divided as COUNTRY > STATE > County
# SUMLEV 40 is for values at state level
# SUMLEV 50 is for values at county level
# keep only the values for county:
census = census[census['SUMLEV']==50]
#print census.head()

# keep only total population estimates and total number of births
cols_to_keep = ['STNAME',
                'CTYNAME',
                'BIRTHS2010',
                'BIRTHS2011',
                'BIRTHS2012',
                'BIRTHS2013',
                'BIRTHS2014',
                'BIRTHS2015',
                'POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']
census = census[cols_to_keep]
#print census.head()

# Set a dual index
census = census.set_index(['STNAME','CTYNAME'])
#print census
#print census.loc['Michigan','Washtenaw County']
#print census.loc[[('Michigan','Washtenaw County'), ('Michigan','Wayne County')]]

###############################################################################
# question: using pd2 dataFrame above,
# Reindex the purchased records DataFrame to be indexed hierarchically, first by store
# then by person
# name this indexes 'Location' and 'Name'
# then add a new entry to it with the value of:
# 'Name':'Kevyn', 'Item Purchased':'Kitty Food', 'Cost':3.00, 'Location': 'Store 2'
df2['Location'] = df2.index
pur_4 = pd.Series({'Name':'Kevyn', 'Item Purchased':'Kitty Food', 'Cost':3.00, 'Location': 'Store 2'})
df2 = df2.append(pur_4, ignore_index=True)
df2 = df2.set_index(['Location', 'Name'])
print df2

'''
df = df.set_index([df.index, 'Name'])
df.index.names = ['Location', 'Name']
df = df.append(pd.Series(data={'Cost': 3.00, 'Item Purchased': 'Kitty Food'}, name=('Store 2', 'Kevyn')))
'''

###############################################################################
# Dealing with missing values
#data.fillna()
# sorting:
#df = df.set_index('time')
#df = df.sort_index()
#df = df.reset_index()
#df = df.set_index('time', 'user')










