# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 10:19:52 2021

@author: Julka
"""

import math as m
import numpy as np

print('układ 2000')
#dane

#HIRVONEN
fi_A = 0.9022890319365018
lam_A = 0.31722166102338717
h_a = 9000
#KIVIOJ
fi_B = 0.9036039237454395
lam_B = 0.3258394151557968
h_b = 100
a = 6378137
e2 = 0.00669438002290
e_2 = e2/(1-e2)

#skala pld srodkowego
m_0 = 0.999923

def uklad_2000(fi,lam,a,e2,m_0,h):
    N = a/(m.sqrt(1-e2 * np.sin(fi)**2))
    t = np.tan(fi)
    n2 = e_2 * np.cos(lam)**2
    lam = m.degrees(lam)
    
    if lam > 13.5 and lam < 16.5:
        s = 5
        lam_0 = 15
    elif lam > 16.5 and lam < 19.5:
        s = 6
        lam_0 = 18
    elif lam > 19.5 and lam < 22.5:
        s = 7
        lam_0 = 21
    elif lam > 22.5 and lam < 25.5:
        s = 8
        lam_0 = 24
        
    lam = m.radians(lam)
    lam_0 = m.radians(lam_0)
    l = lam - lam_0
    
    A_0 = 1 - (e2/4) - (3*(e2**2))/64 - (5*(e2**3))/256
    A_2 = 3/8 * (e2 + ((e2**2)/4) + ((15*e2**3)/128))
    A_4 = 15/256 * (e2**2 + (3*(e2**3))/4)
    A_6 = (35*(e2**3))/3072
    
    
    sigma = a* ((A_0*fi) - (A_2*np.sin(2*fi)) + (A_4*np.sin(4*fi)) - (A_6*np.sin(6*fi)))
    
    x = sigma + ((l**2)/2) * (N*np.sin(fi)*np.cos(fi)) * (1 + ((l**2)/12) * ((np.cos(fi))**2) * (5 - t**2 + 9*n2 + (4*n2**2)) + ((l**4)/360) * ((np.cos(fi))**4) * (61 - (58*(t**2)) + (t**4) + (270*n2) - (330 * n2 *(t**2))))
    y = l * (N*np.cos(fi)) * (1 + ((((l**2)/6) * (np.cos(fi))**2) * (1-(t**2) + n2)) +  (((l**4)/(120)) * (np.cos(fi)**4)) * (5 - (18 * (t**2)) + (t**4) + (14*n2) - (58*n2*(t**2))))

    x00 = round(x * m_0, 3)
    y00 = round(y * m_0 + (s*1000000) + 500000, 3)   
    
    return x00, y00, h 


x,y,h = uklad_2000(fi_A, lam_A, a, e2, m_0,h_a)
x1, y1,h1 = uklad_2000(fi_B, lam_B, a, e2, m_0,h_b) 

print('wspolrzedne punktu poczatkowego:', x, y,h)
print('wspolrzedne punktu koncowego:', x1, y1,h1)

    
    
    
    
    
    
    
    
        
        
    