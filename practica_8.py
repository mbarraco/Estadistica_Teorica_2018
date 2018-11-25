#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:25:03 2018

@author: mm
"""
%reset -f
import itertools
from collections import defaultdict
import pandas as pd
from scipy.stats import binom, rv_discrete
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')


def build_wilcoxon_ranks(samples):
    """Ranks each element of samples according to its absolute value

    Args:
        samples (iterable): each element is a float

    Returns:
        dict: {'index':'rank'}, here 'index' identifies an element in the
        given sample list.
    """
    sorted_indexes = np.argsort(samples)
    sample_ranks = {}
    rank = 0
    ranks = []
    indexes_to_be_ranked = []

    while rank < len(sorted_indexes):

        ranks.append(rank+1)
        indexes_to_be_ranked.append(sorted_indexes[rank])

        if rank == len(sorted_indexes) - 1 or samples[sorted_indexes[rank]] != samples[sorted_indexes[rank + 1]]:
            shared_rank = np.mean(ranks)
            for i in indexes_to_be_ranked:
                sample_ranks[i] = shared_rank

            indexes_to_be_ranked = []
            ranks = []


        rank += 1
    return sample_ranks

# %%
"""
Ejercicio 1. Se piensa que el ph mediano es 6.

H0: theta = 6 vs theta !=6
"""
samples = (5.93, 6.08, 5.86, 5.91, 6.12, 5.90, 5.95, 5.89, 5.98, 5.96)
samples = tuple(el - 6 for el in samples)

# Null hypotheses distro
rv = binom(n=len(samples), p=.5)
x = np.arange(rv.ppf(0.01), rv.ppf(1))
ax = plt.subplot(1, 1, 1)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1)
ax.legend(loc='best')
plt.show()

# Rejection zone
ax.set_ylim(0,.3)
plt.axvline(x=rv.ppf(0.025), color='r', linestyle='--')
plt.axvline(x=rv.ppf(0.975), color='r', linestyle='--')
ax.annotate(r'$\alpha = 0.025$',
            xy=(rv.ppf(0.025), .3),
            xytext=(rv.ppf(0.025), .33),
            arrowprops = {'facecolor':'r', 'shrink':.05})
ax.annotate(r'$\alpha = 0.975$',
            xy=(rv.ppf(0.975), .3),
            xytext=(rv.ppf(0.975), .33),
            arrowprops = {'facecolor':'r', 'shrink':.05})
# Test statistc
T = sum((el > 0 for el in samples ))
plt.axvline(x=T, color='b', linestyle='--')

# %%
"""
Ejercicio 2. Pesos antes y después de una dieta ¿funcionó?

Método: Test del signo.
From Wikipedia:
    "The sign test is a statistical method to test for consistent differences 
    between pairs of observations, such as the weight of subjects before and 
    after treatment. Given pairs of observations (such as weight pre- and 
    post-treatment) for each subject, the sign test determines if one member of
    the pair (such as pre-treatment) tends to be greater than (or less than) 
    the other member of the pair (such as post-treatment)."

Hipótesis nula: La V.A x = "peso inicial - peso final" tiene mayor probabilidad
de ser negativa (ascenso de peso) que positiva (descenso), es decir:
p(X <= 0) ~ Bi(n, p), con p > 0.5

h0: p >= 0.5 vs. h1: p < 0.5

h1 significa que es más probable obtener resultados negativos (descenso de
peso) que resultados positivos o cero.

obs: test the hypothesis that the difference between the X and Y has
zero median, assuming continuous distributions of the two random variables
X and Y, in the situation when we can draw paired samples from X and Y.

"""
plt.close('all')

nivel_de_confianza = .95

samples = ((174, 165), (191, 186), (188, 183), (182, 178), (201, 203),
          (188, 181))

T = sum(int(i - j < 0) for i, j in samples if j !=i)

# Null hypothesis distribution
rv = binom(n=len(samples), p=.5)
x = np.arange(rv.ppf(0.01), rv.ppf(1))
ax = plt.subplot(1, 1, 1)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1)
ax.legend(loc='best')
plt.show()

# Rejection zone
ax.set_ylim(0,.3)
plt.axvline(x=rv.ppf(0.05), color='r', linestyle='--')
ax.annotate(r'$\alpha = 0.05$',
            xy=(rv.ppf(0.05), .3),
            xytext=(rv.ppf(0.05), .33),
            arrowprops = {'facecolor':'r', 'shrink':.05})

plt.axvline(x=T, color='b', linestyle='--')
p_value = rv.cdf(T) if rv.cdf(T) < 0.5 else 1 - rv.cdf(T)
if p_value < 1-nivel_de_confianza:
    print((f"El valor del estadístico T={T} me da un p-valor={p_value}. "
           "Es suficiente para rechazar la hipotesis nula con un nivel de "
           "confianza de 0.95"))
else:
    print((f"El valor del estadístico T={T} me da un p-valor={p_value}. "
           "No es suficiente para rechazar la hipotesis nula con un nivel de "
           "confianza de 0.95"))




# %%
"""
Ejercicio 4. 

Método: Test del signo. (Conover, p 157)
From Wikipedia:
    "The sign test is a statistical method to test for consistent differences 
    between pairs of observations, such as the weight of subjects before and 
    after treatment. Given pairs of observations (such as weight pre- and 
    post-treatment) for each subject, the sign test determines if one member of
    the pair (such as pre-treatment) tends to be greater than (or less than) 
    the other member of the pair (such as post-treatment)."

theta = "diferencia entre el tiempo de reacción antes y después de ingerir
         alchohol"

Idea: la hipótesis nula es que la V.A: "diferencia en cada para (X,Y): X-Y > 0"
sigue una Bi(n, 0.5). Es decir, es igualmente probable que después ingerir
alcohol el tiempo de reacción se acorte o alargue.


    h0: X == 0 vs h1: theta != 0
    
"""
plt.close('all')

samples = ((0.68, 0.73), (0.64, 0.62), (0.68, 0.66), (0.82, 0.92),
           (0.58, 0.68), (0.80, 0.87), (0.72, 0.77), (0.65, 0.70),
           (0.84, 0.88), (0.73, 0.79), (0.65, 0.72), (0.59, 0.60),
           (0.78, 0.78), (0.67, 0.66), (0.65, 0.68), (0.76, 0.77),
           (0.61, 0.72), (0.86, 0.86), (0.74, 0.72), (0.88, 0.97))

# Sign test. Compute the sign of the difference for each (X,Y): Y - X
T = sum((int(i - j > 0) for i, j in samples if i != j))

# Null hypothesis distribution
rv = binom(n=len(samples), p=.5)
x = np.arange(rv.ppf(0.01), rv.ppf(1))
ax = plt.subplot(1, 1, 1)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1)
ax.legend(loc='best')
plt.show()

# Rejection zone for two tailed
ax.set_ylim(0,.3)
plt.axvline(x=rv.ppf(0.025), color='r', linestyle='--')
plt.axvline(x=rv.ppf(0.975), color='r', linestyle='--')
ax.annotate(r'$\alpha = 0.025$',
            xy=(rv.ppf(0.025), .3),
            xytext=(rv.ppf(0.025), .33),
            arrowprops = {'facecolor':'r', 'shrink':.05})
ax.annotate(r'$\alpha = 0.975$',
            xy=(rv.ppf(0.975), .3),
            xytext=(rv.ppf(0.975), .33),
            arrowprops = {'facecolor':'r', 'shrink':.05})

# Test statistc
plt.axvline(x=T, color='b', linestyle='--')
p_value = rv.cdf(T)
print(f"Se observa un p-valor={p_value}")
print((f"El valor del estadístico T={T}, bajo la hipótesis nula, tiene una"
      "probabilidad muy baja. Entonces se rechaza h0."))

# %%
"""
Ejercicio 5.(Conover 5.7, p 353)

Método: test de rango signado de Wilcoxon
From Wikipedia:
    "The Wilcoxon signed-rank test is a non-parametric statistical hypothesis 
    test used to compare two related samples, matched samples, or repeated 
    measurements on a single sample to assess whether their population mean 
    ranks differ (i.e. it is a paired difference test).
    
    H0: difference between the pairs follows a symmetric distribution around 
    zero
    H1: difference between the pairs does not follow a symmetric distribution 
    around zero."

def: Delta = mu_g - mu_e

Idea: la hipótesis nula es que la V.A: "D == 0" sigue una Bi(n, 0.5). 
Es decir, es igualmente probable medir un D positivo o negativo.


    h0: p(D==0) = p = 0.5 vs h1: p != 0.5
    
"""
nivel_de_confianza = 0.05
plt.close('all')


samples_g = (54.7, 58.5, 66.8, 46.1, 52.3, 74.3, 92.5, 40.2, 87.3, 74.8, 63.2, 
             68.5)
samples_e = (55.0, 55.7, 62.9, 45.5, 51.1, 75.4, 89.6, 38.4, 86.8, 72.5, 62.3, 
             66.0)

samples = tuple(zip(samples_g, samples_e)); 

samples_abs_diff = tuple(np.abs(i - j) for i, j in samples if i != j)

sample_ranks = build_wilcoxon_ranks(samples_abs_diff)
    
T = sum(rank for index, rank in sample_ranks.items() 
        if samples[index][0] > samples[index][1])

# Exact distribution of T
occurrences = [0] * (1 + int(len(samples) * (len(samples) + 1) / 2))
for combination in itertools.product([0, 1], repeat=len(samples)):
    rank_sum = sum(index + 1 for index, val in enumerate(combination) if val == 1)
    occurrences[rank_sum] += 1
probabilities = [i / 2**12 for i in occurrences]

# Generate a random variable from probabilities    
rv = rv_discrete(values=(np.arange(len(probabilities)), probabilities))


x = np.arange(rv.ppf(0.01), rv.ppf(1))
ax = plt.subplot(1, 1, 1)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1)
ax.legend(loc='best')
plt.show()

# Rejection zone for two tailed
ymax = 0.035
ax.set_ylim(0, ymax)
plt.axvline(x=rv.ppf(0.025), color='r', linestyle='--')
plt.axvline(x=rv.ppf(0.975), color='r', linestyle='--')
ax.annotate(r'$\alpha = 0.025$',
            xy=(rv.ppf(0.025), ymax),
            xytext=(rv.ppf(0.025), ymax*1.08),
            arrowprops = {'facecolor':'r', 'shrink':.05})
ax.annotate(r'$\alpha = 0.975$',
            xy=(rv.ppf(0.975), ymax),
            xytext=(rv.ppf(0.975), ymax*1.08),
            arrowprops = {'facecolor':'r', 'shrink':.05})


# Test statistc
plt.axvline(x=T, color='b', linestyle='--')
p_value = 2 *(rv.cdf(T) if rv.cdf(T) < 0.5 else 1 - rv.cdf(T))
ax.annotate(fr'$T ={T}$',
            xy=(T, ymax),
            xytext=(T, ymax*1.04))


if p_value < 1-nivel_de_confianza:
    print((f"El valor del estadístico T={T} me da un p-valor={p_value}. "
           "Es suficiente para rechazar la hipotesis nula con un nivel de "
           "confianza de 0.95"))
else:
    print((f"El valor del estadístico T={T} me da un p-valor={p_value}. "
           "No es suficiente para rechazar la hipotesis nula con un nivel de "
           "confianza de 0.95"))

