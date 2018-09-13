#  Clear workspace and close figures
rm(list = ls())
graphics.off()
# set.seed(1)
#...................................
library(functional)

source('~/code/Estadistica_Teorica_2018/misc/helper_functions.R')


#...................................


prob = 0.8 # Binomial prob
sample_sizes = c(1e2, 1e3, 5e3) # AKA: n
N_estimator = 10000 #  Number of times an estimator will be calculated

#
#
# Unbiased AND consistent estimator for Binomial (n=1, p=0.6) distro
#
#
estimator_func = mean

unbiased_consistent = sample_estimator(
    distribution_func=Curry(rbinom, size=1, prob=prob),
    distribution_n_values=sample_sizes,
    estimator_func=estimator_func,
    estimator_n_values=N_estimator
)
#
#
# Biased AND consistent estimator for Binomial (n=1, p=0.6) distro
#
#
estimator_func = function(samples) {mean(samples) + (1/length(samples)) }


biased_consistent = sample_estimator(
    distribution_func=Curry(rbinom, size=1, prob=prob),
    distribution_n_values=sample_sizes,
    estimator_func=estimator_func,
    estimator_n_values=N_estimator
) 

#
#
# Figures
#
#
ylim=c(.6, 1)

boxplot(
    unbiased_consistent,
    ylim=ylim,
    names=sample_sizes,
    main="Unbiased and consistent"
)
abline(a=0,b=3, h=prob, col='green')

boxplot(
    biased_consistent,
    ylim=ylim,
    main="Biased and consistent",
    names=sample_sizes,
)
abline(a=0,b=3, h=prob, col='green')
