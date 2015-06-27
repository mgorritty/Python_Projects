#Algoritmo de Biseccion
#(c) MAGP 2015 06 27

def f(x):
    return x**3+x**2-3*x-3

def bisec(x1,x2,TOL,func):
    while abs(x1-x2) > TOL:
        x3=(x1+x2)/2
        if func(x3)*func(x1) < 0:
            x2=x3
        else: 
            x1=x3
    print (x1,x2,x3)

bisec(1.,2.,1e-4,f)    
