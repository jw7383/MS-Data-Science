# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:12:24 2021

@author: jason
"""

import numpy as np
import matplotlib.pyplot as plt

data1 = np.genfromtxt("radioactive_sample_1.txt")
moving_avg1 = np.array([])
for i in range(len(data1)):
    temp_moving_avg = np.mean(data1[:(i+1)])
    moving_avg1 = np.append(moving_avg1, temp_moving_avg)

fig = plt.figure()    
plt.plot(moving_avg1)

data2 = np.genfromtxt("radioactive_sample_2.txt")
moving_avg2 = np.array([])
for i in range(len(data2)):
    temp_moving_avg = np.mean(data2[:(i+1)])
    moving_avg2 = np.append(moving_avg2, temp_moving_avg)

fig = plt.figure()    
plt.plot(moving_avg2)

data2_median = np.median(data2)