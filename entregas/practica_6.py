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
IntervalData = namedtuple('IntervalData', 'bounds, length, is_covering')




n = (20, 50, 100)
p = (.1 , .5)
K = 2000

n = 100 # TODO: borrar
p = .1 # TODO: borrar
# %%Metodo 1


intervals = []
for i in range (0, K):

    quantile = stats.norm.ppf(0.975)
    sample_mean = np.random.binomial(n, p, 1)[0] / n

    interval = (sample_mean - quantile * np.sqrt(sample_mean * (1 - sample_mean)/n),
                sample_mean + quantile * np.sqrt(sample_mean * (1 - sample_mean)/n))

    intervals.append(IntervalData(bounds=interval,
                                  length=interval[1] - interval[0],
                                  is_covering=int(p > interval[0] and p < interval[1])))


df = pd.DataFrame(intervals)
print(df.is_covering.value_counts()/K)
df.length.hist(bins=20)

# %% Metodo 2

def get_roots(a, b, c):
    """Calculates the roots of a quadratic equation of the form: ax^2 + bx + c = 0.

    Returns:
        tuple: sorted roots
    """
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    return sorted(x1, x2)

intervals = []
for i in range (0, K):

    quantile = stats.norm.ppf(0.975)
    sample_sum = np.random.binomial(n, p, 1)[0]

    # quadratic equation coefficients
    coeff_a = n**2 + n * quantile**2
    coeff_b = -(2 * n * sample_sum + quantile**2 * n)
    coeff_c = sample_sum ** 2

    interval = get_roots(a=coeff_a,
                         b=coeff_b,
                         c=coeff_c)

    intervals.append(IntervalData(bounds=interval,
                                  length=interval[1] - interval[0],
                                  is_covering=int(p > interval[0] and p < interval[1])))




