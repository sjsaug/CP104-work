"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports

# Constants

date = int(input("Enter a date in the format YYYYMMDD: "))
year = date // 10000
month = (date // 100) % 100
day = date % 100
formatted_date = f"{year}/{month:02}/{day:02}"
print(f"The reformatted date: {formatted_date}")