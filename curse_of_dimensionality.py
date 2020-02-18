# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 09:38:13 2020

@author: V Ojha
"""
#%%
import numpy as np
import math
from matplotlib import pyplot as plt
from sklearn.metrics.pairwise import euclidean_distances
#%%
n = 500 # number  of samples 
dim = 100  # number of dimensions
step = 1



xvalue = []
dist_log = []

plt.figure(figsize=(10, 6))

for i in range(0, dim, step): 
    if(i == 0):
        m = 2 
    else:
        m = i 
        
    
    points  = np.random.rand(n,m)
    dist = euclidean_distances(points, points)
    mask = np.ones(dist.shape, dtype=bool)
    np.fill_diagonal(mask, 0)
    max_value = dist[mask].max()
    min_value = dist[mask].min()
    
    xvalue.append(m)
    dist_log.append(math.log10((max_value - min_value)/min_value))
    
    #print(m,dist_log,"\n")

plt.plot(xvalue,dist_log,'b-')
plt.xlabel('Increasing order of dimension')
plt.ylabel(r'$\log \left(\dfrac{dist_{max}(p_i,p_j) - dist_{min}(p_i,p_j)}{dist_{min}(p_i,p_j)} \right)$')
plt.show()
plt.savefig('CoD.pdf')
