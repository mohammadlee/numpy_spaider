# -*- coding: utf-8 -*-
"""
Created on Wed Sep  6 22:02:47 2023

@author: moham
"""

import numpy as np
#linspace
arr=np.linspace(1,5)
print(arr)
arr1=np.linspace(1,5,num=10)
print(arr1)
arr2=np.linspace(1,5,num=10,dtype=float)
print(arr2)
arr3=np.linspace(1,5,num=10,dtype=float,endpoint=False)
print(arr3)
arr4=np.linspace(1,5,num=10,dtype=float,endpoint=False).reshape(2, 5)
print(arr4)
#logspace
brr=np.logspace(1,5)
print(brr)
brr1=np.logspace(1,5,num=3)
print(brr1)
brr2=np.logspace(1,5,num=3,base=2)
print(brr2)
brr3=np.logspace(1,5,num=3,base=2,endpoint=True)
print(brr3)
brr4=np.logspace(1,5,num=6,base=2,endpoint=True).reshape(2, 3)
print(brr4)
#geomspace
crr=np.geomspace(1,5)
print(crr)
crr1=np.geomspace(1,5,num=5)
print(crr1)
crr2=np.geomspace(1,5,num=5,dtype=complex)
print(crr2)
crr3=np.geomspace(1,5,num=5,dtype=complex,endpoint=True)
print(crr3)
crr4=np.geomspace(1,5,num=16,dtype=complex,endpoint=True).reshape(4, 4)
print(crr4)
