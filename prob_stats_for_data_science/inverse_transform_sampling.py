# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 18:05:46 2021

@author: jason
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.load('samples.npy')
print(np.min(data))
print(np.max(data))
#data = np.random.exponential(1,1000)

def cdf(data):
    f = 1 - np.exp(data * -1)
    return f

cdfdata = cdf(data)

plt.hist(cdfdata, bins = 30, color = 'white', edgecolor = 'black')

