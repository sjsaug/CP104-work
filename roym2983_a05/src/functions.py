"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-11-03"
-------------------------------------------------------
"""
# Imports

# Constants

def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """
    product = 1
    for i in range(1, number + 1):
        product *= i
    return product

def calories_treadmill(per_min, minutes):
    """
    -------------------------------------------------------
    Prints a table of the number of calories burned every five minutes.
    Use: calories_treadmill_table(per_min, minutes)
    -------------------------------------------------------
    Parameters:
        per_min - calories burned per minute (int > 0)
        minutes - total minutes run (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for time in range(5, minutes + 1, 5):
        calories = per_min * time
        print(f"Time: {time} min - Calories: {calories:.1f}")
    return


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints a pattern of hashes.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - number of rows (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        if i == 1:
            print(spaces + '#')
        else:
            spaces2 = ' ' * (2 * i - 3)
            print(spaces + '#' + spaces2 + '#')
    return


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """
    print("      ", end="")
    for i in range(start_num, stop_num + 1):
        print(f"{i:4}", end="")
    print("\n    " + "-" * 22)

    for height in range(start_num, stop_num + 1):
        print(f"{height:2} |", end="")
        for width in range(start_num, stop_num + 1):
            final = height * width
            print(f"{final:4}", end="")
        print()
                
    return

def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(start, start + increment * count, increment):
        total += i
    return total