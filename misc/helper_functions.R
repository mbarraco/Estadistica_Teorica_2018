



sample_estimator = function(distribution_func,
                            distribution_n_values,
                            estimator_func, 
                            estimator_n_values) {
    #  Calculate <estimator_func> a number of times defined by user. User can specify
    #  both the estimator function and the distribution the samples are
    #  drawed from.
    #
    #  Args:
    #       distrbution_func (function): the distribution generating function. Must have <n> (sample 
    #       number as th sole argument 
    #       distribution_n_values (vector): sample number for the distribution
    #       estimator_func (function): the estimating function, must have the sample as the sole
    #       argument
    #       estimator_n_values (int): sample number for the estimator
    #
    # Returns:
    #       matrix: a matrix whose columns are the samples of the estimator for each
    #       of the distribution sample sizes defined in <distribution_n_values>
    
    estimator_samples = matrix(NA,
                               nrow=estimator_n_values,     
                               ncol=length(sample_sizes),
                               byrow = TRUE)   
    for (i in 1:length(distribution_n_values)) {
        n = distribution_n_values[i]
        estimator = c()
        set.seed(1)
        for (repetition in 1:estimator_n_values) {
            sample = distribution_func(n)
            estimator = c(estimator, estimator_func(sample))
        } 
        estimator_samples[, i] = t(as.matrix(estimator))
    }
    return (estimator_samples)
}