"""
2048 Agent
"""

from Game import Game
import numpy as np

class Agent:
    """
    Agent class for TwentyFortyEight Environment
    """
    def __init__(self, agent_type="computer"):
        self.agent_type = agent_type
        
    def take_action(self, moves, moves_dict, game_state=None):
        if self.agent_type == "human":
            action = input()
        else:
            action = self.policy(moves, moves_dict, game_state)
        return action
    
    def policy(self, moves, moves_dict, game_state):
        if game_state is None: # Computer blindly makes random moves
            choice = np.random.choice(moves)
            return moves_dict[choice]
        else:
            pass
    
    def MCTS(self, starting_state, n=1600):
        game = Game()
        game.matrix = starting_state
        for i in range(n):
            pass
        options = []
        return options
        
        
        

