# -*- coding: utf-8 -*-
from Game import Game
import numpy as np
import logic
import json

""" class Data:
    def __init__(self, state, action_probabilities=[], score=0):
        self.state = state
        self.action_probabilities = action_probabilities
        self.score = score

    def set_score(self, score):
        self.score = score """

class Agent:
    """
    Agent class for TwentyFortyEight Environment
    """
    def __init__(self, agent_type="computer"):
        self.agent_type = agent_type
        self.scale = 1.0
        self.game_end = False
        #Database for storing states and probabilities
        self.database = [] 
        
    def take_action(self, moves, moves_dict, game_state=None):
        if self.agent_type == "human":
            action = input()
        else:
            action = self.policy(moves, moves_dict, game_state)
        return action
    
    def policy(self, moves, moves_dict, game_state):
        if game_state is None: # Computer blindly makes random moves
            choice = np.random.choice(moves)
        else:
            choice = self.MCTS(game_state)
            
        return moves_dict[choice]

    def select(self, start_state, game):
        curr_state = start_state
#        start = True
        while True:
            possible_actions = logic.possible_actions(curr_state)  # Get all possible actions. These are numbers
            s = tuple(tuple(x) for x in curr_state)
#            print("Current state:", s)
#            input()
            try:
                # SELECTION
                options = []
                
                for a in possible_actions:
                    P = self.memory[s][a]["P"]
                    W = self.memory[s][a]["W"]
                    N = self.memory[s][a]["N"]
                    if N == 0:
                        Q = 0
                    else:
                        Q = W / N
                    options.append(Q + self.scale * (P / (1 + N)))  # Balances exploration and exploitation
#                print("Select one of:")
#                print(options, self.scale)
#                input()

                if options:
                    self.game_end = False
                    a = possible_actions[np.argmax(options)]
#                    print("We chose:", a)
#                    input()
                    game.take_action(a)
                    self.history.append((s, a))  # Keeps track of our history
#                    print("self.history is now:", self.history)
                    curr_state = game.matrix
#                    print("New state is:", curr_state)
#                    
#                    input()
                else:
                    self.game_end = True
                    return 0  # We are at the end of the game
                # SIMULATION AND EXPANSION
            except KeyError:  # We have hit a leaf node
#                print("We hit a leaf node:")
#                print(game.matrix)
#                input()
                vs=[]
                for _ in range(1):
                    vs.append(self.random_simulation(game.matrix))  # Gets score for random simulation to estimate value of state (use nn)
                v = np.mean(vs)
                self.memory[s] = dict()
                len_possible = len(possible_actions)
                for a in possible_actions:
                    self.memory[s][a] = dict()
                    self.memory[s][a]["P"] = 1 / len_possible  # Sets a uniform prior
                    self.memory[s][a]["W"] = 0
                    self.memory[s][a]["N"] = 0
#                print("After expanding, memory is now:", self.memory)
#                input()
                return v
            

    def update(self, start_state, sim_num, v):
        starting_tuple = tuple(tuple(x) for x in start_state)
        starting_memory = self.memory[starting_tuple]
        for action in starting_memory.keys():
#            print("Updated", action)
            self.scale += starting_memory[action]["W"]
        self.scale = 4 * self.scale / (sim_num + 1)
        for i, (s, a) in enumerate(self.history):
#            print("Updating history:", s, a)
#            input()
            self.memory[s][a]["N"] += 1  # Update N
            self.memory[s][a]["W"] += v  # Update W
#            curr_state = list(list(x) for x in s)
#            possible_actions = logic.possible_actions(curr_state) 
#            total_N = 0
#            for action in possible_actions:
#                total_N += self.memory[s][action]["N"]
#            for action in possible_actions:
#                if self.memory[s][action]["N"] == 0
#                self.memory[s][action]["P"] = self.memory[s][action]["N"] / total_N
    
    def MCTS(self, start_state, NNN=1000, deterministic=True): #Changed symbol for N
        game = Game()
        game.matrix = start_state
        self.memory = dict()

        for sim_num in range(NNN):
            if sim_num % 100 == 0:
                print(sim_num)
            self.history = []
            game.matrix = start_state # Resets our game back to the original starting spot
            v = self.select(start_state, game) # Select a state based on the start state
            self.update(start_state, sim_num, v)

        # Make decision   
        starting_tuple = tuple(tuple(x) for x in start_state)
        possible_actions = logic.possible_actions(start_state) # Get all possible actions. These are numbers
        options = []
        p_array = []
        print("After Monte Carlo Tree Search, options are:")
        for a in possible_actions:
            P, W, N = self.memory[starting_tuple][a]["P"], self.memory[starting_tuple][a]["W"], self.memory[starting_tuple][a]["N"]
            P = N/NNN #Calculate probability
            p_array.append(P)
            print("{0}: P={1}, W={2}, N={3}".format(game.moves_dict[a], str(P), str(W), str(N)))
            if deterministic:
                options.append(N)
            else:
                options.append(P)
        data = {
            "start_state": start_state,
            "probabilities": p_array,
            "score": 0
        }
        self.database.append(data) # Adds data for states and probabilities to temp database
        if deterministic:
            choice = possible_actions[np.argmax(options)]
            print()
            print("Acting Deterministically...")
            print("AI chose:", game.moves_dict[choice])
            print()
        else:
            choice = np.random.choice(possible_actions, p=options) # Here tou is set to 1
            print()
            print("Acting Stochastically...")
            print("AI chose:", game.moves_dict[choice])
            print()
    
        return choice

    def random_simulation(self, start_state):
        game = Game()
        game.matrix = start_state

        while not game.isGameOver():
            moves = logic.possible_actions(game.matrix) # Get all possible actions
            move = self.take_action(moves, game.moves_dict) # Not including the game state gives a random move
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
        return game.score()
        
    def update_final_score(self, score):
        for i in range(len(self.database)):
            self.database[i]["score"] = score
            #print(self.database[i])
        with open('data.txt', 'w') as outfile:
            json.dump(self.database, outfile)