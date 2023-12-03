"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-12-02"
-------------------------------------------------------
"""
# Imports
from functions import file_top
# Constants

file_handle = open("students.txt", "r", encoding="utf-8")
print(file_top(file_handle, 5))

file_handle.close()