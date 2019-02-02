def add_matrices(A, B):
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])

    # Check to make sure dimensions match
    if num_rows_A != num_rows_B or num_cols_A != num_cols_B:
        print("Cannot add matrices that do not have matching dimensions.")
        return

    # Create empty return matrix with matching dimensions
    result_matrix = [[0 for c in range(num_cols_A)] for r in range(num_rows_A)]

    # Perform the addition of the two input matrices
    for row_index in range(num_rows_A):
        for col_index in range(num_cols_A):
            result_matrix[row_index][col_index] = A[row_index][col_index] + B[row_index][col_index]

    return result_matrix