import numpy as np
import matplotlib.pyplot as plt

# Change of coordinate basis
basis_a = [
    [2, 0],
    [1, 1]
]
basis_b = [
    [0, 3],
    [-2, -1]
]
point = [1, -2]

''' First plot each basis as 2 vectors
plt.quiver(0, 0, basis_a[0][0], basis_a[1][0], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, basis_a[0][1], basis_a[1][1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, basis_b[0][0], basis_b[1][0], angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, basis_b[0][1], basis_b[1][1], angles='xy', scale_units='xy', scale=1, color='b')
plt.title('Basis A (red) and Basis B (blue)')
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.show()
'''

# Convert the point which is in basis_a to basis_b

# First to standard basis
standard_basis = np.dot(basis_a, point)

# Then to basis_b
basis_b_inv = np.linalg.inv(basis_b)
point_b = np.dot(basis_b_inv, standard_basis)

# Plot the point in both bases
plt.quiver(0, 0, basis_a[0][0], basis_a[1][0], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, basis_a[0][1], basis_a[1][1], angles='xy', scale_units='xy', scale=1, color='r')
plt.quiver(0, 0, basis_b[0][0], basis_b[1][0], angles='xy', scale_units='xy', scale=1, color='b')
plt.quiver(0, 0, basis_b[0][1], basis_b[1][1], angles='xy', scale_units='xy', scale=1, color='b')

plt.quiver(0, 0, point[0], point[1], angles='xy', scale_units='xy', scale=1, color='g')
plt.quiver(0, 0, point_b[0], point_b[1], angles='xy', scale_units='xy', scale=1, color='y')
plt.title('Point in Basis A (green) and Basis B (yellow)')

plt.xlim(-5, 5)
plt.ylim(-5, 5)

plt.grid()
plt.show()

# Print the point in both bases
print(f"Point in basis A: {point}")
print(f"Point in basis B: {point_b}")
