from random import randint

def generate_matrix(num_rows, num_cols):
    # Create num_rows x num_cols matrix and fill it in with random number from 0-9
    matrix = [[str(randint(0,9)) for r in range(int(num_cols))] for c in range(int(num_rows))]
    return matrix