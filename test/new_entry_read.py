#Python 3

import pandas as pd #import pandas library

#there needs to be a check to make sure the 'new' csv has data in the same form as 'old'

with open('old.csv', 'r', encoding='utf-8') as t1, open('new.csv', 'r', encoding='utf-8') as t2:
   fileone = t1.readlines()
   filetwo = t2.readlines() #read new input and existing input
  
 
with open('update.csv', 'w', encoding='utf-8') as outFile:
    for line in filetwo:    
        if line not in fileone:
           outFile.write(line) #write difference between the new and existing inputs

f1 = pd.read_csv('old.csv', index = False)
f2 = pd.read_csv('update.csv', index = False)

#final = f1.append(f2) #append new rows to the existing rows
final = pd.concat([f1, f2], axis= 0)

with open('master_test.csv', 'w', encoding='utf-8', newline='') as f3:
    final.to_csv(f3, index=False) #create new file with all updates
