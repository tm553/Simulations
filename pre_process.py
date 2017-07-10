# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:09:20 2017

@author: Tom
"""

import csv
import collections
import pprint
import pandas as pd

df = pd.read_csv('DemandData.csv')
cols = df.columns

df['Year'] = df['SETTLEMENT_DATE'].apply(lambda x: str(x).split('-')[-1])

df['Month'] = df['SETTLEMENT_DATE'].apply(lambda x: str(x).split('-')[1])

for i in set(df.Year): # for classified by years files
    filename = "DemandData"+i+".csv"
    df.loc[df.Year == i].to_csv(filename,index=False,columns=cols)
    df_month = pd.read_csv("DemandData"+i+".csv")
    cols2 = df_month.columns
    df_month['Month'] = df_month['SETTLEMENT_DATE'].apply(lambda x: str(x).split('-')[1])
    for j in set(df_month.Month): # for classified by months files
        filename2 = "DemandData"+i+"_"+j+".csv"
        df_month.loc[df_month.Month == j].to_csv(filename2,index=False,columns=cols2)

    
    
    
#df['Month'] = df['SETTLEMENT DATE'].apply(lambda x: x.split('-')[1])  
    
#for i in set(df.Month): # for classified by months files
#    filename = "path/"+i+".csv"
#    df.loc[df.Month == i].to_csv(filename,index=False,columns=cols)