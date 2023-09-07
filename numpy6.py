# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 17:04:28 2023

@author: moham
"""

import numpy as np 

r1=np.sin(2)
print(r1)
#
sum=0
for i in range(10):
    sum=sum+np.sin(np.sqrt(i))
    
print(sum)
print('\n')
print(np.math.factorial(4))
print(np.math.sin(30))
####################################sin(x)##########################
sum=0
x= float(input('enter your number'))
for i in range(5):
    sum=sum+np.power(-1,i)*np.power(x,2*i+1)/np.math.factorial(2*i+1)
    
print(sum)
print('\n')
#################################################################### 
a=np.arange(6).reshape(2, 3)
print(np.sin(a))
b=np.arange(1,7).reshape(2, 3)
print(np.log (b))
c=np.arange(1,7).reshape(2, 3)
print(np.log10(c))
print('\n')
A=np.arange(1,15).reshape(7, 2)
for row in A:
    print(row)
print('\n')
for i in A.flat:
    print(i)