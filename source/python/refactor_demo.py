# Simple piece of procedural code to calculate total price
units_sold = 100
unit_price = 2
total_price = units_sold * unit_price
print(f"Total price: ${total_price}")

# q: refactor this code to give it moore structure, readability, and separation of concerns.
# q: refactor this code to use a class and methods instead of functions
# q: add a main() function to the code

""" # Expected Result
def calculate_total_price(units_sold, unit_price):
    return units_sold * unit_price

def main():
    units_sold = 100
    unit_price = 2
    total_price = calculate_total_price(units_sold, unit_price)
    print(f"Total price: ${total_price}")

if __name__ == "__main__":
    main()
"""

"""
GitHub Copilot can assist in this refactoring process by suggesting function names, parameter names, 
and even entire function bodies based on natural language descriptions. 
It helps transform procedural code into more structured and idiomatic Python code. 
In the refactored version:
1.	We’ve encapsulated the calculation logic within a function called calculate_total_price.
2.	The main() function now orchestrates the program flow.
3.	By using functions, we achieve better code organization, reusability, and maintainability.
4.	We’ve added a conditional block to check if the script is being run as the main program.
"""