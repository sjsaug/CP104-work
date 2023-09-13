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
    cost_of_meal = float(input())
    tax_rate = float(input())
    tip_rate = float(input())
    cost_floated = "%.2f" % cost_of_meal
    tax = "%.2f" % (cost_of_meal * (tax_rate/100))
    tip = "%.2f" % (cost_of_meal * (tip_rate/100))
    total = "%.2f" % (cost_of_meal + float(tax) + float(tip))
    print(f"Subtotal: $ {cost_floated}")
    print(f"Tax: $ {tax}")
    print(f"Tip: $ {tip}")
    print("------------------")
    print(f"Total: $ {total}")

main()