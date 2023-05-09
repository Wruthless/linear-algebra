import numpy as np

# Computation of eigenvectors and eigenvalues identifies the
# directions of the greatest variance in the data. Dimensionality
# can be reduced by focusing on the important eigenvectors.

A = np.array([[1, 2], [2, 1]])

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvectors:\n", eigenvectors)
print("Eigenvalues:\n", eigenvalues)
