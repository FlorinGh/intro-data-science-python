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

print data.head()
