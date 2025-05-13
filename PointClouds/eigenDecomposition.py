import numpy as np
# For all real values between 0 and 1 plot the eigen values of each pair

def getEigenValue(A, B):
    # Form the matrix
    M = np.array([[A, 0], [0, B]])

    # Calculate the eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(M)

    # Return the eigenvalues
    return eigenvalues

points = []
for i in range(-100, 100):
    for j in range(-100, 100):
        A = i / 100
        B = j / 100
        eigenvalues = getEigenValue(A, B)
        print(f"A: {A}, B: {B}, Eigenvalues: {eigenvalues}")
        points.append((A, B, eigenvalues[0], eigenvalues[1]))

# Plot the points
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], c='r', marker='o')
ax.set_xlabel('A')
ax.set_ylabel('B')
plt.show()
