from random import randint

def generate_matrix(num_rows, num_cols):
    # Create num_rows x num_cols matrix and fill it in with random number from 0-99
    matrix = [[randint(0,99) for c in range(int(num_cols))] for r in range(int(num_rows))]
    return matrix