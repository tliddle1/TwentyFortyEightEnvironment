import random
import logic

class Game():
    def __init__(self):
        self.commands = {1: logic.up, 
                         2: logic.down,
                         3: logic.left, 
                         4: logic.right}
        self.init_matrix()

    def gen(self):
        return random.randint(0, 3)

    def init_matrix(self):
        self.matrix = logic.new_game(4)
        self.history_matrixs = list()
        self.matrix = logic.add_two(self.matrix)
        self.matrix = logic.add_two(self.matrix)
        

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
            self.matrix = logic.add_two(self.matrix)
                # record last move
            self.history_matrixs.append(self.matrix)

    def generate_next(self):
        index = (self.gen(), self.gen())
        while self.matrix[index[0]][index[1]] != 0:
            index = (self.gen(), self.gen())
        self.matrix[index[0]][index[1]] = 2

    def score(self):
        return logic.score(self.matrix)

game = Game()
game.print_matrix()
while(logic.game_state(game.matrix) != 'lose'):
    move = input()
    if (move == "w"):
        game.take_action(1)
    if (move == "s"):
        game.take_action(2)
    if (move == "a"):
        game.take_action(3)
    if (move == "d"):
        game.take_action(4)
    #moves = logic.possible_actions(game.matrix)
    #action = random.randint(0, len(moves)-1)
    #game.take_action(moves[action])
    game.print_matrix()
print(game.score())
