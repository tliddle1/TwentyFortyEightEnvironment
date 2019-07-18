import random
import logic

class Game():
    def __init__(self):
        self.commands = {1: logic.up, 
                         2: logic.down,
                         3: logic.left, 
                         4: logic.right}
        self.moves_dict = {1: "w", 
                           2: "s",
                           3: "a", 
                           4: "d"}
        self.init_matrix()

    def gen(self):
        return random.randint(0, 3)

    def init_matrix(self):
        self.matrix = logic.new_game(4)
        self.history_matrixs = list()
        self.matrix = logic.add_tile(self.matrix)
        self.matrix = logic.add_tile(self.matrix)
        

    def print_matrix(self):
        print(self.matrix[0])
        print(self.matrix[1])
        print(self.matrix[2])
        print(self.matrix[3])
        print("\n")

    def take_action(self, action_number):
        if action_number in self.commands:
            self.matrix, done = self.commands[action_number](self.matrix)
        if done:    
            self.matrix = logic.add_tile(self.matrix)
                # record last move
            self.history_matrixs.append(self.matrix)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2

    def score(self):
        return logic.score(self.matrix)
    
    def isGameOver(self):
        if logic.game_state(self.matrix) == 'lose':
            return True
        else:
            return False

    def possible_moves(self):
        return logic.possible_actions(self.matrix)
  
    
