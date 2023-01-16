import cython
from cython.parallel import prange

def func(double x):
    return ((0.8*x**2 + 1)**(1/2))/(x + (1.5*x**2 + 2)**(1/2))

def integrate(f, a:cython.double, b: cython.double, long n_iter=10**6):
  cdef double step, x, s, result
  # k: cython.longint
  cdef int k
  step = (b-a) / n_iter
  x = a
  s = f(x) - f(b)
  for k in prange(n_iter, nogil=True):
    with gil:
      x += step
      s += 2 * f(x)
  result = (step / 2) * s
  return result