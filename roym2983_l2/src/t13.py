"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-09-12"
-------------------------------------------------------
"""
# Imports

# Constants

def main():
    midterm = float(input())
    exam = float(input())
    MIDTERM_WEIGHT = 0.35
    EXAM_WEIGHT = 0.65
    final_grade = (midterm * MIDTERM_WEIGHT) + (exam * EXAM_WEIGHT)
    print(final_grade)
    
main()