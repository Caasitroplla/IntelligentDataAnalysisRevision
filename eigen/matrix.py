import numpy
import random

def determinant(matrix: list[list[int]]) -> int:
    """
    Calculate the determinant of a square matrix.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for c in range(len(matrix)):
        det += ((-1) ** c) * matrix[0][c] * determinant([row[:c] + row[c + 1:] for row in matrix[1:]])
    return det


def inverse_matrix(matrix: list[list[int]]) -> list[list[int]]:
    """
    Calcualtes the inverse of a sqaure matrix using the adjugate method.
    """
    # Calculate the determinant
    det = determinant(matrix)

    # Calcualte the cofactor matrix
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            # Remove the i-th row and j-th column (where element is located)
            minor = [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]
            # Calculate the determinant of what remains
            cofactor_row.append(((-1) ** (i + j)) * determinant(minor))
        cofactor_matrix.append(cofactor_row)

    # Transpose the cofactor matrix -> adjugate matrix (rotate 90 degrees)
    adjugate_matrix = []
    for i in range(len(cofactor_matrix)):
        adjugate_row = []
        for j in range(len(cofactor_matrix)):
            adjugate_row.append(cofactor_matrix[j][i])
        adjugate_matrix.append(adjugate_row)

    # Now compute the inverse matrix = adjugate_matrix / det
    inverse_matrix = []
    for i in range(len(adjugate_matrix)):
        inverse_row = []
        for j in range(len(adjugate_matrix)):
            inverse_row.append(adjugate_matrix[i][j] / det)
        inverse_matrix.append(inverse_row)

    return inverse_matrix


def generate_random_matrix(size: int) -> list[list[int]]:
    """
    Generate a random square matrix of given size.
    """
    return [[random.randint(1, 10) for _ in range(size)] for _ in range(size)]

if __name__ == "__main__":
    # Example usage
    matrix = generate_random_matrix(10)

    print("Original Matrix:")
    for row in matrix:
        print(row)

    inv_matrix = inverse_matrix(matrix)
    print("\nInverse Matrix:")
    for row in inv_matrix:
        print(row)

    # Verify the result using numpy
    np_matrix = numpy.array(matrix)
    np_inv_matrix = numpy.linalg.inv(np_matrix)
    print("\nInverse Matrix using numpy:")
    for row in np_inv_matrix:
        print(row)

    print("\n" + "Identical" if  numpy.allclose(inv_matrix, np_inv_matrix) else "Not Identical")
