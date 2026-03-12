from decimal import Decimal
import math

# true = 3.14159 
# approx = 3.14 
# abs_error = abs(true - approx)
# rel_error = abs_error / true
# print("absolute arror",abs_error)
# print("relaticve error",abs_error)
# round_error = abs_error - 0.00159
# print("round error",round_error)


# sum_val = Decimal(0.0)

# for i in range(10):
#     sum_val+=Decimal(0.1)

# print("sum after 1 to 10 ", sum_val)

x = math.pi /6 # pi/6 30 degree

true_val = math.sin(x)
approx_val2 = x - (x**3)/math.factorial(3)
approx_val3 = x - (x**3)/math.factorial(3) + (x**5)/math.factorial(5)
print(f"true val sin{x} = {true_val}")
print(f" approx val upto 2 terms {approx_val2}")

print(f"truncation error upto 2 terms {abs(true_val - approx_val2)}")
print(f"truncation error upto 3 terms {abs(true_val - approx_val3)}")














