"""
-------------------------------------------------------
Exam Task 1 Function Definitions
-------------------------------------------------------
Author: August Roy Mclaughlin
ID:     169052983
Email:  roym2983@mylaurier.ca
__updated__ = "2023-08-25"
-------------------------------------------------------
"""


def even_avg(values):
    """
    -------------------------------------------------------
    Returns the average (integer, rounded down) of all even numbers
    in values. If values has no even numbers, the average is 0.
    Use: ea = even_avg(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of int)
    Returns‌​‌​​​​‌​​‌‌‌​​​‌​‌‌​​‌‌​‌‌‌:
        ea - the average of the even numbers in values (int)
    -------------------------------------------------------
    """
    even = []
    for i in values:
        if i % 2 == 0:
            even.append(i)
    if len(even) == 0:
        ea = 0
    else:
        ea = sum(even) // len(even)
    return ea
