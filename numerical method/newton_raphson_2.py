import math

def f(x) : 
    return math.cos(x) - 3*x + 1
# define the derivatives cosx = 3x-1
def df(x):
    return -math.sin(x) - 3

def newton_raphson(x0, tol,max_iter = 100):
    x = x0
    
    print("Iter\t x_n\t\t f(x_n)\t\t Error ")
    print("-" * 55)
    
    for i in range(1,max_iter+1):
        x_new = x - f(x) / df(x)
        error = abs(x_new - x)
        
        print(f"{i}\t {x:.6f}\t {f(x):.6f}\t{error:.6f}")
        
        if error < tol:
            return x_new
        
        x = x_new
    return x

root = newton_raphson(3,1e-5)
print(f"\nAppropriate root : {root:.6f}")



