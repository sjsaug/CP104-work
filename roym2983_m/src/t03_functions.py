"""
-------------------------------------------------------
Midterm B Task 3 Function Definitions
-------------------------------------------------------
Author: August Roy Mclaughlin
ID:     169052983
Email:  roym2983@mylaurier.ca
__updated__ = "2023-11-01"
-------------------------------------------------------
"""
# Constants
# your constants here
BASE_COST = 125.00
EXTRA_COST = 25.00
VIP_DISCOUNT = 0.10


def servicing():
    """
    -------------------------------------------------------
    Determines the cost of getting a home furnace tune up. The cost is made up of:
        base cost: $125.00
        cost per extra service: $25.00
        VIP discount 10% only if:
            more than 1 extra service purchased
            and purchaser is a VIP
    The function must ask the user for these inputs.
    Use: cost = servicing()
    -------------------------------------------------------
    Returns‌​‌​​​​‌​​‌‌‌​​​‌​‌‌​​‌‌​‌‌‌:
        cost - cost of getting a home furnace tune up based upon the base cost,
            the number of extra services purchased, and VIP discount
            if applicable (float)
    -------------------------------------------------------
    """

    # your code here
    services = int(input("How many extra services are you purchasing? "))
    cost = BASE_COST + (EXTRA_COST * services)

    if services > 1:
        vip = input("Are you a VIP member (Y/N)? ")
        if vip == "Y":
            cost = cost - (cost * VIP_DISCOUNT)

    return cost
