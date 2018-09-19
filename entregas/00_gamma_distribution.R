#  Clear workspace and close figures
rm(list = ls())
graphics.off()
# set.seed(1)
#...................................
library(functional)

source('~/code/Estadistica_Teorica_2018/misc/helper_functions.R')


#...................................


# Interesante ver outliers -> sample_sizes = c(10, 1e2, 1e3) # AKA: n.
sample_sizes = c(1e2, 5e2, 1e3, 5e3)
N_estimator = 1e4 #  Number of times an estimator will be calculated

#
#
# Unbiased AND consistent estimator for Binomial (n=1, p=0.6) distro
#
#

# Setup distribution: rgamma(n, shape, rate = 1, scale = 1/rate)
alpha = 4
lambda = 2
scale = 1 / lambda
shape = alpha
distribution_func = Curry(rgamma, scale=scale, shape=shape)
    
# Estimator functions


# Moment estimators
lambda_me_estimator_func = function(samples) {
    m2 = (samples %*% samples / length(samples))
    m1 = mean(samples)
    return(m1 / (m2 - m1^2))
}
alpha_me_estimator_func = function(samples) {
    m2 = (samples %*% samples / length(samples))
    m1 = mean(samples)
    return(m1^2 / (m2 - m1^2))
}

# Modified moment estimators
lambda_mme_estimator_func = function(samples) {
    m1 = mean(samples)
    r = mean(unlist(Map(function(x) {1/x}, samples)))^-1
    return(1/(m1-r))
}
alpha_mme_estimator_func = function(samples) {
    m1 = mean(samples)
    r = mean(unlist(Map(function(x) {1/x}, samples)))^-1
    return(m1/(m1-r))
}

estimator_analizer_func = Curry(sample_estimator,
    distribution_func=distribution_func,
    distribution_n_values=sample_sizes,
    estimator_n_values=N_estimator
)

alpha_me = estimator_analizer_func(alpha_me_estimator_func)
alpha_mme = estimator_analizer_func(alpha_mme_estimator_func)
lambda_me = estimator_analizer_func(lambda_me_estimator_func)
lambda_mme = estimator_analizer_func(lambda_mme_estimator_func)

#
#
# Figures
#
#
graphics.off()

ylim=c(.6, 1)

boxplot(
    alpha_me,
    # ylim=ylim,
    names=sample_sizes,
    main="Alpha moment estimator"
)
abline(h=alpha, col='green')

boxplot(
    alpha_mme,
    # ylim=ylim,
    names=sample_sizes,
    main="Alpha modified moment estimator"
)
abline(h=alpha, col='green')



# lambda
boxplot(
    lambda_me,
    # ylim=ylim,
    names=sample_sizes,
    main="Lambda moment estimator"
)
abline(h=lambda, col='pink')

boxplot(
    lambda_mme,
    # ylim=ylim,
    names=sample_sizes,
    main="Lambda modified moment estimator"
)
abline(h=lambda, col='pink')


