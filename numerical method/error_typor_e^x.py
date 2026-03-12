import math
def taylor_series(x,n_range):
    return sum(x**n / math.factorial(n) for n in range(n_range))
x = 1.0

term_list = [2,4,6,8]
print("truncation error analysis for e^x \n")
true_val = math.exp(x)
for n in term_list:
    approx = taylor_series(x,n)
    error = abs(true_val - approx)
    print(f"{n} , approx value = {approx:.10f} , error value = {error}")