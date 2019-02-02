def transpose_matrix(A):
    num_rows_in_A = len(A)
    num_cols_in_A = len(A[0])

    # Create empty transpose matrix of A: num_cols_in_A x num_rows_in_A
    transpose_A = [[0 for r in range(num_rows_in_A)] for c in range(num_cols_in_A)]

    for row_index_in_A in range(num_rows_in_A):
        for col_index_in_A in range(num_cols_in_A):
            transpose_A[col_index_in_A][row_index_in_A] = A[row_index_in_A][col_index_in_A]
    
    return transpose_A