"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-09-11"
-------------------------------------------------------
"""
# Imports

# Constants

def main():
    lg_dogs = int(input())
    sm_dogs = int(input())
    LG_PRICE = 75.00
    SM_PRICE = 50.00
    total = (lg_dogs * LG_PRICE) + (sm_dogs * SM_PRICE)
    print(total)

main()