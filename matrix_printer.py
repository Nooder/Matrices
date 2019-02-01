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