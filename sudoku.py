BOARD_ROWS = 9

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(board):
    for row in range(BOARD_ROWS):
        if row != 0 and row % 3 == 0:
            print("- - - - - - - - -")

        for col in range(BOARD_ROWS):
            if col != 0 and col % 3 == 0:
                print("|", end="")

            if col == 8:
                print(board[row][col])
            else:
                print(str(board[row][col])+ " ", end="")

def find_empty(board):
    for row in range(BOARD_ROWS):
        for col in range(BOARD_ROWS):
            if board[row][col] == 0:
                return (row, col)
    return BOARD_ROWS, BOARD_ROWS

def checkrow(board, row, num):
    for col in range(BOARD_ROWS):
        if board[row][col] ==num:
            return False
    return True

def checkcol(board, col, num):
    for row in range(BOARD_ROWS):
        if board[row][col] ==num:
            return False
    return True

def checkbox(board, row, col, num):
    for i in range(3):
        for j in range(3):
            if board[row + i][col + j] == num:
                return False

    return True

def check(board, row, col, num):
    if checkrow(board, row, num) and checkcol(board, col, num) and checkbox(board, row - (row%3), col - (col%3), num):
        return True
    else:
        return False

def solvesudoku(board):
    row, col = find_empty(board)
    if row != BOARD_ROWS and col != BOARD_ROWS:
        for num in range(1,10):
                if check(board, row, col, num):
                    board[row][col] = num

                    if solvesudoku(board):
                        return True

                    board[row][col] = 0

    else:
        return True


print_board(board)
print("\n")
if solvesudoku(board):
    print("Sudoku has been solved.\nSolution:")

else:
    print("There is no solution.")

print_board(board)