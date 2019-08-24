# -*- coding: utf-8 -*-
"""
File to play 2048
"""
from Game import Game
from Agent import Agent
import logic
import numpy as np
import threading
import multiprocessing

num_games = 4
num_workers = 4
games_per_worker = num_games // num_workers
agent = Agent()

def play_game(worker_num):
    for game_id in range(1, games_per_worker+1):
        game = Game()
        game.print_matrix()
        while not game.isGameOver():
            moves = logic.possible_actions(game.matrix) # Get all possible actions
            move = agent.take_action(moves, game.moves_dict, game.matrix)
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
            #game.print_matrix()
        agent.update_final_score(game.score(), game_num=worker_num*game_id)
        print("Finished game {0}: {1}".format(worker_num*game_id, game.score()))

if __name__ == "__main__":
    game_threads = []
    for worker in range(1, num_workers+1):
        t = multiprocessing.Process(target=play_game, args=(worker,))
        game_threads.append(t)

    for thread in game_threads:
        thread.start()

    for thread in game_threads:
        thread.join()

    print("Done!")


