# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 08:24:53 2021

@author: admin
"""

X =  4242710.000 
Y =  4242710.000
Z =  0.0001

a = 6000000
e2 = 0.007
import math
import numpy as np
print('hirvonem')
def hirvonen (X, Y, Z, a, e2):
    r = math.sqrt(X**2 + Y**2)
    fi_n = math.atan(Z/(r*(1-e2)))
    eps = 0.000001/3600 *math.pi/180 # radiany
    fi = fi_n*2
    while np.abs(fi_n - fi) > eps:
        fi = fi_n
        N = a/np.sqrt(1-e2*np.sin(fi_n)**2)
        h = r/np.cos(fi_n) -N
        fi_n = math.atan(Z/(r*(1-e2*(N/(N + h)))))
    lam = math.atan(Y/X)
    h = r/np.cos(fi_n) -N
    return fi, lam, h
def s_m_s(fi):
    fi= fi*180/math.pi # stopnie
    d =np.floor(fi)
    m = np.floor((fi - d)*60)
    s = round((fi -d -m/60)*3600, 5)
    print(d, 'st', m, 'min', s, 'sek')
fi, lam, h = hirvonen(X, Y, Z, a, e2)
print('fi = ')
s_m_s(fi)
print('lam = ')
s_m_s(lam)
print('h =',round(h, 3))
print('fi =' , fi,'lam = ' ,lam) 




