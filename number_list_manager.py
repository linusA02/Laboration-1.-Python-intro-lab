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
    # Print each number separately instead of printing the whole list.
    for number in random_numbers:
        print(number)


def sort_ascending():
    # Sort the list from smallest to largest.
    random_numbers.sort()


def sort_descending():
    # Sort the list from largest to smallest.
    random_numbers.sort(reverse=True)


def add_number():
    # Ask the user for a number and add it to the list.
    try:
        number = int(input("Enter a number: "))
        random_numbers.append(number)
    except ValueError:
        print("Please enter a valid number.")


def remove_number():
    # Remove a specific number from the list.
    try:
        number = int(input("Enter the number to remove: "))

        if number in random_numbers:
            random_numbers.remove(number)
        else:
            print("That number is not in the list.")

    except ValueError:
        print("Please enter a valid number.")


def remove_last():
    # Remove the last number if the list is not empty.
    if random_numbers:
        random_numbers.pop()
    else:
        print("The list is empty.")


def remove_first():
    # Remove the first number if the list is not empty.
    if random_numbers:
        random_numbers.pop(0)
    else:
        print("The list is empty.")


def sum_numbers():
    # Calculate and print the sum of all numbers.
    print(sum(random_numbers))


# Logic for your menu
while True:
    try:
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
    0. Quit
    """)
        )

    except ValueError:
        print("Please enter a number from the menu.")
        continue

    if user_choice == 1:
        show_data()

    elif user_choice == 2:
        sort_ascending()

    elif user_choice == 3:
        sort_descending()

    elif user_choice == 4:
        add_number()

    elif user_choice == 5:
        remove_number()

    elif user_choice == 6:
        remove_last()

    elif user_choice == 7:
        remove_first()

    elif user_choice == 8:
        sum_numbers()

    elif user_choice == 0:
        print("Goodbye!")
        break

    else:
        print("Please choose a valid menu option.")