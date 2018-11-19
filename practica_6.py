#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 08:27:08 2018

@author: mm
"""
import numpy as np
from scipy import stats as st


# Ejercicio 6
sample = [1.52, 1.65, 1.72, 1.65, 1.72, 1.83, 1.62, 1.75, 1.72, 1.68, 1.51, 
          1.65, 1.58, 1.65, 1.61, 1.70, 1.60, 1.73, 1.61, 1.52, 1.81, 1.72, 
          1.50, 1.82, 1.65]
sample_mean = np.mean(sample)

s2 = sum([(x - sample_mean)**2 for x in sample]) / (len(sample) - 1)
s = np.sqrt(s2)

t = {
     '.95': 2.0639
 }
interval95= (sample_mean - t['.95'] * s / np.sqrt(len(sample)), 
             sample_mean + t['.95'] * s / np.sqrt(len(sample)))

# Check the correctness
interval95_builtin = st.t.interval(0.95, len(sample)-1, loc=np.mean(sample), scale=st.sem(sample))


