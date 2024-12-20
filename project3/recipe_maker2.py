"""
File:    recipe_maker.py
Author:  Snigdha Darji
Date:    05/07/21
Section: 14
E-mail:  sdarji1@umbc.edu
Description:
  taking raw materials from factories and converting them
  to recipes
"""


import json


#gets the raw materials for the recipe
def get_raw_materials():


    materials = {}

    #initialize
    material = input("Name the raw material? ")

    while material != "done" and material != "stop":

        #num at which the raw materials are mined
        rate = int(input("What is the rate at which it is mined? "))

        #sets the value for the key material
        materials[material] = rate
        material = input("Name the raw material? ")

    return materials



#ingredients needed
def get_ingredients():



    result = {}
    ingredient = input("Name the ingredient: ")

    while ingredient != "stop" and ingredient != "done":

        needed = int(input("How much of that ingredient is needed?"))

        # sets the amount needed for the ingredient
        result[ingredient] = needed

        ingredient = input("Name the ingredient: ")

    #returns ingredients dict
    return result


#creates the recipe dictionary
def get_recipes():


    recipes = {}

    output = input("Name the output? ")


    while output != "done" and output != "stop":

        output_count = int(input("What is the rate at which it is output? "))

        # parts gets the ingredients needed for the recipe
        recipe = {"output" : output, "output_count" : output_count, "parts" : get_ingredients() }

        #sets the values for the output keys
        recipes[output] = recipe

        output = input("Name the output? ")


    return recipes


#creates dictionary and opens json
def main():

    #final dictionary
    dict = { "raw_materials" : get_raw_materials(), "recipes" : get_recipes() }

    #asks for the name of json file to be created
    file = input("What is the file name? ")

    #opens and writes a json
    with open(file, 'w') as output:

        #dumps the dictionary into a json file
        output.write(json.dumps(dict))



if __name__ == '__main__':
    main()