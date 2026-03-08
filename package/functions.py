import numpy as np
import time


def functiontest(N=10):
    return np.arange(N)


def approx_10s_function():
    count = 0
    start = time.time()
    x = np.random.rand(1000, 1000)

    # Keep doing some matrix multiplication until ~10 seconds pass
    while time.time() - start < 10:
        count+=1
        x = np.dot(x, x) * 0.000001

    return count