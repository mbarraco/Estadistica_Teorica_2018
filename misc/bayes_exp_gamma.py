"""A posteriori calculation of an a priori Exponential distributed rate variable <l> for a Gamma
distributed variable <T>
"""
import numpy as np
from scipy.stats import gamma, expon
import pandas as pd
import matplotlib.pyplot as plt
plt.close('all')

n = 100
l = 4
scale = 1 / l
a = 2 # alpha
rv_priori = expon()

sample = [.75]
scale_posteriori= 1 / sum(sample)
rv_posteriori = gamma(a=2* len(sample) + 1, scale=scale_posteriori)

x = np.linspace(rv_priori.ppf(0.0001), 20, 100)

# Figures
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(x, rv_priori.pdf(x), 'r', label='dist.')
ax1.axvline(x=rv_priori.expect(), color='g', linestyle=':', label='exp. val.')
ax1.set_title("priori")
ax1.legend()
ax2.plot(x, rv_posteriori.pdf(x), 'b',  label='a posteriori')
ax2.axvline(x=rv_posteriori.expect(), color='g', linestyle=':', label='exp. val.')
ax2.set_title("posteriori")
ax2.legend()
