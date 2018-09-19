library(functional)
#  Clear workspace and close figures
rm(list = ls())
graphics.off()
set.seed(1)
source('~/code/Estadistica_Teorica_2018/misc/helper_functions.R')

#
#  Estimators definition
#
moment_func = function(samples){ 2 * mean(samples) }

likelihood_func = function(samples){ max(samples) }

robust_func = function(samples){ 2 * median(samples) }

modified_likelihood_func = function(samples){ (6/5) * max(samples) }

#
#  Simulation
#

iterations = 1e3
sample_sizes = c(5)

estimator_analizer_func = Curry(
    sample_estimator,
    distribution_func = Curry(runif,min=0,max=1),
    distribution_n_values = sample_sizes,
    estimator_n_values = iterations
)
moments = estimator_analizer_func(moment_func)
likelihood = estimator_analizer_func(likelihood_func)
robust = estimator_analizer_func(robust_func)
modified_likelihood = estimator_analizer_func(modified_likelihood_func)

estimator_set = cbind(moments, likelihood, robust, modified_likelihood)

boxplot(
    estimator_set,
    # ylim=ylim,
    names=c('moments', 'likelihood', 'robust', 'mod_likelihood'),
    main="Uniform upper limit estimator"
)
abline(h=1, col='green')
