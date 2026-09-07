# Warm-up program 1
# Build a menu-based program that manages a list of random numbers.
# This file is meant to warm you up before the larger student system.
# Try to handle errors by using if-statements or try-except blocks.
# Show a menu for the user that gives the following choices:

# 1. Show all data in the list (NOTE: YOU SHOULD NOT JUST PRINT THE ENTIRE LIST, e.g., print(my_list) is wrong)
# 2. Sort the list in ascending order
# 3. Sort the list in descending order
# 4. Add a number
# 5. Remove a specific number
# 6. Remove the last number
# 7. Remove the first number
# 8. Sum all numbers

# You should try to use separate functions for each functionality.

# Starting code
import random

random_numbers = []


def show_data():
    # Implement
    pass


# Add more functions below

# Logic for your menu
while True:
    # This prompts the user to enter a choice. It converts it to an integer.
    user_choice = int(
        input("""
    1. Show all data in the list
    2. Sort the list in ascending order
    3. Sort the list in descending order
    4. Add a number
    5. Remove a specific number
    6. Remove the last number
    7. Remove the first number
    8. Sum all numbers 
    """)
    )

    if user_choice == 1:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 2:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 3:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 4:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 5:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 6:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 7:
        # Call function here (and remove the pass keyword)
        pass
    elif user_choice == 8:
        # Call function here (and remove the pass keyword)
        pass
