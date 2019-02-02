from matrix_printer import print_matrix
from matrix_generator import generate_matrix
from matrix_addition import add_matrices
from matrix_multiplication import multiply_matrices
from largest_smallest_matrix_members import largest_matrix_member, smallest_matrix_member

print("--------MATRIX GENERATOR--------")
num_rows = 0
num_cols = 0

def get_dimensions():
    global num_cols
    global num_rows
    num_cols = input("Enter # of cols: ")
    num_rows = input("Enter # of rows: ")

get_dimensions()
matrix_A = generate_matrix(num_rows, num_cols)
matrix_B = generate_matrix(num_rows, num_cols)
matrix_addition = add_matrices(matrix_A, matrix_B)
matrix_multiplication = multiply_matrices(matrix_A, matrix_B)
print("Matrix A:")
print_matrix(matrix_A)
print("Matrix B:")
print_matrix(matrix_B)
print("Matrix A + B:")
print_matrix(matrix_addition)
print("Matrix A * B:")
print_matrix(matrix_multiplication)