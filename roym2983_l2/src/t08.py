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
    user_height = float(input())
    user_weight = float(input())
    upper_limit_bmi = int(input())
    bmi = "%.2f" % (user_weight / user_height**2)
    bmi_prime = "%.2f" % (float(bmi) / float(upper_limit_bmi))
    print(f"Body Mass Index (kg/m^2) = {bmi}")
    print(f"BMI Prime = {bmi_prime}")

main()