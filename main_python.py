import timeit
import numpy as np
from scipy import signal

a = np.random.randn(10**5)
b = np.random.randn(10**5)

def test_np_convolve():
    return np.convolve(a, b)

def test_scipy_convolve():
    return signal.fftconvolve(a, b)

loop = 1

result_np = timeit.timeit('test_np_convolve()', globals=globals(), number=loop)
result_scipy = timeit.timeit('test_scipy_convolve()', globals=globals(), number=loop)
print(result_np / loop)
print(result_scipy / loop)