"""
-------------------------------------------------------
Testing for Task 7: line_lengths
-------------------------------------------------------
Author: August Roy Mclaughlin
ID:     169052983
Email:  roym2983@mylaurier.ca
__updated__ = "2023-12-14"
-------------------------------------------------------
"""
# Imports
from t07_functions import line_lengths
# your imports here

# Your code here
CASES = (
    ("source.txt", 16),
)

for case in CASES:
    f_in = open(case[0], "r", encoding="utf-8")
    f_short = open("f_short.txt", "a", encoding="utf-8")
    f_long = open("f_long.txt", "a", encoding="utf-8")
    n = case[1]
    short_lines, long_lines = line_lengths(f_in, f_short, f_long, n)
    f_in.close()
    f_short.close()
    f_long.close()
    print(f"Short lines : {short_lines}\nLong lines : {long_lines}")
    
"""
For this task, it said I should get 6 and 3 but my testing is giving me 5 and 3, and 5 and 3 makes sense.
On the t07 part it says that the testing should result in 6 and 3 but I only count 5 lines in the example f_short
I talked with a TA and he agreed with me on the fact that there were only 5 lines in the example f_short and instructed me to write this comment
"""