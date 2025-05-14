import spread
import numpy as np
import matplotlib.pyplot as plt


def pca(point_cloud, principal_components=2):
    # Convert point cloud to numpy array
    point_cloud = np.array(point_cloud)

    # Calculate covariance matrix (and zero mean the data)
    mean_vector = np.mean(point_cloud, axis=0)
    centered_data = point_cloud - mean_vector
    size = centered_data.shape[0]
    covariance_matrix = np.dot(centered_data.T, centered_data) / (size - 1)

    # Eigen decomposition
    eigenvalues, eigenvectors = np.linalg.eigh(covariance_matrix)

    # Sort eigenvalues and eigenvectors
    sorted_indices = np.argsort(eigenvalues)[::-1]
    #sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # Select top k eigenvectors
    top_eigenvectors = sorted_eigenvectors[:, :principal_components]

    # Project data onto the new subspace
    projected_data = np.dot(centered_data, top_eigenvectors)

    # Reconstruct the data from the projection
    reconstructed_data = np.dot(projected_data, top_eigenvectors.T) + mean_vector

    # Calculate reconstruction error
    reconstruction_error = np.mean(np.linalg.norm(centered_data - reconstructed_data, axis=1))

    return projected_data, reconstructed_data, reconstruction_error


def graph(point_cloud, reconstructed_data):
    # Visualize the original and reconstructed data
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = zip(*point_cloud)
    x_rec, y_rec, z_rec = zip(*reconstructed_data)
    ax.scatter(x, y, z, label='Original Data', alpha=0.5)
    ax.scatter(x_rec, y_rec, z_rec, label='Reconstructed Data', alpha=0.5)
    ax.set_title('PCA Reconstruction')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    #ax.set_zlabel('Z-axis')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    print('\nTrended Data:')
    # Trended data generation
    point_cloud = spread.generate_trended_point_cloud(num_points=100, trend=0)
    # Perform pca
    projected_data, reconstructed_data, reconstruction_error = pca(point_cloud, principal_components=2)
    # Print results
    print("Original data shape:", np.array(point_cloud).shape)
    print("Projected data shape:", projected_data.shape)
    print("Reconstructed data shape:", reconstructed_data.shape)
    print("Reconstruction error:", reconstruction_error)
    # Graph the original and reconstructed data
    graph(point_cloud, reconstructed_data)
