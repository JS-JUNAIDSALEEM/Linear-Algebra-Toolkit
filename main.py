import numpy as np
import os

# Create output folder
os.makedirs("output", exist_ok=True)


# 1. Vector addition
def vector_addition(vector1, vector2):

    if len(vector1) != len(vector2):
        print("Vectors must have the same size.")
        return None

    result = np.add(vector1, vector2)

    return result


# 2. Vector subtraction
def vector_subtraction(vector1, vector2):

    if len(vector1) != len(vector2):
        print("Vectors must have the same size.")
        return None

    result = np.subtract(vector1, vector2)

    return result


# 3. Vector dot product
def vector_dot_product(vector1, vector2):

    if len(vector1) != len(vector2):
        print("Vectors must have the same size.")
        return None

    result = np.dot(vector1, vector2)

    return result


# 4. Vector magnitude
def vector_magnitude(vector):

    result = np.linalg.norm(vector)

    return result


# 5. Vector normalization
def vector_normalization(vector):

    magnitude = np.linalg.norm(vector)

    if magnitude == 0:
        print("Zero vector cannot be normalized.")
        return None

    result = vector / magnitude

    return result


# 6. Matrix addition
def matrix_addition(matrix1, matrix2):

    if matrix1.shape != matrix2.shape:
        print("Matrices must have the same dimensions.")
        return None

    result = np.add(matrix1, matrix2)

    return result


# 7. Matrix subtraction
def matrix_subtraction(matrix1, matrix2):

    if matrix1.shape != matrix2.shape:
        print("Matrices must have the same dimensions.")
        return None

    result = np.subtract(matrix1, matrix2)

    return result


# 8. Matrix multiplication
def matrix_multiplication(matrix1, matrix2):

    if matrix1.shape[1] != matrix2.shape[0]:
        print("Matrix dimensions are not suitable for multiplication.")
        return None

    result = np.dot(matrix1, matrix2)

    return result


# 9. Matrix transpose
def matrix_transpose(matrix):

    result = np.transpose(matrix)

    return result


# 10. Matrix determinant
def matrix_determinant(matrix):

    if matrix.shape[0] != matrix.shape[1]:
        print("Determinant requires a square matrix.")
        return None

    result = np.linalg.det(matrix)

    return result


# 11. Matrix inverse
def matrix_inverse(matrix):

    if matrix.shape[0] != matrix.shape[1]:
        print("Inverse requires a square matrix.")
        return None

    determinant = np.linalg.det(matrix)

    if np.isclose(determinant, 0):
        print("Inverse does not exist for this matrix.")
        return None

    result = np.linalg.inv(matrix)

    return result


# 12. Solve linear equations
def solve_equations(matrix, values):

    if matrix.shape[0] != matrix.shape[1]:
        print("Coefficient matrix must be square.")
        return None

    if len(values) != matrix.shape[0]:
        print("Values must match the matrix dimensions.")
        return None

    if np.isclose(np.linalg.det(matrix), 0):
        print("Unique solution does not exist.")
        return None

    result = np.linalg.solve(matrix, values)

    return result


# Create vectors
vector1 = np.array([2, 4, 6])
vector2 = np.array([1, 3, 5])

# Create matrices
matrix1 = np.array([
    [1, 2],
    [3, 4]
])

matrix2 = np.array([
    [5, 6],
    [7, 8]
])


print("\n========== LINEAR ALGEBRA TOOLKIT ==========")


# Vector operations
print("\n========== VECTOR OPERATIONS ==========")

print("Vector 1:", vector1)
print("Vector 2:", vector2)

print("Vector Addition:", vector_addition(vector1, vector2))

print("Vector Subtraction:", vector_subtraction(vector1, vector2))

print("Dot Product:", vector_dot_product(vector1, vector2))

print("Vector 1 Magnitude:", vector_magnitude(vector1))

print("Vector 1 Normalization:", vector_normalization(vector1))


# Matrix operations
print("\n========== MATRIX OPERATIONS ==========")

print("\nMatrix 1:")
print(matrix1)

print("\nMatrix 2:")
print(matrix2)

print("\nMatrix Addition:")
print(matrix_addition(matrix1, matrix2))

print("\nMatrix Subtraction:")
print(matrix_subtraction(matrix1, matrix2))

print("\nMatrix Multiplication:")
print(matrix_multiplication(matrix1, matrix2))

print("\nMatrix Transpose:")
print(matrix_transpose(matrix1))

print("\nMatrix Determinant:")
print(matrix_determinant(matrix1))

print("\nMatrix Inverse:")
print(matrix_inverse(matrix1))


# Solve linear equations
print("\n========== LINEAR EQUATIONS ==========")

# Equations:
# 2x + y = 5
# x + 3y = 6

coefficient_matrix = np.array([
    [2, 1],
    [1, 3]
])

values = np.array([5, 6])

solution = solve_equations(coefficient_matrix, values)

print("Equation Solution:")
print(solution)


# Save vector results
vector_results = {
    "Addition": vector_addition(vector1, vector2),
    "Subtraction": vector_subtraction(vector1, vector2),
    "Dot_Product": vector_dot_product(vector1, vector2),
    "Magnitude": vector_magnitude(vector1)
}

with open("output/vector_results.txt", "w") as file:

    for operation, result in vector_results.items():
        file.write(operation + ": " + str(result) + "\n")


# Save matrix results
matrix_results = {
    "Addition": matrix_addition(matrix1, matrix2),
    "Subtraction": matrix_subtraction(matrix1, matrix2),
    "Multiplication": matrix_multiplication(matrix1, matrix2),
    "Transpose": matrix_transpose(matrix1),
    "Inverse": matrix_inverse(matrix1)
}

with open("output/matrix_results.txt", "w") as file:

    for operation, result in matrix_results.items():

        file.write(operation + ":\n")
        file.write(str(result) + "\n\n")


# Save equation solution
with open("output/equation_solution.txt", "w") as file:

    file.write("Solution of linear equations:\n")
    file.write(str(solution))


print("\n========== PROJECT COMPLETED ==========")
print("All results are saved in the output folder.")