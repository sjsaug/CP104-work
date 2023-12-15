"""
-------------------------------------------------------
Exam Task 2 Function Definitions
-------------------------------------------------------
Author: August Roy Mclaughlin
ID:     169052983
Email:  roym2983@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Constants

# Your constants here


def rainfall():
    """
    -------------------------------------------------------
    Asks the user for daily rainfall (in mm) from the keyboard.
    The function stops asking for rainfall when the user enters -1.
    The function returns:
        the total number of dry days (rainfall lower than 4mm)
        the total number of damp days (rainfall 4mm - 8mm)
        the total number of wet days (rainfall greater than 8mm)
        the average rainfall for all days (rounded down)
    Do all inputs and calculations in integer.
    Use: dry_days, damp_days, wet_days, avg = rainfall()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​​​‌​‌‌​​‌‌​‌‌‌:
        dry_days - number of dry days (int)
        damp_days - number of damp days (int)
        wet_days - number of wet days (int)
        avg - average rainfall of all days (int)
    -------------------------------------------------------
    """
    dry_days = 0
    damp_days = 0
    wet_days = 0
    DRY = 4
    DAMP = 8
    total_rainfall = 0
    rainfall = int(input("Rainfall mm (-1 to stop): "))
    while rainfall != -1:
        if rainfall < DRY:
            dry_days += 1
        elif rainfall < DAMP:
            damp_days += 1
        else:
            wet_days += 1
        total_rainfall += rainfall
        rainfall = int(input("Rainfall mm (-1 to stop): "))
    if dry_days == 0:
        avg = 0
    else:
        avg = total_rainfall // (dry_days + damp_days + wet_days)
    return dry_days, damp_days, wet_days, avg
