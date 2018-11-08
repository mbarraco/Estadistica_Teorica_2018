#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 07:53:31 2018

Practica 5, Estadística Teórica 2018.
@author: mm
"""
import numpy as np
from scipy import stats as st
from scipy.special import comb

# Ejercicio 5.6


# Hardcoded version
delta = (3/7) * (1/15) * sum([i * i * (6-i) for i in range(1,7)])

# General version
x = 1 # medición
total = 6 # total
#n = 50 # favorables
sacadas = 2 




def prob_posteriori(sample, theta):
    """Evaluates de posteriori probability of the urn containing <theta> white
    balls.
    
    Args:
        sample: the amount of drawn white balls.
        theta: the amount of white balls in the urn.
    
    """
    prob_sample = (1/6) * sum(
            [st.hypergeom.pmf(M=total, n=i, N=sacadas, k=sample)
             for i in range(1,7)]
        )
    prob_joint = (1/6) * st.hypergeom.pmf(M=total, n=theta, N=sacadas, k=sample)
    return prob_joint / prob_sample
    

delta = sum([prob_posteriori(sample=x, theta=i) * i for i in range(1, 7)])
print((f"Given that {x} white balls out of {sacadas} were drawn, "
       f"the estimation for the total amount of white balls is {delta}"))
