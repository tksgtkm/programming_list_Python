import numpy as np
from numpy.linalg import norm

from random import normalvariate
from math import sqrt

def random_unit_vector(n):
    unnormalized = [normalvariate(0, 1) for _ in range(n)]
    the_norm = sqrt(sum(x * x for x in unnormalized))
    return [x / the_norm for x in unnormalized]

def svd_1d(A, eps=1e-10):
    n, m = A.shape
    x = random_unit_vector(min(n, m))
    last_V = None
    current_V = x

    if n > m:
        B = np.dot(A.T, A)
    else:
        B = np.dot(A, A.T)

    iterations = 0
    while True:
        iterations += 1
        last_V = current_V
        current_V = np.dot(B, last_V)
        current_V = current_V / norm(current_V)

        if abs(np.dot(current_V, last_V)) > 1 - eps:
            print("converged in {} iterations".format(iterations))
            return current_V
        
def svd(A, k=None, eps=1e-10):
    A = np.array(A, dtype=float)
    n, m = A.shape
    svd_so_far = []
    if k is None:
        k = min(n, m)

    for i in range(k):
        matrix_for_1D = A.copy()

        for singular_value, u, v in svd_so_far[:i]:
            matrix_for_1D -= singular_value * np.outer(u, v)

        if n > m:
            v = svd_1d(matrix_for_1D, eps=eps)
            u_unnomalized = np.dot(A, v)
            sigma = norm(u_unnomalized)
            u = u_unnomalized / sigma
        else:
            u = svd_1d(matrix_for_1D, eps=eps)
            v_unnomarlized = np.dot(A.T, u)
            sigma = norm(v_unnomarlized)
            v = v_unnomarlized / sigma

        svd_so_far.append((sigma, u, v))

    singular_value, us, vs = [np.array(x) for x in zip(*svd_so_far)]

    return singular_value, us.T, vs