"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-11-11"
-------------------------------------------------------
"""
# Imports

# Constants

def total_wins():
    """
    -------------------------------------------------------
    Returns the total number of wins for the teams "purple" and "gold".
    Use: wins = total_wins()
    -------------------------------------------------------
    Returns:
        purple, gold - the total number of wins for both purple and gold (int)
    """
    purple = 0
    gold = 0
    team = input('Enter winning team: ')
    while team != '':
        if team == 'purple':
            purple += 1
        elif team == 'gold':
            gold += 1
        team = input('Enter winning team: ')
    return purple, gold


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """
    prime = True
    i = 2
    while i < number:
        if number % i == 0:
            prime = False
            break
        i += 1
    return prime

def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    month = 1
    interest_rate_monthly = (interest_rate / 100) / 12

    print(f'Principal: ${principal_amount:.2f}')
    print(f'Interest Rate: {interest_rate:.2f}%')
    print(f'Monthly Payment: ${payment:.2f}')
    print('----------------------------------')
    print('Month Interest   Payment   Balance')
    print('----------------------------------')
    while principal_amount > 0:
        if payment > principal_amount:
            interest_gained = principal_amount * interest_rate_monthly
            payment = principal_amount + interest_gained
            principal_amount = 0
        else:
            interest_gained = principal_amount * interest_rate_monthly
            principal_amount = principal_amount - payment + interest_gained
        print(f'{month:5}{interest_gained:9.2f}{payment:10.2f}{principal_amount:10.2f}')
        month += 1
    return


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """
    digits = 0
    number = abs(number)
    while number > 0:
        number //= 10
        digits += 1
    return digits


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
        Must use while loop in this function.
    ------------------------------------------------------
    """
    total = 0
    i = 1
    while i < number:
        if number % i == 0:
            total += i
        i += 1
    return total