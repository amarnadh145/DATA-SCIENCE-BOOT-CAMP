import numpy as np

A = np.array([[1, 5, 7], [3, 9, 10]])
B = np.array([[2, 5, 7], [3, 8, 12]])

common = np.intersect1d(A, B)
print(common)
