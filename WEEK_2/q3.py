import numpy as np

A = np.array([[1, 5, 7], [3, 9, 10]])

range_A = A[np.where((A >= 5) & (A <= 10))]
print(range_A)
