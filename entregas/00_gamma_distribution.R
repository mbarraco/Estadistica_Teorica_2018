#  Clear workspace and close figures
rm(list = ls())
graphics.off()
# set.seed(1)
#...................................
library(functional)

source('~/code/Estadistica_Teorica_2018/misc/helper_functions.R')


#...................................


# Interesante ver outliers -> sample_sizes = c(10, 1e2, 1e3) # AKA: n.
sample_sizes = c(1e2, 1e3, 1e4)
N_estimator = 10000 #  Number of times an estimator will be calculated

#
#
# Unbiased AND consistent estimator for Binomial (n=1, p=0.6) distro
#
#

# Setup distribution: rgamma(n, shape, rate = 1, scale = 1/rate)
scale = 1 
shape = 1
distribution_func = Curry(rgamma, scale=scale, shape=shape)
    
# Estimator functions



lambda_fm_estimator = function(samples) {
    mean(samples) / (samples %*% samples / length(samples) - mean(samples))
}
    
    
lambda_fme = sample_estimator(
    distribution_func=distribution_func,
    distribution_n_values=sample_sizes,
    estimator_func=lambda_fm_estimator,
    estimator_n_values=N_estimator
)

#
#
# Figures
#
#

boxplot(
    lambda_fme,
)
# abline(a=0,b=3, h=prob, col='green')