"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-10-29"
-------------------------------------------------------
"""
# Imports

# Constants

def url_categorize(url):
    """
    -------------------------------------------------------
    Returns whether a url represents a business, a non-profit, or another
    type of organization.
    Use: url_type = url_categorize(url)
    -------------------------------------------------------
    Parameters:
        url - the web address of the organization (str)
    Returns:
        url_type - the organization type (str)
            'business' if url ends with 'com'
            'non-profit' if url ends with 'org'
            'other' if url ends with something else
    ------------------------------------------------------
    """
    if url.endswith('com'):
        url_type = 'business'
    elif url.endswith('org'):
        url_type = 'non-profit'
    else:
        url_type = 'other'
    return url_type


def parse_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code. A product code has three parts:
        The first three letters describe the product category
        The next four digits are the product ID
        The remaining characters describe the product's qualifiers
    Use: pc, pi, pq = parse_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a valid product code (str)
    Returns:
        pc - the category part of product_code (str)
        pi - the id part of product_code (str)
        pq - the qualifier part of product_code (str)
    -------------------------------------------------------
    """
    pc = product_code[:3]
    pi = product_code[3:7]
    pq = product_code[7:]
    return pc, pi, pq


def validate_code(product_code):
    """
    -------------------------------------------------------
    Parses a given product code and prints whether the various parts are valid.
    A product code has three parts:
        The first three letters describe the product category and must
        all be in upper case.
        The next four digits are the product ID.
        The remaining characters describe the product's qualifiers,
        such as colour, size, etc. and always begins with an uppercase letter.
    Use: category, digits, qualifiers = validate_code(product_code)
    -------------------------------------------------------
    Parameters:
        product_code - a product code (str)
    Returns:
        category - True if there are three upper-case characters, False otherwise
        digits - True if there are four digits, False otherwise
        qualifiers - True if starts with 1 upper-case letter, False otherwise
        example : validate_code('BFG9000x7') -> (True, True, False)
    -------------------------------------------------------
    """
    category = False
    digits = False
    qualifiers = False

    if len(product_code) >= 3:
        category = product_code[:3].isupper()
    if len(product_code) >= 7:
        digits = product_code[3:7].isdigit()
    if len(product_code) > 7:
        qualifiers = product_code[7].isupper()
        
    return category, digits, qualifiers


def is_palindrome(s):
    """
    -----------------------------------------------------------------
    Checks whether the given string is palindrome or not. A palindrome is
    a string the reads the same forwards as backwards. Case is ignored.
    Use: palindrome = is_palindrome(s)
    -----------------------------------------------------------------
    Parameters:
        s - a string to be checked (str)
    Returns:
        palindrome - True if s is a palindrome, False otherwise (boolean)
    -----------------------------------------------------------------
    """
    s = s.lower()
    s = s.replace(' ', '')
    palindrome = s == s[::-1]
    return palindrome


def text_analyze(txt):
    """
    -------------------------------------------------------
    Analyzes txt and returns the number of uppercase letters,
    lowercase letters, digits, and number of whitespaces in txt.
    Use: uppr, lowr, dgts, whtspc = text_analyze(txt)
    -------------------------------------------------------
    Parameters:
        txt - the text to be analyzed (str)
    Returns:
        uppr - number of uppercase letters in txt (int >= 0)
        lowr - number of lowercase letters in txt (int >= 0)
        dgts - number of digits in txt (int >= 0)
        whtspc - number of white spaces in the text (spaces, tabs, linefeeds) (int >= 0)
    ------------------------------------------------------
    """
    uppr = 0
    lowr = 0
    dgts = 0
    whtspc = 0
    for c in txt:
        if c.isupper():
            uppr += 1
        elif c.islower():
            lowr += 1
        elif c.isdigit():
            dgts += 1
        elif c.isspace():
            whtspc += 1
    return uppr, lowr, dgts, whtspc