from sys import maxsize

def largest_matrix_member(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = -maxsize

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if matrix[row_index][col_index] > result:
                result = matrix[row_index][col_index]

    return result

def smallest_matrix_member(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    result = maxsize

    for row_index in range(num_rows):
        for col_index in range(num_cols):
            if matrix[row_index][col_index] < result:
                result = matrix[row_index][col_index]

    return result