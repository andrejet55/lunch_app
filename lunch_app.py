# App to know what to make for lunch for one week
# Version 1.0:
#   Randomly selects one dish per day according to the list of dishes
#   Allows to add more dishes

#Version 2.0:
#   GUI

# Version 2.0:
#   Allows to select for one week the recipes with food in common to save time in preparation
#   and chop or cook in advance from day one


# Version 3.0
#   Balance food for health

# Version 4.0
#   Saves data on cloud. SQL queries
#   Allows to vote recipes (best for students, cheapest, easiest)

# Version 5.0
# Data analysis with the social media about foods
# Vinculates statistics with coupons and local business, supermarkets, grocery stores, etc.


import pandas as pd
from menu import define_lunch, create_menu, get_menu, add_recipe, delete_recipe

print("Welcome! to the lunch chooser.")

option = ''

while option != 'E':
    menu = pd.read_csv('menu.csv')
    
    option = input("Press S to get an idea for lunch, M to go to the recipes menu or E to exit.\n")

    if option == 'M':
        while option != 'EM':
            option = input('''Welcome to the menu. Press "See" to see all the recipes in the menu, "Add" to add a recipe and "Delete" to eliminate one.
            If you want to exit recipe menu write "EM".\n''')
            
            if option == 'See':
                #Reads the file with the menu, if not a file, prints there are no recipes
                #Try and catch
                try:
                    get_menu(menu)
                except ValueError:
                    create_menu()
            elif option == 'Add':
                add_recipe(menu)   
                
            elif option == 'Delete':
                delete_recipe(menu) 
            
    if option == 'S':
        
        define_lunch(menu)
        
    elif option == 'E':
        print('Enjoy your food! Goodbye :/)')
        
    else:
        print("Try putting a valid command.\n")
    
        
    

