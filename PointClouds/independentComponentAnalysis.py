import numpy as np
from sklearn.decomposition import FastICA
import matplotlib.pyplot as plt

point_cloud = np.random.rand(100, 2) * 100

point_cloud_centered = point_cloud - np.mean(point_cloud, axis=0)

# Creating new set of axis maximising the independence of each axis
ica = FastICA(n_components=2)
point_cloud_transformed = ica.fit_transform(point_cloud_centered)

assert point_cloud_transformed != None

# Plotting the original and transformed point clouds
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.scatter(point_cloud[:, 0], point_cloud[:, 1], alpha=0.5)
plt.title('Original Point Cloud')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.subplot(1, 2, 2)
plt.scatter(point_cloud_transformed[:, 0], point_cloud_transformed[:, 1], alpha=0.5)
plt.title('Transformed Point Cloud')
plt.xlabel('Independent Component 1')
plt.ylabel('Independent Component 2')
plt.tight_layout()
plt.show()
