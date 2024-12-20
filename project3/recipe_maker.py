"""
File:    recipe_maker.py
Author:
Date:    05/07/21
Section:
E-mail:
Description:
  taking raw materials from factories and converting them
  to recipes
"""

class Recipe:

    def ___init__(self, dict, raw, rate, output, ingredient, amount,file):

        self.dict = {}
        self.raw = raw
        self.raw_list = {}
        self.rate = rate
        self.output = output
        self.ingredient = ingredient
        self.amount = amount
        self.file = file
    """
    def recipe_maker(self):

        #need a for loop for every raw, ask for input that many number of times

        self.raw = input('Name the raw material? ')
        while self.raw != 'done':

            self.rate = int(input('What is the rate at which it is mined? '))
            self.raw = input('Name the raw material? ')

        else:
            self.output = input('Name the output? ')
            self.rate = input('What is the rate at which it is output? ')

            self.ingredient = input('Name the ingredient: ')
            while self.ingredient != 'stop':

                self.amount = input('How much of that ingredient is needed? ')
                self.ingredient = input('Name the ingredient: ')

            else:
                self.output = input('Name the output: ')
                self.rate = input('What is the rate at which it is output? ')


        return {"raw_materials": {self.raw:self.rate}, "recipes": {self.output: {"output": self.output,
                                                                                 "output_count":self.rate,
                                                                                 "parts":{self.ingredient:self.rate}},
        "cog":{self.output}}}

    
    """

    def raw_materials(self):

        flag = True

        self.raw = input('Name the raw material? ')
        while self.raw != 'done':

            self.rate = int(input('What is the rate at which it is mined? '))
            self.raw = input('Name the raw material? ')

        else:
            flag = False

    def recipes(self):
        flag = True

        self.output = input('Name the output? ')
        self.rate = input('What is the rate at which it is output? ')

        self.ingredient = input('Name the ingredient: ')

        while self.output != 'done':

            while self.ingredient != 'stop':
                self.amount = input('How much of that ingredient is needed? ')
                self.ingredient = input('Name the ingredient: ')

            else:
                flag = True
                if self.ingredient == 'stop':
                    self.output = input('Name the output? ')
                    self.rate = input('What is the rate at which it is output? ')
                    flag = False
    def output(self):




    def run(self):

        flag = True

        while flag:
            self.raw_materials()
            flag = False
        self.recipes()

        if flag == False:

            self.output = input('Name the output? ')
            if self.output == 'done':
                self.file = input('What is the file name? ')




if __name__ == "__main__":

    Recipe().run()








