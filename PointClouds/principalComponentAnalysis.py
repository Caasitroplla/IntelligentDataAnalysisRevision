import numpy as np

point_cloud = np.random.rand(100, 2) * 100

# Standardize the data this makes the mean 0 and the variance 1
point_cloud -= np.mean(point_cloud, axis=0)
point_cloud /= np.std(point_cloud, axis=0)

# Calculate the covariance matrix
covariance_matrix = np.cov(point_cloud, rowvar=False)

# Calculate the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(covariance_matrix)

# Sort the eigenvalues and eigenvectors
sorted_indices = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[sorted_indices]

k = 1  # Number of principal components
eigenvectors = eigenvectors[:, sorted_indices][:, :k]

# Project the data onto the new feature space
projected_data = point_cloud @ eigenvectors
# Reconstruct the data
reconstructed_data = projected_data @ eigenvectors.T
# Calculate the reconstruction error
reconstruction_error = np.mean(np.linalg.norm(point_cloud - reconstructed_data, axis=1))

print("Original data shape:", point_cloud.shape)
print("Projected data shape:", projected_data.shape)
print("Reconstructed data shape:", reconstructed_data.shape)
print("Reconstruction error:", reconstruction_error)

# Visualize the original and reconstructed data
import matplotlib.pyplot as plt

plt.scatter(point_cloud[:, 0], point_cloud[:, 1], label='Original Data', alpha=0.5)
plt.scatter(reconstructed_data[:, 0], reconstructed_data[:, 1], label='Reconstructed Data', alpha=0.5)
plt.title('PCA Reconstruction')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.axis('equal')
plt.show()
