library(functional)
#  Clear workspace and close figures
rm(list = ls())
graphics.off()
set.seed(1)
#
# 1)Generar n = 100 muestras de una viable aleatoria ε(λ) con λ = 1 y graficar su 
# distribucion empirica junto con su funcion de distribucion acumulada.
#
n = 100
lambda = 1
# Generamos una muestra de tamaño n con distribucion exponencial
log_transform = function (x, lambda){
    - log(1-x) / lambda
}
X = lapply(runif(n,0,1), 
           Curry(log_transform, lambda=lambda))
X = unlist(X)

x = seq(0,5,.01) 
plot(ecdf(X), col="green") 

lines(x, unlist(lapply(x, function(x) 1 - exp(-x))),
     ylim=c(0,1.1), pch=20, cex=.5, col="blue")

legend('bottomright', 
       legend=c("F.D.A"),  
       col=c("purple"),  
       pch=1)  
#
# 2) Calcular λ mediante el metodo de momentos y el EMV.
#
# i) Estimador de momentos, primero (f) y segundo.
first_m_e = function(X) {
    #First moment estimator. X is a sample vector
    1 / mean(X)
}
second_m_e = function(X) {
    #First moment estimator. X is a sample vector
    sqrt(2/mean(X))
}


fme = first_m_e(X)
sme = second_m_e(X)

#
#  Estimate lambda by means of Linear regression.
#
X = sort(X)
X_cum = ecdf(X)
X_cum = X_cum(X)
X_linear = log(1-X_cum)
plot(sort(X), X_linear)
model_linear = lm(formula=X_linear[1:99] ~ X[1:99] - 1)
prediction_linear = model_linear$coefficients[2]  * data_test$parent +
lse = model_linear$coefficients[1]

