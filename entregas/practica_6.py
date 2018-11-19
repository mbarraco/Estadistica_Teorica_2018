#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 18 13:50:07 2018

@author: Mariano y Mauro
"""
import numpy as np
from scipy import stats
from collections import namedtuple
import pandas as pd
import matplotlib.pyplot as plt
import pickle


plt.close('all')
IntervalData = namedtuple('IntervalData', 'bounds, length, is_covering')

# Configuración de las simulaciones
n_collection = (20, 50, 100)
p_collection = (.1 , .3)
K = 2000

quantile = stats.norm.ppf(0.975)


def get_roots(a, b, c):
    """Calculates the roots of a quadratic equation of the form: ax^2 + bx + c = 0.
    
    Returns:
        tuple: sorted roots
    """
    x1 = (-b + np.sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b - np.sqrt(b**2 - 4*a*c)) / (2 * a)
    return sorted((x1, x2))

experiment_data = {}
for n in n_collection:
    for p in p_collection:
        print(f"{n}{p}")
        intervals_1 = []
        intervals_2 = []
        for i in range (0, K):

            # Metodo 2
            sample_sum = np.random.binomial(n, p, 1)[0]
        
            # quadratic equation coefficients
            coeff_a = n**2 + n * quantile**2
            coeff_b = -(2 * n * sample_sum + quantile**2 * n)
            coeff_c = sample_sum ** 2
        
            interval = get_roots(a=coeff_a,
                                 b=coeff_b,
                                 c=coeff_c)
            intervals_2.append(IntervalData(bounds=interval,
                                          length=interval[1] - interval[0],
                                          is_covering=int(p > interval[0] and p < interval[1])))
            # Metodo 1
            sample_mean = sample_sum / n
            interval = (sample_mean - quantile * np.sqrt(sample_mean * (1 - sample_mean)/n),
                        sample_mean + quantile * np.sqrt(sample_mean * (1 - sample_mean)/n))
            intervals_1.append(IntervalData(bounds=interval,
                                          length=interval[1] - interval[0],
                                          is_covering=int(p > interval[0] and p < interval[1])))
            
            experiment_data[(n,p,1)] = intervals_1
            experiment_data[(n,p,2)] = intervals_2
            
    df = pd.DataFrame(intervals_2)
    df.length.hist(bins=50)

       

with open('/Users/mm/code/Estadistica_Teorica_2018/entregas/practica_6_data', 'wb') as out_file:
    pickle.dump(experiment_data, out_file, protocol=2)

