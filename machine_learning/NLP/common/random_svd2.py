import numpy as np
from scipy.linalg import svd

def random_svd(A, num_components, n_iter=10):

    random_matrix = np.random.randn(A.shape[1], num_components)

    for _ in range(n_iter):
        Q = np.dot(A, random_matrix)

        Q, _ = np.linalg.qr(Q)

        random_matrix = np.dot(A.T, Q)

        random_matrix, _ = np.linalg.qr(random_matrix)

    B = np.dot(Q.T, A)
    Uhat, s, Vt = svd(B, full_matrices=False)
    U = np.dot(Q, Uhat)

    return U[:, :num_components], s[:num_components], Vt[:num_components, :]
