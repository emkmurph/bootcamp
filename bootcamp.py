# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 12:18:54 2020

@author: emkmu
"""


'spam eggs'

2+2
random()
import numpy
random()

import random as rand


rand.random()

data = []
for i in range (10):
    print(i)
    data.append(rand.randint(1,10))
    
    
    
    
    import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
np.random.seed(42)
x = np.random.normal(size=1000)
plt.hist(x, density=True, bins=30)  # `density=False` would make counts
plt.ylabel('Probability')
plt.xlabel('Data');