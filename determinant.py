def is_invertible(matrix):
    """Takes a matrix and returns True if the matrix is invertible, false otherwise.

    Assumes the matrix is square.
    """
    return get_determinant(matrix) != 0

def get_determinant(matrix):
    """Gets the determinant of a given matrix.

    Assumes the matrix is square.
    """
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        determinant = 0
        sign = 1
        for col, val in enumerate(matrix[0]):
            determinant += sign * val * get_determinant(get_submatrix(matrix, 0, col))
            sign *= -1

        return determinant


def get_submatrix(matrix, row, col):
    """Gets the submatrix of a matrix after a given row and col is removed.
    """
    # Remove the row first as it is easier.
    matrix = matrix[:row] + matrix[row + 1:]
    submatrix = [row[:col] + row[col + 1:] for row in matrix]
    return submatrix

done = False
matrix_str = []

print("Give me a square matrix to check if it is invertible. Use newline to divide the rows and space to divide the columns. Type q when you are done.\n")
while not done:
    user_input = input()
    if user_input.lower() == 'q':
        done = True
    else:
        matrix_str.append(user_input)

matrix = list(map(lambda s : list(map(int, s.split(" "))), matrix_str))

print(f'Determinant: {get_determinant(matrix)}')
