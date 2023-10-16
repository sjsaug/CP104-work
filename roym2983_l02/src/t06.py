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
    pr = int(input())
    num = int(input())
    inst = float(input())
    inst_rate = (inst/100)

    monthly = pr*(((inst_rate / 12)*((1 + inst_rate / 12)**(num*12))) / (((1 + inst_rate / 12)**(num*12)) - 1))
    print(f'The monthly payments are : ${monthly}')

main()