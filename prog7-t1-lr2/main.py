import math
import concurrent.futures as ftres
from functools import partial
import timeit

def integrate(f, a, b, n=10**6):
  step = (b-a) / n
  x=a
  s=f(x)-f(b)
  for k in range(1, n+1):
    x+=step
    s+=2*f(x)
  result = (step/2)*s
  return result

  
def foo(f,a,b,n_jobs):
    executor = ftres.ThreadPoolExecutor(max_workers=n_jobs)
    # future_result = executor.submit(identity,10)
    # ai, bi = 0, 0
    step = (b - a) / n_jobs

    fs = [(a + i * step, a + (i + 1) * step) for i in range(n_jobs)]
    # print(step, fs, "\n")

    
    spawn_lst = []
    for i in fs:
        spawn = partial(executor.submit, integrate, f, i[0], i[1])
        spawn_lst.append(spawn)

    # # TODO # 2
    res = []
    for f in spawn_lst:
        res.append(f())

    # print(res)

    s = [r.result() for r in ftres.as_completed(res)]
    print(sum(s))
    # print(res)


# t = timeit.timeit('foo(lambda f:math.sin(f)+3, 0, 15, 4)', setup="from __main__ import foo, math", number = 1)
# print(t)

# TODO Вынести timeit в cli
# Сделать отчет по времени
