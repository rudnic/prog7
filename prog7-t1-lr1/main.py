import math
import timeit

# TODO сделать тесты, вынести timeit в cli

def integrate(f, a, b, n=10**7):

    h = (b - a) / n
    x = a
    s = f(x) - f(b)

    for k in range(1, n+1):

        x += h
        s += 2 * f(x)
    
    result = (h / 2) * s
    print(round(result, 8))

if __name__ == "__main__":
    f1 = lambda x: math.sin(x) + 3
    # t = timeit.timeit('integrate(lambda x: math.sin(x) + 3, 0, 15)', setup = 'from __main__ import integrate, math', number=1)
    print(t)