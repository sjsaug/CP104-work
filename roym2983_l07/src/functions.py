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

def population_growth(target, current, rate):
    """
    -------------------------------------------------------
    Determines the number of years to reach a target population.
    Use: years = population_growth(target, current, rate)
    -------------------------------------------------------
    Parameters:
        target - target population (int > current)
        current - current population (int > 1)
        rate - percent rate of growth (float > 0)
    Returns:
        years - the number of years to reach target population (int)
    -------------------------------------------------------
    """
    years = 0
    while current < target:
        current = current * (1 + rate / 100)
        years += 1
    return years


def positive_statistics():
    """
    -------------------------------------------------------
    Asks a user to enter a series of positive numbers, then calculates
    and returns the minimum, maximum, total, and average of those numbers.
    Stop processing values when the user enters a negative number.
    The first number entered must be positive.
    Use: minimum, maximum, total, average = positive_statistics()
    -------------------------------------------------------
    Returns:
        minimum - smallest of the entered values (float)
        maximum - largest of the entered values (float)
        total - total of the entered values (float)
        average - average of the entered values (float)
    ------------------------------------------------------
    """
    num = float(input("Enter a positive number (negative to quit): "))
    minimum = num
    maximum = num
    total = num
    count = 1
    while num >= 0:
        num = float(input("Enter a positive number (negative to quit): "))
        if num >= 0:
            total += num
            count += 1
            if num < minimum:
                minimum = num
            if num > maximum:
                maximum = num
    average = total / count
    return minimum, maximum, total, average


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    expenses = 0
    num = float(input("Enter an expense (0 to quit): "))
    while num != 0:
        expenses += num
        num = float(input("Enter an expense (0 to quit): "))
    balance = available - expenses
    if balance > 0:
        status = "Surplus"
    elif balance < 0:
        status = "Deficit"
    else:
        status = "Balanced"
    return expenses, balance, status


def get_int(low, high):
    """
    -------------------------------------------------------
    Asks a user for an integer value between low and high, and
    continues asking until an acceptable value is input.
    Use: value = get_int(low, high)
    -------------------------------------------------------
    Parameters:
        low - the lowest acceptable integer (inclusive) (int)
        high - the higest acceptable integer (inclusive) (int > low)
    Returns:
        value - a number between low and high (int)
    ------------------------------------------------------
    """
    value = int(input(f"Enter a value between {low} and high {high}: "))
    while value < low or value > high:
        if value < low:
            print(f"Value is too low")
        if value > high:
            print(f"Value is too high")
        value = int(input(f"Enter a value between {low} and high {high}: "))
    return value

def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """
    total = 0
    count = 0
    employee_id = int(input("Employee ID: "))
    while employee_id != 0:
        wage = float(input("Hourly wage rate: "))
        hours = float(input("Hours worked: "))
        if hours > 40:
            wage = wage * 1.5
            salary = wage * hours
            #salary = (wage * 40) + (wage * (hours - 40))
        else:
            salary = wage * hours
        salary = salary - (salary * 0.03625)
        total += salary
        count += 1
        employee_id = int(input("Enter employee ID (0 to quit): "))
    average = (total / count)
    return total, average