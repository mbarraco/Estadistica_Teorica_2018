from scipy.stats import chi2
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')


#%% Chi squared
fig, (ax1, ax2) = plt.subplots(2, 1)
shape_parameters = [55]
mean, var, skew, kurt = chi2.stats(*shape_parameters, moments='mvsk')
x = np.linspace(chi2.ppf(0.01, shape_parameters[0]), chi2.ppf(0.99, shape_parameters[0]), 100)
ax1.plot(x, chi2.pdf(x, *shape_parameters), 
        'r-', lw=5, alpha=0.6, label='chi2 pdf')

rv = chi2(*shape_parameters)
#ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

