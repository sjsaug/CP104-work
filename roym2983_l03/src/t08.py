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
    print("Material     Cubic Metres")
    print(f"Dirt         {amt_dirt:>5.1f}")
    print(f"Gravel       {amt_gravel:>5.1f}")
    print(f"Sand         {amt_sand:>5.1f}")
    print(f"Total        {total:>5.1f}")

main()