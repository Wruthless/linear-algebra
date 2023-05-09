import numpy as np

# The Transformation matrix.
# First row is subtracted from the second row to ensure rows are perpendicular.
T = np.array([[np.sqrt(2), -np.sqrt(2)], [np.sqrt(2), np.sqrt(2)]])

# A vector for the transformation matrix.
v = np.array([1, 1])

# Applying the transformation.
# dot() performs matrix multiplication between the matrix T, and the vector v
# This applies the transformation to the vector.
Tv = T.dot(v)

# Printing the original vector and the transformed matrix.
print("Original vector: ", v)
print("Transformed vector: ", Tv)
