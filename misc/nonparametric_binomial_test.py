#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 17:49:07 2018

@author: mm
"""

import pandas as pd 
from scipy.stats import binom
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')


datasets_path = "/Users/mm/code/Estadistica_Teorica_2018/datasets/"

df = pd.read_csv(f"{datasets_path}NBA_player_of_the_week.csv") 
df.describe()

"""
X = "age of the player of the week"
P(X <= 23) = p
"""

# Single tailed.  h0: p < p0 vs. h1: p > p0

T = sum(df['Age'] <= 23)
n = len(df['Age'])
p0 = 0.2 # p for null hypoteses
rv = binom(n, p0)

# Probability of Bi(n, p0)
fig, ax = plt.subplots(1, 1)
x = np.arange(rv.ppf(0.0001), rv.ppf(0.9999999999))
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()
plt.axvline(x=T, color='b', linestyle='--')
plt.axvline(x=rv.ppf(0.95), color='r', linestyle='--')

# Two tailed.  h0: p = p0 vs. h1: p != p0
# Probability of Bi(n, p0)
fig, ax = plt.subplots(1, 1)
x = np.arange(rv.ppf(0.0001), rv.ppf(0.9999999999))
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()
plt.axvline(x=T, color='b', linestyle='--')
plt.axvline(x=rv.ppf(0.975), color='r', linestyle='--')
plt.axvline(x=rv.ppf(0.025), color='r', linestyle='--')

