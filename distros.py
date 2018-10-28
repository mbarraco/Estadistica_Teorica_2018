import scipy.stats as st
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')


#%% Chi squared

fig, (ax1, ax2) = plt.subplots(2, 1)
shape_parameters = [55]
x = np.linspace(st.chi2.ppf(0.01, shape_parameters[0]), 
                st.chi2.ppf(0.99, shape_parameters[0]), 
                100)
ax1.plot(x, chi2.pdf(x, *shape_parameters), 
        'r-', lw=5, alpha=0.6, label='chi2 pdf')

rv = st.chi2(*shape_parameters)
#ax.plot(x, rv.pdf(x), 'k-', lw=2, label='frozen pdf')

#%% Poisson
plt.close('all')

fig, axs = plt.subplots(3, 1)
lambdas = [1, 5, 10]
plot_index = 0
for l in lambdas:
    dist = st.poisson(l)
    x = np.arange(-1, 30)
    axs[plot_index].plot(x, dist.pmf(x), lw=.5, color='black',
             label=r'$\mu=%i$' % l, linestyle='steps-mid')

    plt.xlabel('$x$')
    plt.ylabel(r'$p(x|\mu)$')
    plt.title('Poisson Distribution')
    plt.show()
    plot_index += 1
