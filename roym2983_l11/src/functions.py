"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-12-01"
-------------------------------------------------------
"""
# Imports

# Constants

def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - the type of values in matrix (str)
    Returns:
        None
    -------------------------------------------------------
    """
    print("   ", end="")
    for i in range(len(matrix[0])):
        print(f"{i:6}", end="")
    print()

    for i, row in enumerate(matrix):
        print(f"{i:2}", end=" ")
        for value in row:
            if value_type == 'float':
                print(f"{value:6.2f}", end="")
            elif value_type == 'int':
                print(f"{value:6}", end="")
        print()
    return

def print_matrix_char(matrix):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list of strings in a formatted table.
    Prints row and column headings.
    Use: print_matrix_char(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of strings (2D list)
    Returns:
        None.
    -------------------------------------------------------
    """
    # Print column headings
    h1 = "    "
    for col in range(len(matrix[0])):
        h1 += f"{col: >4}"
    print(h1)

    # Print matrix content
    for row in range(len(matrix)):
        row_string = f"{row: >2}  "
        for col in range(len(matrix[0])):
            row_string += f"{matrix[row][col]: >4}"
        print(row_string)
        
    return


def matrix_stats(matrix):
    """
    -------------------------------------------------------
    Returns statistics on a 2D list.
		Use: smallest, largest, total, average = matrix_stats(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list of float/int)
    Returns:
        smallest - the smallest number in matrix (float/int)
        largest - the largest number in matrix (float/int)
        total - the total of the numbers in matrix (float/int)
        average - the average of numbers in matrix (float/int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    total = 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
            if matrix[i][j] > largest:
                largest = matrix[i][j]
            total += matrix[i][j]
            count += 1
    average = total / count
    return smallest, largest, total, average

def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """
    smallest = matrix[0][0]
    largest = matrix[0][0]
    s_loc = [0, 0]
    l_loc = [0, 0]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < smallest:
                smallest = matrix[i][j]
                s_loc[0] = i
                s_loc[1] = j
            if matrix[i][j] > largest:
                largest = matrix[i][j]
                l_loc[0] = i
                l_loc[1] = j
    return s_loc, l_loc

def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    transposed = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    return transposed
