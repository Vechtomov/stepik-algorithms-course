import time

def timed(func, *args, n_iter = 10):
    acc = float("inf")
    for _ in range(n_iter):
        t0 = time.perf_counter()
        func(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc