"""
File:    silicon_crisis.py
Author:  Snigdha Darji
Date:    05/07/21
Section: 14
E-mail: sdarji1@umbc.edu
Description:
  takes data from a json file created from recipe_maker.py
  displaying data of amounts and creating mines/factories
"""

import json


class Crisis:



    def __init__(self):

        # if filename was not provided, ask for it
        # if not filename:

        #opens the json file
        filename = input("Enter SC Recipe File Name: ")

        # open JSON file and store it in dictionary
        with open(filename) as f:
            data = json.loads(f.read())


        self.filename = ''

        # store raw materials and recipe
        self.raw_materials = data["raw_materials"]
        self.recipes = data["recipes"]

        # create 2 idling mines and factories, both with 0 production
        self.mines = ['', '']
        self.factories = ['', '']
        self.turns_same_production = [0, 0]


        # set current turn to 1
        self.turns = 1

        # create empty stockpile and set each item to 0
        self.stockpile = {}

        for material in self.raw_materials:
            self.stockpile[material] = 0

        for recipe in self.recipes:
            self.stockpile[recipe] = 0




    # recursive, calculate how many you need to create item
    def calculate_cost(self, item, target):

        target_count = 0

        #base case
        if item in self.raw_materials or item not in self.recipes:
            return 0

        #checking every item in parts
        parts = self.recipes[item]['parts']

        for part in parts:
            if part == target:

                #adds each part
                target_count += parts[part]

            elif part in self.recipes:
                target_count += self.calculate_cost(part, target) * parts[part]

        #returns the total number of how many x in y
        return target_count



    # set raw material to mine
    def set_mine(self, mine_index, material):
        """

        :param mine_index:
        :param material:
        :return:
        """

        if 0 <= mine_index < len(self.mines) and material in self.raw_materials:

            if self.mines[mine_index] == '':
                self.mines[mine_index] = material



    # sets recipe to produce
    def set_factory(self, factory_index, recipe):

        if 0 <= factory_index < len(self.factories) and recipe in self.recipes:

            self.factories[factory_index] = recipe
            self.turns_same_production[factory_index] = 0



    # display mines
    def display_mines(self):

        for i in range(len(self.mines)):
            mine = self.mines[i]

            print("\tMine",i)

            #mine is not set yet hence the ''
            if mine == '':
                print("\t\tMine Currently Inactive")

            else:
                print('\t\t',mine,'mine producing',self.raw_materials[mine],'per turn')



    # display factories
    def display_factories(self):

        for i in range(len(self.factories)):
            factory = self.factories[i]

            print("\tFactory",i)

            #factory not set yet
            if factory == '':

                print("\t\tFactory Currently Inactive")

            else:

                #produces based on turn and user input
                turn_production = self.recipes[factory]["output_count"]
                turns_same_production = self.turns_same_production[i]
                total_production = turns_same_production * turn_production

                print("\t\t",factory,"factory producing",turn_production,"per turn, total production",total_production)



    # display raw materials
    def display_materials(self):

        print(':::Raw Materials:::')

        for material in self.raw_materials:

            print("\t",material,"- mined in increments of",self.raw_materials[material])



    # display recipes
    def display_recipes(self):

        print(":::Recipes:::")

        for recipe in self.recipes:

            print("\t",recipe,"- produced in increments of",self.recipes[recipe]['output_count'])

            print("\tRequired Materials:")

            for part in self.recipes[recipe]['parts']:
                count = self.recipes[recipe]['parts'][part]

                print("\t\t",part,": ",count)



    # display stockpile
    def display_stockpile(self):

        print(":::Current Stockpile:::")

        for item in self.stockpile:
            count = self.stockpile[item]

            #there's stuff set in the stockpile
            if count != 0:
                print("\t",item,": ",count)



    # check if there is enough parts on stockpile to make an item
    def check_stockpile_for_parts(self, item):

        required_parts = self.recipes[item]['parts']

        for required_part in required_parts:
            required_count = required_parts[required_part]

            # if greater than, there's not enough to produce it
            if required_count > self.stockpile[required_part]:

                return False

        return True



    # remove parts needed to create item from stockpile
    def subtract_parts(self, item):

        required_parts = self.recipes[item]['parts']

        for required_part in required_parts:

            required_count = required_parts[required_part]
            self.stockpile[required_part] -= required_count



    # mine raw material from all mines
    def mine_all(self):

        for material in self.mines:

            if material != '':

                self.stockpile[material] = self.raw_materials[material] + self.stockpile[material]



    # produces object for factory with given index
    def produce_one(self, index):


        recipe = self.factories[index]

        # check if there is enough supplies
        if self.check_stockpile_for_parts(recipe):
            # if yes, remove them from stockpile
            self.subtract_parts(recipe)
            output_count = self.recipes[recipe]['output_count']

            # check if produced item was a factory
            if recipe == 'factory':

                for i in range(output_count):

                    #this is just setting it with an empty string, not yet adding stuff
                    self.factories.append('')
                    self.turns_same_production.append(0)


            # check if a mine
            elif recipe == 'mine':

                for x in range(output_count):
                    self.mines.append('')

            else:
                self.stockpile[recipe] = self.stockpile[recipe] + output_count


            # add production count
            self.turns_same_production[index] += 1



    # loops over factories, tried to produce item based on recipe
    def produce_all(self):


        for i in range(len(self.factories)):

            # check if factory works
            if self.factories[i] != '':

                #makes a factory
                self.produce_one(i)



    # make one turn
    def make_turn(self):

        #print output
        print('Mining...')
        self.mine_all()

        print('Making...')
        self.produce_all()

        #counter for a turn
        self.turns += 1

        print('Turn',self.turns,'Complete')




    # read command from user, execute function based on command
    # return True when user wants to continue, False for quit
    def next_command(self):

        cmd = input('Select Next Action>> ').lower()


        # makes one turn
        if cmd =='end turn':
            self.make_turn()


        #quits the entire program
        elif cmd == 'quit':
            return False

        else:

            #splits the user input
            cmd_words = cmd.split()

            # handling "set" commands goes back to the methods with input
            if cmd_words[0] == 'set' and len(cmd_words) == 4:

                if cmd_words[1] == 'mine':

                    self.set_mine(int(cmd_words[2]), cmd_words[3])

                elif cmd_words[1] == 'factory':

                    self.set_factory(int(cmd_words[2]), cmd_words[3])

            # all of the display commands
            elif cmd_words[0] == 'display':

                if len(cmd_words) == 2:

                    # display stockpile command
                    if cmd_words[1] == 'stockpile':
                        self.display_stockpile()

                    # display factories command
                    elif cmd_words[1] == 'factories':
                        self.display_factories()

                    # display mines command
                    elif cmd_words[1] == 'mines':
                        self.display_mines()

                     #display recipes command
                    elif cmd_words[1] == 'recipes':
                        self.display_recipes()

                elif cmd == 'display raw materials':
                    self.display_materials()


            # "how many x are in a y" command
            elif len(cmd_words) == 7 and cmd_words[0] == 'how' and cmd_words[1] == 'many':

                item = cmd_words[6]
                target = cmd_words[2]

                #calculates
                print('There are',self.calculate_cost(item, target),target,'in a',item)

        #keeps going
        return True


    # handle commands in a loop
    def run(self):

        #place holder to keep the loop keep giving next action
        while (self.next_command()):
            pass



if __name__ == "__main__":

    Crisis().run()