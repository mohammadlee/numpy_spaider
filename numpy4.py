# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 14:13:04 2023

@author: moham
"""

import numpy as np
#zero matries
arr=np.zeros((3,3),dtype=int)
print(arr)
arr1=np.zeros(15,dtype=int)
print(arr1)
arr2=np.zeros(15,dtype=int).reshape(3, 5)
print(arr2)
#ones matries
brr=np.ones((4,4),dtype=int)
print(brr)
brr1=np.ones(18,dtype=int)
print(brr1)
brr2=np.ones(18,dtype=int).reshape(2,9)
print(brr2)
#empty matries
crr=np.empty((2,3))
print(crr)
crr1=np.empty(6)
print(crr1)
crr2=np.empty(6).reshape(3, 2)
print(crr2)
#random
re=np.random.default_rng(1)
drr=re.random(6)
print(drr)
