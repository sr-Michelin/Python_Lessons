import time

import numpy as np
from numba import vectorize, cuda


@vectorize(['float32(float32, float32)'], target='cuda')
def Add(a, b):
    return a + b


def Add_cpu(a, b):
    return a + b


def main():
    N = 100000000

    A = np.ones(N, np.float32)
    B = np.ones(N, np.float32)

    start = time.time()
    C = Add(A, B)
    end = time.time() - start

    start_c = time.time()
    C = Add_cpu(A, B)
    end_c = time.time() - start_c

    print('time_GPU: ', end, 's')
    print('time_CPU: ', end_c, 's')


if __name__ == "__main__":
    main()
