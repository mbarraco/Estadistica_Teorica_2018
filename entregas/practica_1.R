library(functional)
#  Clear workspace and close figures
rm(list = ls())
graphics.off()
set.seed(1)
#
# 1)Generar n = 100 muestras de una viable aleatoria ε(λ) con λ = 1 y graficar su 
# distribucion empirica junto con su funcion de distribucion acumulada.
#
fme = c()
sme = c()
lse = c()


n = 100

for (i in 1:1000) {
    
    lambda = 1
    # Generamos una muestra de tamaño n con distribucion exponencial
        log_transform = function (x, lambda){
            - log(1-x) / lambda
        }
        X = lapply(runif(n,0,1), 
                   Curry(log_transform, lambda=lambda))
        X = unlist(X)
        
        x = seq(0,5,.01) 
    if(FALSE) {
        
        plot(ecdf(X), col="green") 
        lines(x, unlist(lapply(x, function(x) 1 - exp(-x))),
             ylim=c(0,1.1), pch=20, cex=.5, col="blue")
        
        legend('bottomright', 
               legend=c("F.D.A"),  
               col=c("purple"),  
               pch=1)  
    }
        
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
    
    # Save estimator values
    fme = c(fme, first_m_e(X))
    sme = c(sme, second_m_e(X))
    
    
    #
    # 3) Proponer un estimador de la función de distribucion acumulada
    # distinto al obtenido en a
    #
    #  Estimate lambda by means of Linear regression.
    T = X
    T = sort(T)
    X_cum = ecdf(T)
    X_cum = X_cum(T)[1:(n-1)]
    T= T[1:(n-1)]
    X_linear = log(1-X_cum)
    model_linear = lm(formula=X_linear~T - 1)
    lse = c(lse, - model_linear$coefficients[1])
    mse = mean(model_linear$residuals)
    
    # Figure: linear fit of cumulative probability function
    if(FALSE) {
        plot(
            sort(T), 
            X_linear,
            ylab="log(1-X)",
            xlab="x")
        lines(T, T * model_linear$coefficients, col="green")
        legend('topright', 
               legend="Ajuste",  
               col="green",  
               pch=1)
        
        # Figure: empirical cumulative function and estimators curves.
        plot(
            ecdf(T),
            col="green",
            xlab="x",
            ylab="Probabilidad acumulada",
            main="") 
        lines(x, unlist(lapply(x, function(x) 1 - exp(-x))),
              ylim=c(0,1.1), pch=20, cex=.5, col="red")
        lines(x, unlist(lapply(x, function(x) 1 - exp(-lse*x))),
              ylim=c(0,1.1), pch=20, cex=.5, col="blue")
        lines(x, unlist(lapply(x, function(x) 1 - exp(-fme*x))),
              ylim=c(0,1.1), pch=20, cex=.5, col="purple")
        
        colors = c("red", "blue", "purple")
        legend('bottomright', 
               legend=c("Teorica", "Cuadrados min.", "Primer momento"),  
               col=colors,  
               pch=1)  
    }
}