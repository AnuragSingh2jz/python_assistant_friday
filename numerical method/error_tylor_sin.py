import math
import math

def maclaurin_sin(x, n_range):
    return sum(((-1)**n * x**(2*n + 1)) / math.factorial(2*n + 1)
               for n in range(n_range))

x = math.pi/4


term_list = [2,4,6,8]
print("truncation error analysis for e^x \n")
true_val = math.sin(x)
for n in term_list:
    approx = maclaurin_sin(x,n)
    error = abs(true_val - approx)
    print(f"{n} , approx value = {approx:.10f} , error value = {error}")
