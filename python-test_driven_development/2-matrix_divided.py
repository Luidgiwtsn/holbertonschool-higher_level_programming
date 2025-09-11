
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix of integers or floats.
        div (int or float): The number to divide each element by.

    Returns:
        list of lists: A new matrix with each element divided and rounded
                       to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of numbers,
                   if rows are not the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is zero.
    """

    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not all(isinstance(el, (int, float)) for el in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        new_matrix.append(new_row)
    return new_matrix
