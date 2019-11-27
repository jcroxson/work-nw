# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 11:46:49 2019

@author: JCroxson
"""
#import pandas library
import pandas as pd
#read in master file
r1 = pd.read_csv('replace.csv')
#find location of entry in question (do in batches if necessary)
r1.loc[r1['ASIN'] == 'G55UH76W', 'SubBrand'] = 'Prebiotic'
#r1.loc[r1['ASIN'] == 'ASIN_in_question', 'column_to_change_here'] = 'add_change_here'
#r1.loc[r1['ASIN'] == 'ASIN_in_question', 'column_to_change_here'] = 'add_change_here'
#r1.loc[r1['ASIN'] == 'ASIN_in_question', 'column_to_change_here'] = 'add_change_here'
#r1.loc[r1['ASIN'] == 'ASIN_in_question', 'column_to_change_here'] = 'add_change_here'
#r1.loc[r1['ASIN'] == 'ASIN_in_question', 'column_to_change_here'] = 'add_change_here'
#write new entry
r1.to_csv('replace.csv', index = False)