# The Series Data Structure

'''
Series are 1D arrangements (tables with only one column)
the index are automaticaly integers, but we can alocat custom one

two ways to create series: using list and using dictionaries
if using lists, the indexes are auto, starting from 0
when using dictionaries, the index will be the dic indices

first column is the index column, also called labes
the second column is the values columnn
'''

import pandas as pd
import numpy as np

animals = ['tiger', 'shark', 'eagle']
animalSeries = pd.Series(animals)
#print animalSeries

numbers1 = [1, 3, 4, 90]
intSeries = pd.Series(numbers1)
#print intSeries

numbers2 = [1, 3, 4, None]
floatSeries = pd.Series(numbers2)
#print(floatSeries)

# None is not the same with numpy nan
#print np.nan == np.nan
#print np.nan == None
#print np.isnan(np.nan)
#print np.isnan(None) # not accepted as the type of None is unknown

sports = {'Archery':'Bhutan','Golf':'Scotland','Sumo':'Japan','Taekwondo':'South Korea'}
sportSeries = pd.Series(sports)
#print sportSeries
#print sportSeries.index

# we can also create custom index with two list, but the index must be indicated
# the index list mut be at the end of the call
# the lists must have the same dimension
ser1 = pd.Series(['Ro', 'Ca' ], index=['t1', 't2'])
#print ser1


# Querying a Series is done with loc and iloc attributes
# iloc will search the column; keep in mind that the list is indexed from 0
#print sportSeries
#print sportSeries.iloc[3] # search in the values column the value of index 3
#print sportSeries.loc['Golf'] # search un the labels and return the value of this label

#print sportSeries[3]  # will return the same as sportSeries.iloc[3]
# the code figures out that this would be iloc
#print sportSeries['Golf']  # will return same as sportSeries.loc['Golf']
## this should be avoided thouth as if we have 3 as index in a different location
## it will cause confusion: always use iloc and loc

# creating a new line is as simple as defining a value; this will be appended at the end
# series accepts all data types
p = pd.Series([1, 2, 3])
p.loc['animal'] = 'bears'
p.loc[2]=4 # the series values can also be changes
#print p
p.loc[3]=[2, 3] # this is an example of index called 3 at location 4
#calling p[3] will not return bears, from index 3, but the actual index location
#print p[3]
#print p.iloc[3]

s = pd.Series([100.0, 120.0, 101.0, 3.0])
#print s
total = np.sum(s)
#print total
# this is the fastest way to compute the sum of all components in a series

r = pd.Series(np.random.randint(0,1000,10000))
#print r.head() # will print only the first 5 values
#print len(r) # series length

r +=10 # add 10 to all values in series, faster than iterating all the series
#print r.head()

# Iterating in a series
for label, value in r.iteritems():
    r.loc[label] = value+10
    #r.set_value(label,value+10)
