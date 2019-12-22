# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 12:38:09 2019

@author: callaway

Goal: Build a password generator using the diceware list
and methodology
"""
import pandas as pd
import random
    
def getList():
    
    path = 'http://world.std.com/~reinhold/diceware.wordlist.asc'
    listy = pd.read_csv(path, dtype = {'-----BEGIN PGP SIGNED MESSAGE-----':
                                       str})
    listy.rename(columns ={'-----BEGIN PGP SIGNED MESSAGE-----':'number'},
                 inplace = True)
    listy = listy.iloc[0:7776]
    listy['word'] = listy.number.str[6:]
    listy.number = listy.number.str[:5]
    listy.number = listy.number.astype(int)
    listy.set_index('number',inplace = True)
    return listy

def rollDice():
    
    all_rolls = []
    for x in range(0,5):
        roll = []
        for x in range(0,5):
            num = random.randint(1,6)
            roll.append(num)
        s = [str(i) for i in roll]
        nums = int("".join(s))
        all_rolls.append(nums)    
    return all_rolls


def getPassWord(list_of_words,list_of_rolls):
    
    words = []
    for index in list_of_rolls:
        w = list_of_words.loc[index,'word']
        words.append(w)
    s = [str(i) for i in words]
    password = str("".join(s))
    return password

# Make your password
print(getPassWord(getList(), rollDice()))
