
import random

def new_game(n):
    matrix = []

    for i in range(n):
        matrix.append([0] * n)
    return matrix

def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while(mat[a][b] != 0):
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 2
    return mat

def add_four(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)
    while(mat[a][b] != 0):
        a = random.randint(0, len(mat)-1)
        b = random.randint(0, len(mat)-1)
    mat[a][b] = 4
    return mat

def add_tile(mat):
    chance = random.randint(1,10)
    if chance == 1:
        return add_four(mat)    
    else:
        return add_two(mat)

def score(mat):
    """returns the current score of the game given the current matrix"""
    score = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            switcher = {
                2: 0, 
                4: 4, 
                8: 16, 
                16: 48, 
                32: 128, 
                64: 320, 
                128: 768, 
                256: 1792, 
                512: 4096, 
                1024: 9216, 
                2048: 20480, 
                4096: 45056, 
                8192: 98304, 
                16384: 212992, 
                32768: 458752, 
                65536: 983040
            }
            score += switcher.get(mat[i][j], 0)
    return score

def possible_actions(mat):
    """returns the possible actions that can be taken to change the game state given the current matrix"""
    #Check right
    moves = []
    if (check_up(mat)):
        moves.append(1)
    if (check_down(mat)):
        moves.append(2)
    if (check_left(mat)):
        moves.append(3)
    if (check_right(mat)):
        moves.append(4)
    return moves
    
    

def check_right(mat):
    for row in range(len(mat)):
        if mat[row][0] != 0 and (mat[row][1] == 0 or mat[row][1] == mat[row][0]):
            return True
        elif mat[row][1] != 0 and (mat[row][2] == 0 or mat[row][2] == mat[row][1]):
            return True
        elif mat[row][2] != 0 and (mat[row][3] == 0 or mat[row][3] == mat[row][2]):
            return True
    return False

def check_down(mat):
    for row in range(len(mat)):
        if mat[0][row] != 0 and (mat[1][row] == 0 or mat[1][row] == mat[0][row]):
            return True
        elif mat[1][row] != 0 and (mat[2][row] == 0 or mat[2][row] == mat[1][row]):
            return True
        elif mat[2][row] != 0 and (mat[3][row] == 0 or mat[3][row] == mat[2][row]):
            return True
    return False

def check_left(mat):
    for row in range(len(mat)):
        if mat[row][3] != 0 and (mat[row][2] == 0 or mat[row][2] == mat[row][3]):
            return True
        elif mat[row][2] != 0 and (mat[row][1] == 0 or mat[row][1] == mat[row][2]):
            return True
        elif mat[row][1] != 0 and (mat[row][0] == 0 or mat[row][0] == mat[row][1]):
            return True
    return False

def check_up(mat):
    for row in range(len(mat)):
        if mat[3][row] != 0 and (mat[2][row] == 0 or mat[2][row] == mat[3][row]):
            return True
        elif mat[2][row] != 0 and (mat[1][row] == 0 or mat[1][row] == mat[2][row]):
            return True
        elif mat[1][row] != 0 and (mat[0][row] == 0 or mat[0][row] == mat[1][row]):
            return True
    return False

def game_state(mat):
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
    for i in range(len(mat)):  # check for any zero entries
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                return 'not over'
    for k in range(len(mat)-1):  # to check the left/right entries on the last row
        if mat[len(mat)-1][k] == mat[len(mat)-1][k+1]:
            return 'not over'
    for j in range(len(mat)-1):  # check up/down entries on last column
        if mat[j][len(mat)-1] == mat[j+1][len(mat)-1]:
            return 'not over'
    return 'lose'

def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            new[i].append(mat[i][len(mat[0])-j-1])
    return new

def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

def cover_up(mat):
    new = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    done = False
    for i in range(4):
        count = 0
        for j in range(4):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return (new, done)

def merge(mat):
    done = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                done = True
    return (mat, done)

def up(game):
    # return matrix after shifting up
    game = transpose(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(game)
    return (game, done)

def down(game):
    game = reverse(transpose(game))
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(reverse(game))
    return (game, done)

def left(game):
    # return matrix after shifting left
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    return (game, done)

def right(game):
    # return matrix after shifting right
    game = reverse(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = reverse(game)
    return (game, done)
