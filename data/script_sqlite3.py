# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 22:50:53 2020

@author: Sam
"""
#%%
import os
os.chdir('C:\\Users\\Sam\\Documents\\Imperial\\IC_modules\\DataScience_Science\\cw4')

import numpy as np
import pandas as pd
import sqlite3
#%%

def to_csv():
    db = sqlite3.connect('compas.db')
    cursor = db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    for table_name in tables:
        table_name = table_name[0]
        table = pd.read_sql_query("SELECT * from %s" % table_name, db)
        table.to_csv(table_name + '.csv', index_label='index')
    cursor.close()
    db.close()

to_csv()

#%%
df = pd.read_csv("FOC_lexicon_003_final.csv")
#%%
queries = ['assault', 'burglary', 'crime', 'criminal', 'prison', 'drugs', 'fraud', 'gang', 'police']

sub_df = df.loc[df.query_word.isin(queries), ['query_word', 'word']]

sub_df.to_csv("crime_lexicon.csv")