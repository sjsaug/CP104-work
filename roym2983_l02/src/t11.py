"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""
# Imports

# Constants

def main():
    PROFIT_PERCENTAGE = 18
    projected_sales = float(input())
    profit = projected_sales * (PROFIT_PERCENTAGE/100)
    print(f"The projected profit on sales of $ {projected_sales} is $ {profit}")

main()