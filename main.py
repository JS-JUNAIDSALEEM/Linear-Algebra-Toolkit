# Linear Algebra Toolkit

import numpy as np
import os

# Create output folder
os.makedirs("output", exist_ok=True)


# Input validation functions

def convert_vector(v, name="Vector"):

    try:
        v = np.asarray(v, dtype=float)

    except (TypeError, ValueError):
        print(name + " must contain numeric values.")
        return None

    if v.ndim != 1 or v.size == 0:
        print(name + " must be a valid non-empty vector.")
        return None

    if not np.all(np.isfinite(v)):
        print(name + " must contain valid numbers.")
        return None

    return v


def convert_matrix(m, name="Matrix"):

    try:
        m = np.asarray(m, dtype=float)

    except (TypeError, ValueError):
        print(name + " must contain numeric values.")
        return None

    if m.ndim != 2 or m.shape[0] == 0 or m.shape[1] == 0:
        print(name + " must be a valid non-empty matrix.")
        return None

    if not np.all(np.isfinite(m)):
        print(name + " must contain valid numbers.")
        return None

    return m


# Round results to 3 decimal places
def round_result(result):

    if result is None:
        return None

    return np.round(result, 3)


# 1. Vector Addition

def vector_addition(v1, v2):

    v1 = convert_vector(v1, "Vector 1")
    v2 = convert_vector(v2, "Vector 2")

    if v1 is None or v2 is None:
        return None

    if v1.shape != v2.shape:
        print("Vectors must have the same size.")
        return None

    return np.add(v1, v2)


# 2. Vector Subtraction

def vector_subtraction(v1, v2):

    v1 = convert_vector(v1, "Vector 1")
    v2 = convert_vector(v2, "Vector 2")

    if v1 is None or v2 is None:
        return None

    if v1.shape != v2.shape:
        print("Vectors must have the same size.")
        return None

    return np.subtract(v1, v2)


# 3. Vector Dot Product

def vector_dot_product(v1, v2):

    v1 = convert_vector(v1, "Vector 1")
    v2 = convert_vector(v2, "Vector 2")

    if v1 is None or v2 is None:
        return None

    if v1.shape != v2.shape:
        print("Vectors must have the same size.")
        return None

    return np.dot(v1, v2)


# 4. Vector Magnitude

def vector_magnitude(v):
    v = convert_vector(v)

    if v is None:
        return None

    return np.linalg.norm(v)


# 5. Vector Normalization

def vector_normalization(v):
    v = convert_vector(v)

    if v is None:
        return None

    magnitude = np.linalg.norm(v)

    if np.isclose(magnitude, 0):
        print("Zero vector cannot be normalized.")
        return None

    return v / magnitude


# 6. Matrix Addition

def matrix_addition(m1, m2):

    m1 = convert_matrix(m1, "Matrix 1")
    m2 = convert_matrix(m2, "Matrix 2")

    if m1 is None or m2 is None:
        return None

    if m1.shape != m2.shape:
        print("Matrices must have the same dimensions.")
        return None

    return np.add(m1, m2)


# 7. Matrix Subtraction

def matrix_subtraction(m1, m2):

    m1 = convert_matrix(m1, "Matrix 1")
    m2 = convert_matrix(m2, "Matrix 2")

    if m1 is None or m2 is None:
        return None

    if m1.shape != m2.shape:
        print("Matrices must have the same dimensions.")
        return None

    return np.subtract(m1, m2)


# 8. Matrix Multiplication

def matrix_multiplication(m1, m2):

    m1 = convert_matrix(m1, "Matrix 1")
    m2 = convert_matrix(m2, "Matrix 2")

    if m1 is None or m2 is None:
        return None

    if m1.shape[1] != m2.shape[0]:
        print("Matrix dimensions are not suitable for multiplication.")
        return None

    return np.dot(m1, m2)


# 9. Matrix Transpose

def matrix_transpose(m):

    m = convert_matrix(m)

    if m is None:
        return None

    return np.transpose(m)


# 10. Matrix Determinant

def matrix_determinant(m):

    m = convert_matrix(m)

    if m is None:
        return None

    if m.shape[0] != m.shape[1]:
        print("Determinant requires a square matrix.")
        return None

    return np.linalg.det(m)


# 11. Matrix Inverse

def matrix_inverse(m):

    m = convert_matrix(m)

    if m is None:
        return None

    if m.shape[0] != m.shape[1]:
        print("Inverse requires a square matrix.")
        return None

    if np.isclose(np.linalg.det(m), 0):
        print("Inverse does not exist for this matrix.")
        return None

    return np.linalg.inv(m)


# 12. Solve Linear Equations

def solve_equations(a, b):

    a = convert_matrix(a, "Coefficient matrix")
    b = convert_vector(b, "Values")

    if a is None or b is None:
        return None

    if a.shape[0] != a.shape[1]:
        print("Coefficient matrix must be square.")
        return None

    if a.shape[0] != b.size:
        print("Values must match the matrix dimensions.")
        return None

    if np.isclose(np.linalg.det(a), 0):
        print("Unique solution does not exist.")
        return None

    return np.linalg.solve(a, b)


# Get positive number from user

def get_positive_integer(message):

    while True:

        try:
            num = int(input(message))

            if num <= 0:
                print("Please enter a number greater than zero.")
                continue

            return num

        except ValueError:
            print("Please enter a valid whole number.")


# Get vector input from user

def get_vector_input(name):

    while True:

        values = input(
            "Enter " + name + " values separated by spaces: "
        ).strip().split()

        if not values:
            print("Vector cannot be empty. Please try again.")
            continue

        try:
            v = np.array([float(x) for x in values])

        except ValueError:
            print("Please enter numeric values only.")
            continue

        if not np.all(np.isfinite(v)):
            print("Please enter valid numbers only.")
            continue

        return v


# Get matrix input from user

def get_matrix_input(name):

    print("\nEnter details for " + name + ":")

    rows = get_positive_integer("Number of rows: ")
    cols = get_positive_integer("Number of columns: ")

    m = []

    for i in range(rows):

        while True:

            values = input(
                "Enter values for row " + str(i + 1) + " (space for separating elements): "
            ).strip().split()

            if len(values) != cols:
                print("Please enter exactly " + str(cols) + " values.")
                continue

            try:
                row = [float(x) for x in values]

            except ValueError:
                print("Please enter numeric values only.")
                continue

            if not np.all(np.isfinite(row)):
                print("Please enter valid numbers only.")
                continue

            m.append(row)
            break

    return np.array(m, dtype=float)


# Save results in a text file

def save_results(file_path, results):

    with open(file_path, "w") as file:

        for name, result in results.items():
            result = round_result(result)

            if result is None:
                result = "Not available - check the input values."

            file.write(name + ": " + str(result) + "\n")


# Vector Operations

def vector_operations():

    print("\n========== VECTOR OPERATIONS ==========")

    v1 = get_vector_input("Vector 1")
    v2 = get_vector_input("Vector 2")

    print("\nVector 1:", v1)
    print("Vector 2:", v2)

    results = {
        "Addition": vector_addition(v1, v2),
        "Subtraction": vector_subtraction(v1, v2),
        "Dot Product": vector_dot_product(v1, v2),
        "Vector 1 Magnitude": vector_magnitude(v1),
        "Vector 1 Normalization": vector_normalization(v1)
    }

    print("\nVector Results:")

    for name, result in results.items():
        print(name + ":", round_result(result))

    save_results("output/vector_results.txt", results)

    print("\nVector results saved in output/vector_results.txt")


# Matrix Operations

def matrix_operations():

    print("\n========== MATRIX OPERATIONS ==========")

    m1 = get_matrix_input("Matrix 1")
    m2 = get_matrix_input("Matrix 2")

    print("\nMatrix 1:")
    print(m1)

    print("\nMatrix 2:")
    print(m2)

    results = {
        "Addition": matrix_addition(m1, m2),
        "Subtraction": matrix_subtraction(m1, m2),
        "Multiplication": matrix_multiplication(m1, m2),
        "Transpose of Matrix 1": matrix_transpose(m1),
        "Determinant of Matrix 1": matrix_determinant(m1),
        "Inverse of Matrix 1": matrix_inverse(m1)
    }

    print("\nMatrix Results:")

    for name, result in results.items():
        print("\n" + name + ":")
        print(round_result(result))

    save_results("output/matrix_results.txt", results)

    print("\nMatrix results saved in output/matrix_results.txt")


# Solve Linear Equations

def equation_operations():

    print("\n========== LINEAR EQUATIONS ==========")
    print("Enter the coefficient matrix and values vector.")

    a = get_matrix_input("Coefficient Matrix")
    b = get_vector_input("right-hand-side values")

    result = solve_equations(a, b)

    print("\nEquation Solution:")

    if result is None:
        print("A unique solution could not be calculated.")
        results = {"Solution": None}

    else:
        print(round_result(result))
        results = {"Solution": result}

    save_results("output/equation_solution.txt", results)

    print("\nEquation result saved in output/equation_solution.txt")


# Main Menu
def main():

    while True:

        print("\n========== LINEAR ALGEBRA TOOLKIT ==========")
        print("1. Vector Operations")
        print("2. Matrix Operations")
        print("3. Solve Linear Equations")
        print("4. Exit")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            vector_operations()

        elif choice == "2":
            matrix_operations()

        elif choice == "3":
            equation_operations()

        elif choice == "4":
            print("\nThank you for using Linear Algebra Toolkit.")
            print("========== PROJECT COMPLETED ==========")
            break

        else:
            print("Invalid choice. Please select between 1 and 4.")


# Run Program
if __name__ == "__main__":
    main()
