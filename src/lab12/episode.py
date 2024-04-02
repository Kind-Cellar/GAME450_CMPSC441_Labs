''' 
Lab 12: Beginnings of Reinforcement Learning

Create a function called run_episode that takes in two players
and runs a single episode of combat between them. 
As per RL conventions, the function should return a list of tuples
of the form (observation/state, action, reward) for each turn in the episode.
Note that observation/state is a tuple of the form (player1_health, player2_health).
Action is simply the weapon selected by the player.
Reward is the reward for the player for that turn.
'''
import sys
from pathlib import Path

sys.path.append(str((Path(__file__) / ".." / ".." / "..").resolve().absolute()))

from src.lab11.pygame_combat import run_turn
from src.lab11.turn_combat import Combat



def run_episode(playerOne, playerTwo):
    currentGame = Combat()
    returnResult = []
    result = run_turn(currentGame, playerOne, playerTwo)
    returnResult.append(result)
    while 2 > 1:
        if(result[0][0] == 0 or result[0][1] == 0):
            return returnResult
        else:
            result = run_turn(currentGame, playerOne, playerTwo)
            returnResult.append(result)
    return returnResult
