from matrix_printer import print_matrix
from matrix_generator import generate_matrix

print("--------MATRIX GENERATOR--------")
num_rows = 0
num_cols = 0

def get_dimensions():
    global num_cols
    global num_rows
    num_cols = input("Enter # of cols: ")
    num_rows = input("Enter # of rows: ")

get_dimensions()
matrix = generate_matrix(num_rows, num_cols)
print_matrix(matrix)