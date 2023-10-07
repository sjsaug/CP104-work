"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  August Roy McLaughlin
ID:      169052983
Email:   roym2983@mylaurier.ca
__updated__ = "2023-10-06"
-------------------------------------------------------
"""
# Imports

# Constants

foundation_length = float(input("Foundation length (m): "))
foundation_width = float(input("Foundation width (m): "))
foundation_height = float(input("Foundation height (m): "))
wall_height = float(input("Wall height (m): "))
concrete_cost = float(input("Cost of concrete ($/m^3): "))
brick_cost = float(input("Cost of bricks ($/m^2): "))

concrete_volume = foundation_length * foundation_width * foundation_height
bricks_needed_for_walls = 2 * wall_height * (foundation_length + foundation_width)
total_concrete_cost = concrete_volume * concrete_cost
total_brick_cost = bricks_needed_for_walls * brick_cost
total_cost = total_concrete_cost + total_brick_cost

print(f"Concrete needed for foundation (m^3): {concrete_volume:.2f}")
print(f"Cost of concrete: ${total_concrete_cost:.2f}")
print(f"Bricks needed for walls (m^2): {bricks_needed_for_walls:.2f}")
print(f"Cost of bricks: ${total_brick_cost:.2f}")
print(f"Total cost: ${total_cost:,.2f}")