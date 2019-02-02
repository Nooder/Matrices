from random import randint

def generate_matrix(num_rows, num_cols):
    # Check for invalid input
    if len(str(num_rows)) < 1 or len(str(num_cols)) < 1:
        print("Invalid input dimensions.")
        return

    # Create num_rows x num_cols matrix and fill it in with random number from 0-99
    matrix = [[randint(-99,99) for c in range(int(num_cols))] for r in range(int(num_rows))]
    return matrix