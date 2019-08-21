import Game
import numpy as np


def get_layered_state(mat):
    state = []
    for e in range(1, 16):
        matrix = []
        for i in range(4):
            column = []
            for j in range(4):
                if mat[i][j] == 2 ** e:
                    column.append(1)
                else:
                    column.append(0)
            matrix.append(column)
        state.append(matrix)
    return np.array(state)
    # Prints the game state (all 16 layers)


def ones_to_nums(self, layered_state):
    matrix = []
    for i in range(4):
        matrix.append([0] * 4)
    for i in range(0, 15):
        for j in range(0, 4):
            for k in range(0, 4):
                if layered_state[i][j][k] == 1:
                    matrix[j][k] = 2 ** (i + 1)
    return matrix


if __name__ == '__main__':
    mat = np.zeros((4, 4))
    mat[1, 1] = 2048
    print(get_layered_state(mat))