import numpy as np

A = np.array([[3, 2],
    [1, 3]])

# Eigen Decomposition

# Compute eigenvalue and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Diagonal matrix of eigenvalues
Lambda = np.diag(eigenvalues)

# Inverse of eigenvectors matrix
V_inv = np.linalg.inv(eigenvectors)

# Reconstruct A
A_reconstructed = eigenvectors @ Lambda @ V_inv

print("Original A:")
print(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)

print("\nReconstructed A:")
print(A_reconstructed)

# Check if close to original
print("\nIs reconstruction accurate?", np.allclose(A, A_reconstructed))
