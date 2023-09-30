"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-09-29"
-------------------------------------------------------
"""
# Imports

# Constants

def main():
    minutes = int(input("Enter number of minutes: "))
    days = minutes // (24 * 60)
    hours = (minutes % (24 * 60)) // 60
    minutes_2 = minutes % 60
    print(f"There are {days} days, {hours} hours and {minutes_2} minutes in {minutes}")

main()