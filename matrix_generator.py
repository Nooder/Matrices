from random import randint

print("--------MATRIX GENERATOR--------")
num_cols = input("Enter # of cols: ")
num_rows = input("Enter # of rows: ")

def generate_matrix(num_rows, num_cols):
    # Create num_rows x num_cols matrix and fill it in with random number from 0-9
    matrix = [[str(randint(0,9)) for r in range(int(num_cols))] for c in range(int(num_rows))]
    return matrix

def print_matrix(matrix):
    # Get # of rows and columns
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Print top boundary of matrix
    print("-" * int(num_cols)*4 + "-")
    for r in range(int(num_rows)):
        # Print left boundary of matrix for this row
        print("| ", end="")
        for c in range(int(num_cols)):
            # Print each column member of the row
            print(str(matrix[r][c]) + " | ", end = "")
        # Print a new line for the next row's columns
        print("")
    # Print bottom boundary of matrix
    print("-" * int(num_cols)*4 + "-")

matrix = generate_matrix(num_rows, num_cols)
print_matrix(matrix)