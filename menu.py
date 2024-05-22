# Code to manipulate menu

import random
import pandas as pd
from tabulate import tabulate

def define_lunch(menu):
        
        number_recipes = len(menu)
        lunch_index = random.randint(0,number_recipes-1)
        lunch = menu.iloc[lunch_index]
        
        pd.set_option('display.max_colwidth', None)
        print("Your lunch today will be:\n",lunch)

def create_menu():
    #Creates dataframe
    print('There is no menu available. You need to add new recipes!')
    features = ['Recipe', 'Ingredients', 'Instructions']
    menu = pd.DataFrame(columns=features)
    print('Empty menu created succesfully')


#Read recipes
def get_menu(menu):

    menu = pd.read_csv('menu.csv')
    
    # Display the DataFrame using tabulate with a custom table format
    print(tabulate(menu, headers=menu.columns, tablefmt="grid"))  # Adjust tablefmt as needed
    return menu


def add_recipe(menu):
    
    name = input('Write the name of your recipe\n')
    ingredients = input('Write the list of ingredients in just one line, separated by coma\n')
    instructions = input('Write the instructions to prepare your recipe\n')
    recipe = {"Name": name, "Ingredients": ingredients, 'Instructions': instructions}
    
    # Append the new row to the DataFrame (adds to the end by default)
    menu.loc[len(menu.index)] = recipe
    
    # Save the DataFrame to a CSV file
    menu.to_csv("menu.csv", index=False)
    
    print("recipe added successfully!")


def delete_recipe(menu):
    name = input("Write the name of the recipe you want to delete")
    
    # Select rows where "name" is equal to the target name using `.isin`
    rows_to_drop = menu["Name"].isin([name])
    #drop that recipe
    menu = menu.drop(menu[rows_to_drop].index)
    
    # Save the DataFrame to a CSV file
    menu.to_csv("menu.csv", index=False)
    
    print("recipe deleted successfully!")