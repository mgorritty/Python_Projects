#Algoritmo de Biseccion
#(c) MAGP 2015 06 27
# Ref. Applied Numerical Analysis / Gerald & Wheatley

def f(x):
    return x**3+x**2-3*x-3

def bisec(x1,x2,TOL,func):
    n=0
    a=x1
    b=x2
    while abs(x1-x2) > TOL:
        x3=(x1+x2)/2.
        if func(x3)*func(x1) < 0:
            x2=x3
        else: 
            x1=x3
        n=n+1
    # devuelve x3, iteraciones y máximo error    
    return x3,n,abs(b-a)/2**n

print bisec(-0.5,-1.5,1e-4,f)    
