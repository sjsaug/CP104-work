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

pos_dgt_num = int(input("Enter a positive digit number: "))
tens = pos_dgt_num // 10
ones = pos_dgt_num % 10
diff = tens - ones
print(f"The difference of the digits of {pos_dgt_num} is {diff}")