"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-10-13"
-------------------------------------------------------
"""
# Imports
from math import fabs
# Constants

def get_weight(mass):
    """
    -------------------------------------------------------
    Describes a mass in terms of its weight. If its weight is > 1000 N,
    it is "heavy", less than 10 N it is "light", and "average" otherwise.
    weight = mass (kg)  acceleration due to gravity (9.8/m/s^2)
    Use: weight, message = get_weight(mass)
    -------------------------------------------------------
    Parameters:
        mass - mass of an object in kg (float > 0)
    Returns:
        weight - weight of an object in Newtons (float)
        message - description of weight of object (str)
    -------------------------------------------------------
    """
    ACCEL = 9.8
    weight = mass * (ACCEL)
    
    if weight > 1000:
        msg = "heavy"
        
    elif weight < 10:
        msg = "light"
        
    else:
        msg = "average"
        
    return weight, msg

def closest(target, v1, v2):
    """
    -------------------------------------------------------
    Determines closest value of two values to a target value.
    Use: result = closest(target, v1, v2)
    -------------------------------------------------------
    Parameters:
        target - the target value (float)
        v1 - first comparison value (float)
        v2 - second comparison value (float)
    Returns:
        result - one of v1 or v2 that is closest to target,
          v1 is the value chosen if v1 and v2 are an equal
          distance from target (float)
    -------------------------------------------------------
    """
    distance1 = fabs(target - v1)
    distance2 = fabs(target - v2)

    if distance1 <= distance2:
        result = v1
    else: 
        result = v2
    
    return result
    
def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """
    BREEZE = 39
    STRONG_WIND = 61
    GALE_WINDS = 88
    WHOLE_GALE = 89
    HURRICANE = 117
    if speed < 0:
        category = "Unknown"
    elif fabs(speed) < BREEZE:
        category = "Breeze"
    elif BREEZE <= fabs(speed) <= STRONG_WIND:
        category = "Strong Wind"
    elif (STRONG_WIND + 1) <= fabs(speed) <= GALE_WINDS:
        category = "Gale Winds"
    elif WHOLE_GALE <= fabs(speed) <= HURRICANE:
        category = "Whole Gale"
    else:
        category = "Hurricane"
        
    return category


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    REQ_YEARS = 5
    REQ_SALARY = 30000
    years_employed = int(input("Years employed: "))
    if years_employed >= REQ_YEARS:
        salary = float(input("Annual salary: "))
        if salary >= REQ_SALARY:
            status = bool(True)
        if salary < REQ_SALARY:
            status = bool(False)
    else:
        status = bool(False)
    return status

def fast_food():
    """
    -------------------------------------------------------
    Food order function.
    Asks user for their order and if they want a combo, and if
    necessary, what is the side order for the combo:
    Prices:
        Burger: $6.00
        Wings: $8.00
        Fries combo: add $1.50
        Salad combo: add $2.00
    Use: price = fast_food()
    -------------------------------------------------------
    Returns:
        price - the price of one meal (float)
    -------------------------------------------------------
    """
    BURGER = 6.00
    WINGS = 8.00
    FRIES = 1.50
    SALAD = 2.00
    order = str(input("Order B - burger or W - wings: "))
    if order == "B" or order == "W":
        if order == "B":
            sel_order = BURGER
        if order == "W":
            sel_order = WINGS
        combo_yn = str(input("Make it a combo? (Y/N): "))
        if combo_yn == "Y":
            combo_opt = str(input("Add F - fries or S - salad: "))
            if combo_opt == "F":
                sel_combo = FRIES
            if combo_opt == "S":
                sel_combo = SALAD
        if combo_yn == "N":
            sel_combo = 0
    
        return (sel_order + sel_combo)
