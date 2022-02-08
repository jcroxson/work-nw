# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:56:52 2019

@author: JCroxson
"""

#Python 3 Do the WHOLE thing with pandas
import pandas as pd #import pandas

#read in existing file and new file. Pandas can achieve this with its workhorse read_csv() call. Calling out the header row can be an important
#piece of the puzzle for us.
t1 = pd.read_csv('old.csv', encoding = 'utf-8')
t2 = pd.read_csv('new.csv', encoding = 'utf-8')

#this will reorder columns to match the existing 'old.csv', which is a proxy for the MI File
t2 = t2[t1.columns]
#This code will show the difference
t3 = pd.concat([t1, t2]).loc[t2.index.symmetric_difference(t1.index)]
#t3 = t2.merge(t1, how = 'inner' , sort = False, indicator=False)#.loc[lambda x : x['_merge']=='left_only']

"""
This is where we will need to run the ML algorithm to recode the t3 df with our coding
"""

#concatenate the two files by row
t4 = pd.concat([t1, t3], axis = 0)

#want to add a column that indicates of it's a new entry (Type = New, Old)
#ADDED SOME COMMENTS
#drop duplicate values while retaining the first file
#DataFrame.drop_duplicates(self, subset=None, keep='first', inplace=False)
#(columns to use, keep first, last, or drop all duplicates, drop dulicates in place or return copies)
#t3.drop_duplicates(keep = 'first', inplace = True)
#safety measure to reset the index
#t3.reset_index(drop = True, inplace = True)

#write final to new master file
t4.to_csv('master.csv', encoding = 'utf-8', index = False)

