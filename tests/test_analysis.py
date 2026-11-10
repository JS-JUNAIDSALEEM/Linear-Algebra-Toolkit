
import unittest
import numpy as np

from main import (
    convert_vector,
    convert_matrix,
    vector_addition,
    vector_subtraction,
    vector_dot_product,
    vector_magnitude,
    vector_normalization,
    matrix_addition,
    matrix_subtraction,
    matrix_multiplication,
    matrix_transpose,
    matrix_determinant,
    matrix_inverse,
    solve_equations
)


class TestVectorOperations(unittest.TestCase):

    def test_vector_addition(self):
        result = vector_addition([1, 2, 3], [4, 5, 6])
        np.testing.assert_array_equal(result, [5, 7, 9])

    def test_vector_subtraction(self):
        result = vector_subtraction([4, 5, 6], [1, 2, 3])
        np.testing.assert_array_equal(result, [3, 3, 3])

    def test_vector_dot_product(self):
        self.assertEqual(vector_dot_product([1, 2, 3], [4, 5, 6]), 32)

    def test_vector_magnitude(self):
        self.assertAlmostEqual(vector_magnitude([3, 4]), 5.0)

    def test_vector_normalization(self):
        result = vector_normalization([3, 4])
        np.testing.assert_allclose(result, [0.6, 0.8])

    def test_vector_with_wrong_dimensions(self):
        result = vector_addition([[1, 2], [3, 4]], [[1, 2], [3, 4]])
        self.assertIsNone(result)

    def test_vectors_with_different_sizes(self):
        result = vector_addition([1, 2], [1, 2, 3])
        self.assertIsNone(result)

    def test_zero_vector_normalization(self):
        result = vector_normalization([0, 0, 0])
        self.assertIsNone(result)

    def test_invalid_vector_input(self):
        result = convert_vector([1, "abc"])
        self.assertIsNone(result)


class TestMatrixOperations(unittest.TestCase):

    def test_matrix_addition(self):
        result = matrix_addition([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        np.testing.assert_array_equal(result, [[6, 8], [10, 12]])

    def test_matrix_subtraction(self):
        result = matrix_subtraction([[5, 6], [7, 8]], [[1, 2], [3, 4]])
        np.testing.assert_array_equal(result, [[4, 4], [4, 4]])

    def test_matrix_multiplication(self):
        result = matrix_multiplication([[1, 2]], [[3], [4]])
        np.testing.assert_array_equal(result, [[11]])

    def test_matrix_transpose(self):
        result = matrix_transpose([[1, 2, 3], [4, 5, 6]])
        np.testing.assert_array_equal(result, [[1, 4], [2, 5], [3, 6]])

    def test_matrix_determinant(self):
        result = matrix_determinant([[1, 2], [3, 4]])
        self.assertAlmostEqual(result, -2.0)

    def test_matrix_inverse(self):
        result = matrix_inverse([[1, 2], [3, 4]])
        np.testing.assert_allclose(result, [[-2, 1], [1.5, -0.5]])

    def test_matrix_with_wrong_dimensions(self):
        result = matrix_addition([1, 2], [1, 2])
        self.assertIsNone(result)

    def test_matrix_addition_with_different_shapes(self):
        result = matrix_addition([[1, 2]], [[1], [2]])
        self.assertIsNone(result)

    def test_determinant_of_non_square_matrix(self):
        result = matrix_determinant([[1, 2, 3], [4, 5, 6]])
        self.assertIsNone(result)

    def test_inverse_of_singular_matrix(self):
        result = matrix_inverse([[1, 2], [2, 4]])
        self.assertIsNone(result)

    def test_invalid_matrix_input(self):
        result = convert_matrix([[1, "abc"], [3, 4]])
        self.assertIsNone(result)


class TestLinearEquations(unittest.TestCase):

    def test_solve_equations(self):
        matrix = [[2, 1], [1, 3]]
        values = [5, 6]
        result = solve_equations(matrix, values)
        np.testing.assert_allclose(result, [1.8, 1.4])

    def test_solve_equations_with_wrong_values_size(self):
        result = solve_equations([[2, 1], [1, 3]], [5])
        self.assertIsNone(result)

    def test_solve_equations_with_non_square_matrix(self):
        result = solve_equations([[1, 2, 3], [4, 5, 6]], [1, 2])
        self.assertIsNone(result)

    def test_solve_equations_with_singular_matrix(self):
        result = solve_equations([[1, 2], [2, 4]], [3, 6])
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
