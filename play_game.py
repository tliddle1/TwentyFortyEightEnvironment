# -*- coding: utf-8 -*-
"""
File to play 2048
"""
from Game import Game
from Agent import Agent
import logic
import numpy as np


game = Game()
agent = Agent()
game.print_matrix()

scores = []
for _ in range(100):
    num_moves = 0
    while not game.isGameOver():
        num_moves = num_moves + 1
        moves = logic.possible_actions(game.matrix) # Get all possible actions
        move = agent.take_action(moves, game.moves_dict)
        print(move)
        if (move == "w"):
            game.take_action(1)
        if (move == "s"):
            game.take_action(2)
        if (move == "a"):
            game.take_action(3)
        if (move == "d"):
            game.take_action(4)
        if (move == "q"):
            break
        #action = random.randint(0, len(moves)-1)
        #game.take_action(moves[action])
        game.print_matrix()
    scores.append(num_moves)

print(scores)
