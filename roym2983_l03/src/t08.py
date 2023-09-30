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
    amt_dirt = float(input("Enter amount of dirt (m^3): "))
    amt_gravel = float(input("Enter amount of gravel (m^3): "))
    amt_sand = float(input("Enter amount of sand (m^3): "))
    total = amt_dirt + amt_gravel + amt_sand
    cm = "Cubic Metres"
    print(f"{'Material':<20} {cm:>20}")
    print(f"{'Dirt':<20} {amt_dirt:>20.1f}")
    print(f"{'Gravel':<20} {amt_gravel:>20.1f}")
    print(f"{'Sand':<20} {amt_sand:>20.1f}")
    print(f"{'Total':<20} {total:>20.1f}")

main()