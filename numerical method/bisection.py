import math
from decimal import Decimal
#define the function
def f(x):
    return x**4 -32
#Bisection method with iteration table
def bisetion(a,b,tol):
    if f(a)*f(b)>=0:
        print("Bisection method fails.")
        return None
    
    iteration=1

    #Table header
    print("Iteration\t a\t\t b\t\t c\t\t f(c)\t\t Error")
    print("-"*75)

    while (b-a) / 2 > tol:
        c=(a+b)/2
        error=(b-a)/2

        #print Iteration values
        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")  #\t for space
        
        if f(c)==0:
            return c
        elif f(a)*f(c)<0:
            b=c
        else:
            a=c

        iteration+=1

    return (a+b)/2
#Input interval and tolerance
root=bisetion(2,3,1e-4)
print("\nApproximate root:",root)