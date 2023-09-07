# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:53:48 2023

@author: moham
"""

import numpy as np
a=np.arange(1,7 ).reshape(2, 3)
b=np.arange(7,13 ).reshape(2, 3)
print(a,'\n', b)
print('\n')
print(a+b)
print('\n')
print(a*b)
print('\n')
c=np.arange(1,7 ).reshape(2, 3)
d=np.arange(7,13 ).reshape(3, 2)
print(c@d)
print('\n')
print(c .dot( d))
print('\n')

A=np.arange(1,13 ).reshape(3, 4)
print(A)
print('\n')
print(A.sum(axis=1))
print('\n')
print(A.sum(axis=0))
print('\n')
print(A.cumsum(axis=1))
print('\n')
print(A.cumsum(axis=0))