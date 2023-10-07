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

num_flyers = int(input("Number of flyers: "))
num_delivery_ppl = int(input("Number of delivery people: "))

flyers_per_person = num_flyers // num_delivery_ppl
leftover_flyers = num_flyers % num_delivery_ppl

print(f"Flyers per delivery person: {flyers_per_person}")
print(f"Flyers left over: {leftover_flyers}")