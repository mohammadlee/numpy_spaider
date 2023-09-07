# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np 

arr=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr)
print(arr[1:10:2])#even
brr=np.array([[1,2,3,4,5],
              [6,7,8,9,10],
              [11,12,13,14,15]])
print(brr)
a=brr[1:2,3:4]
print(a)#9
b=brr[1:4,2:4]
print(b)#[[8,9],[13,14]]

