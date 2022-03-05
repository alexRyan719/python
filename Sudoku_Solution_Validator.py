# Level 4 Kata - Code Wars
# Sudoku Background
# Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9, so that each column, each row, and each of the
# nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
# (More info at: http://en.wikipedia.org/wiki/Sudoku)

# Sudoku Solution Validator
# Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board, and returns true if it is a valid solution, or
# false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid
# solutions.

# The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.

# Examples
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2],
#   [6, 7, 2, 1, 9, 5, 3, 4, 8],
#   [1, 9, 8, 3, 4, 2, 5, 6, 7],
#   [8, 5, 9, 7, 6, 1, 4, 2, 3],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 6, 1, 5, 3, 7, 2, 8, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 4, 5, 2, 8, 6, 1, 7, 9]
# ]); // => true
# validSolution([
#   [5, 3, 4, 6, 7, 8, 9, 1, 2], 
#   [6, 7, 2, 1, 9, 0, 3, 4, 8],
#   [1, 0, 0, 3, 4, 2, 5, 6, 0],
#   [8, 5, 9, 7, 6, 1, 0, 2, 0],
#   [4, 2, 6, 8, 5, 3, 7, 9, 1],
#   [7, 1, 3, 9, 2, 4, 8, 5, 6],
#   [9, 0, 1, 5, 3, 7, 2, 1, 4],
#   [2, 8, 7, 4, 1, 9, 6, 3, 5],
#   [3, 0, 0, 4, 8, 1, 1, 7, 9]
# ]); // => false


def check(group):
    if 1 in group and 2 in group and 3 in group and 4 in group and 5 in group and 6 in group and 7 in group and 8 in group and 9 in group:
        return True
    else:
        return False

def valid_solution(board):
    # Declare variables.
    is_valid = True
    test_group = []
    width = 9
    height = 9
    x = 0
    y = 0
    
    # Check rows.
    for group in board:
        if not check(group):
            is_valid = False
        if 0 in group:
            is_valid = False
    
    # Check columns.
    while x < width:
        while y < height:
            test_group.append(board[y][x])
            y += 1
        if not check(test_group):
            is_valid = False
        x += 1
        y = 0
        test_group = []
        
    # Check sub-grids 1-9.
    # Check sub-grid 1.
    x = 0
    y = 0
    while y < 3:
        while x < 3:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 0
    if not check(test_group):
        is_valid = False
    test_group = [] 

    # Check sub-grid 2.
    x = 3
    y = 0
    while y < 3:
        while x < 6:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 3
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 3.
    x = 6
    y = 0
    while y < 3:
        while x < 9:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 6
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 4.
    x = 0
    y = 3
    while y < 6:
        while x < 3:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 0
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 5.
    x = 3
    y = 3
    while y < 6:
        while x < 6:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 3
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 6.
    x = 6
    y = 3
    while y < 6:
        while x < 9:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 6
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 7.
    x = 0
    y = 6
    while y < 9:
        while x < 3:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 0
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 8.
    x = 3
    y = 6
    while y < 9:
        while x < 6:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 3
    if not check(test_group):
        is_valid = False
    test_group = []
    
    # Check sub-grid 9.
    x = 6
    y = 6
    while y < 9:
        while x < 9:
            test_group.append(board[x][y])
            x += 1
        y += 1
        x = 6
    if not check(test_group):
        is_valid = False
    test_group = []
    
    return is_valid
