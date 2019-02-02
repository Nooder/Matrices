def multiply_matrices(A, B):
    num_rows_A = len(A)
    num_cols_A = len(A[0])
    num_rows_B = len(B)
    num_cols_B = len(B[0])

    # Check to make sure dimensions are correct for matrix-matrix multiplication
    if num_cols_A != num_rows_B:
        print("Cannot multiply matrices. Number of columns in A does not match number of rows in B.")
        return

    # Initialize result matrix with proper dimensions: num_rows_A x num_cols B
    result_matrix = [[0 for r in range(num_rows_A)] for c in range(num_cols_B)]

    # Perform multiplication cell by cell
    for row_index_in_A in range(num_rows_A):
        for col_index_in_B in range(num_cols_B):
            multiplication_result = 0
            for multiplication_index in range(num_cols_A):
                multiplication_result += A[row_index_in_A][multiplication_index] * B[multiplication_index][col_index_in_B]
            result_matrix[row_index_in_A][col_index_in_B] = multiplication_result

    return result_matrix