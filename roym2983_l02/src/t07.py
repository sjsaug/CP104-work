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
    num_flyers = int(input())
    num_volunteers = int(input())
    
    flyers_per = num_flyers//num_volunteers
    remainder = num_flyers % num_volunteers
    
    print(flyers_per)
    print(remainder)
    
main()