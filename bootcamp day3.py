# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 08:22:24 2020

@author: emkmu
"""

# Print the time

import datetime

from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

print(current_time)


# Make a simple stopwatch

import time

start = time.time()
end=time.time()
print(end-start)

start_time = datetime.now() 
time_elapsed = datetime.now() - start_time
print('Time elapsed (hh:mm:ss.ms) {}'.format(time_elapsed))


# Print a word provided by a user:

val = input("Please provide a word:")
print(val)

# Validate user input:
while True:
    try:
        word = input("Enter a word:")
        test = int(word)
    except ValueError:
        print(word)
        break
    else:
        print("Please enter a word")
        continue

#Record and Print a List

word_1 = input("Enter an item: ")
word_2 = input("And another: ")
word_3 = input("And another: ")
print(word_1,word_2,word_3)

# Module 6 - Performing End to End
# load pandas package
import pandas as pd

# Part 1: read data into data frame
df =  pd.read_csv("andre.csv")

# Part 2: remove data from 1976 and after 1993
df = df[ df.Year > 1976 ]
df = df[ df.Year < 1994 ]

df.head()


# Part 3: make a histogram
df.hist("H",bins=100)

# Create my own pipeline

df = pd.read_csv('hotels-properties-citywide-1.csv')

df.head()

df = df[ df.BOROCODE != 5 ]

df.head()

df.hist("Borough",bins=4)
