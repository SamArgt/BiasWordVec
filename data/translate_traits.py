# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:32:58 2020

@author: Sam
"""
#%%
import os
os.chdir('C:\\Users\\Sam\\Documents\\Imperial\\IC_modules\\DataScience_Science\\BiasWordVec\\data')
import numpy as np
from googletrans import Translator


f = open("traits_words.txt")
lines = f.readlines()
words_en = [w.strip() for w in lines]
f.close()

#%%

words_fr = []
count_na = 0
i =1
for w in words_en:
    translator = Translator()
    try:
        w_fr = translator.translate(w, src='en', dest='fr').text
    except:
        count_na += 1
        w_fr = np.nan
        
    if i % (len(words_en) // 10) == 0:
        print("{} % ".format(i * 100 // len(words_en)))
        
    i+=1 
    words_fr.append(w_fr)
    
#%%
f = open("traits_words_fr.txt", "w")
f.writelines('\n'.join(words_fr))
f.close()
