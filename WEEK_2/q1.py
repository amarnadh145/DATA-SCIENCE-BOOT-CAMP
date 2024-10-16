import numpy as np

A = np.array([[1, 5, 7], [3, 9, 10]])
B = np.array([[2, 5, 7], [3, 8, 12]])

vertical_stack = np.vstack((A, B))
horizontal_stack = np.hstack((A, B))

print(vertical_stack)
print(horizontal_stack)
