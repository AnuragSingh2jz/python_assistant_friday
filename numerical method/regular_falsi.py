def f(x):
    return x**2 - 4

def regula_falsi(a, b, tol, max_iter=20):
    if f(a) * f(b) >= 0:
        print("Method fails, choose proper a and b")
        return None

    print("Iter\t a\t\t b\t\t c\t\t f(c)\t\t Error")
    print("-" * 75)

    c_old = a

    for i in range(1, max_iter + 1):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))
        error = abs(c - c_old)

        print(f"{i}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")

        if abs(f(c)) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return c

root = regula_falsi(0, 3, 1e-5)
print("\nApproximate Root:", root)