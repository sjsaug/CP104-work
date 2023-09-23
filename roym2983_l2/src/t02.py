"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-09-22"
-------------------------------------------------------
"""
# Imports

# Constants

def main():
    WATER = 32
    fahrenheit = int(input())
    celcius = (fahrenheit - WATER) * (5/9)
    print(int(celcius))

main()