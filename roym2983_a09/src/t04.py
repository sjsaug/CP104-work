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
from functions import line_numbering
# Constants


file_handle = open("wilde.txt", "r", encoding="utf-8")

print(line_numbering(file_handle))

file_handle.close()