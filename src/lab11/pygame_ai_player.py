""" Create PyGameAIPlayer class here"""
import random

class PyGameAIPlayer:
    # Constructor that sets the current_city to 0
    def __init__(self):
        self.current_city = 0
        pass
    def selectAction(self):
        # we increment the city by 1 and do modulos 10 to prevent going over 9
        self.current_city = (self.current_city + 1) % 10
        # we return the city we want to go to
        return ord(str(self.current_city))

    pass


""" Create PyGameAICombatPlayer class here"""


class PyGameAICombatPlayer:
    # Constructor for the Combat Player
    def __init__(self, name):
        super().__init__(name)

    def weapon_selecting_strategy(self):
        # Pick a random number between 1-3 and subtract 1 to stay within weapon index 
        self.weapon = random.randint(1, 3) - 1
        # Return the weapon
        return self.weapon

    pass
