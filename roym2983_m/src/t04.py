"""
-------------------------------------------------------
Midterm B Task 4 Testing
-------------------------------------------------------
Author: August Roy Mclaughlin
ID:     169052983
Email:  roym2983@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports
# your imports here
from t04_functions import get_it

# your code here
response = input("Enter a response (Y/N): ")
classification = get_it(response)
print(f"Classified : {response} as {classification}")