from scipy.stats import gamma
import matplotlib.pyplot as plt




n = 1000
sample = gamma.rvs(1, size=n)

sample_mean_collection = [sum(gamma.rvs(1, size=n)) / n for i in range(1,10000)]



n, bins, patches = plt.hist(sample_mean_collection, 50, density=True, facecolor='g', alpha=0.75)
plt.title("Sample mean of Gamma")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
# plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()