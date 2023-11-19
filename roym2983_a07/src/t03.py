"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-11-18"
-------------------------------------------------------
"""
# Imports
from functions import get_indexes, list_positives
# Constants

numbers = list_positives()
indexes = get_indexes(numbers, 5)
print(indexes)