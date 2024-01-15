import numpy as np

from random_svd import svd

movieRatings = np.array([
    [2, 5, 3],
    [1, 2, 1],
    [4, 1, 1],
    [3, 5, 2],
    [5, 3, 1],
    [4, 5, 5],
    [2, 4, 2],
    [2, 2, 5],
], dtype='float64')

    # v1 = svd_1d(movieRatings)
    # print(v1)

theSVD = svd(movieRatings)

print(theSVD)

theSVD2 = (np.linalg.svd(movieRatings))
print(theSVD2)