import Game

class game_state():
    def __init__(self, mat):
        self.state = []        
        for e in range(1,16):
            matrix = []
            for i in range(4):
                column = []
                for j in range(4):
                    if mat[i][j] == 2**e:
                        column.append(1)
                    else:
                        column.append(0)
                matrix.append(column)
            self.state.append(matrix)
        #Prints the game state (all 16 layers)
        """
        for i in range(0,15):
            print(2**(i+1))
            for j in range(0,4):
                print(self.state[i][j])
                print("\n")
        """

    def ones_to_nums(self):
        matrix = []
        for i in range(4):
            matrix.append([0] * 4)
        for i in range(0,15):
            for j in range(0,4):
                for k in range(0,4):
                    if self.state[i][j][k] == 1:
                        matrix[j][k] = 2**(i+1)
        return matrix
                