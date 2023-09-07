# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 20:40:20 2023

@author: moham
"""

import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr.ndim)
brr=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])
print(brr.ndim)
print(arr.shape)
print(brr.shape)
brr1=np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]).reshape(4,3)
print(brr1)   
crr=np.arange(16)
print(crr) 
drr=np.arange(0,16,2)
print(drr)          
err=np.arange(0,16,2).reshape(4,2)
print(err)
print(arr.size)
print(arr.dtype)
rt=np.arange(1,16,dtype=float).reshape(3,5)
print(rt)
print(arr.itemsize)
p=2*(np.pi)
print(p)
v=np.arange(0,2*np.pi,0.2 ,dtype=float)
print(v)