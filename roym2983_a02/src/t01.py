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

total_sales = int(input("Enter the total sales: "))

ANNUAL_TAX = 0.1850
ANNUAL_TAX_PERCENT = ANNUAL_TAX * 100

tax = total_sales * ANNUAL_TAX

print(f"Projected Tax Report \n -------------------------- \n Total sales: $ {total_sales} \n Annual Tax: % {ANNUAL_TAX_PERCENT} \n -------------------------- \n Tax: $ {tax}")