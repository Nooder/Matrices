from largest_smallest_matrix_members import largest_matrix_member

def print_matrix(matrix):
    # Get # of rows and columns
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Get largest and smallest members to calculate cell printing width
    largest_width = len(str(largest_matrix_member(matrix)))
    top_bottom_border_width = num_cols * (largest_width + 2) + (num_cols + 1)

    # Print top boundary of matrix
    # Formula: Number of columns * (Longest cell member length + 2) + (Number of columns + 1)
    print("-" * top_bottom_border_width)
    for r in range(int(num_rows)):
        # Print left boundary of matrix for this row
        print("|", end="")
        for c in range(int(num_cols)):
            # Print each column member of the row
            # Formula for left-hand spacing: longest cell member length - current cell member length + 1
            right_hand_spacing = largest_width - len(str(matrix[r][c])) + 1
            print(" " * right_hand_spacing + str(matrix[r][c]) + " |" , end = "")
        # Print a new line for the next row's columns
        print("")
    # Print bottom boundary of matrix
    print("-" * top_bottom_border_width)