"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-11-25"
-------------------------------------------------------
"""
# Imports

# Constants

def add_spaces(sentence):
    """
    -------------------------------------------------------
    Create a new sentence with added space between words. Words start
    with upper-case characters.
    Use: spaced = add_spaces(sentence)
    -------------------------------------------------------
    Parameters:
        sentence - sentence that represents a sentence in which all the
            words are run together (no spaces), but the first character
            of each word is uppercase. sentence has at least one
            character (str)
    Returns:
        spaced - new sentence in which the words are separated
            by spaces and only the first word starts with
            an uppercase character (str)
    -------------------------------------------------------
    """
    spaced = sentence[0]
    for i in range(1, len(sentence)):
        if sentence[i].isupper():
            spaced += " " + sentence[i]
        else:
            spaced += sentence[i]
    return spaced.capitalize()

def pluralize(string):
    """
    -------------------------------------------------------
    Pluralizes a string according to the rules:
        - if string ends with 's', 'sh', or 'ch', add 'es'
        - if string ends with 'y' but not 'ay' or 'oy', replace
            the 'y' with 'ies'
        - otherwise add 's'
    Use: pluralized = pluralize(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        pluralized - a pluralized_string version of string (str)
    -------------------------------------------------------
    """
    if string.endswith("s") or string.endswith("sh") or string.endswith("ch"):
        pluralized = string + "es"
    elif string.endswith("y") and not string.endswith("ay") and not string.endswith("oy"):
        pluralized = string[:-1] + "ies"
    else:
        pluralized = string + "s"
    return pluralized

def common_end(str1, str2):
    """
    -------------------------------------------------------
    Returns the longest common ending of two strings.
    Use: suffix = common_end(str1, str2)
    -------------------------------------------------------
    Parameters:
        str1 - first string for ending comparison (str)
        str2 - second string for ending comparison (str)
    Returns:
        suffix - the longest common ending of str1 and str2 (str)
    -------------------------------------------------------
    """
    suffix = ""
    i = 1
    while i <= len(str1) and i <= len(str2):
        if str1[-i] == str2[-i]:
            suffix = str1[-i] + suffix
        else:
            break
        i += 1
    return suffix

def valid_isbn(isbn):
    """
    -------------------------------------------------------
    Determines if an ISBN string is valid. An ISBN string is valid if:
        - it consists of only digits and dashes ('-')
        - it contains 5 groups of digits separated by dashes
        - its first group of digits is either '978' or '979'
        - its final group of digits is a single digit
        - its entire length is 17 characters
    Use: is_valid = valid_isbn(isbn)
    -------------------------------------------------------
    Parameters:
        isbn - a string (str)
    Returns:
        is_valid - True if isbn is valid, False otherwise (boolean)
    -------------------------------------------------------
    """
    is_valid = True
    num_groups_digits = isbn.split('-')

    if len(isbn) != 17:
        is_valid = False
    elif isbn[0:3] not in ['978', '979']:
        is_valid = False
    elif not isbn[-1].isdigit():
        is_valid = False
    elif len(num_groups_digits) != 5:
        is_valid = False
    else:
        for i in range(len(isbn)):
            if not (isbn[i].isdigit() or isbn[i] == '-'):
                is_valid = False
                break
            elif i > 0 and isbn[i] == '-' and isbn[i - 1] == '-':
                is_valid = False
                break

    return is_valid

def has_word_chain(words):
    """
    -------------------------------------------------------
    Determines if a list of strings is a word chain. A word chain
    is a list of words in which the last character of a word in
    the list is the same as the first character of the next word
    in the list.
    Use: word_chain = has_word_chain(words)
    -------------------------------------------------------
    Parameters:
        words - a list of strings (list of str, len > 1)
    Returns:
        word_chain - True if words is a word chain,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    word_chain = True
    i = 0
    while i < len(words) - 1:
        if words[i][-1] != words[i + 1][0]:
            word_chain = False
            break
        i += 1
    return word_chain