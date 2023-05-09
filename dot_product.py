import numpy as np

# A 3x3 matrix.
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# A 3x1 column matrix.
v = np.array([2, 3, 4]).reshape(-1, 1)  # reshape the 1D array into a 2D column vector.

# Calculate the dot product of A and v.
Av = A.dot(v)

print(Av)
