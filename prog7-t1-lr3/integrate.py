# f = sum , a = 0, b = 100, # 5050
# Thread-1  f = sum, a=0, b = 50 n_iter = 50
# Thread-2  f = sum, a=51, b = 100 n_iter = 50

def integrate(f, a, b, *, n_iter=1000):
    # TODO # 1
    return f(range(int(a), (int(b) + 1)))
