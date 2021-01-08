"""
Your task is to use:
    -lists,
    -printing,
    -conditions, and other skills
, to make a "Noughts and Crosses" kind of game, with text visualisation of the board.
"""

board = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]   # The board

stage = 0

def printBoard(tabl):
    for y in range(0, len(tabl), 1):
        print(*board[y], sep='|')

def indx(num):
    if (num - 1) < 3:
        return {'x': num - 1, 'y': 0}
    elif (num - 1) < 6:
        return {'x': num - 4, 'y': 1}
    else:
        return {'x': num - 7, 'y': 2}  # Return pos

def won():
    for y in range(0, len(board), 1):  # Check rows
        if board[y][0] == board[y][1] and board[y][1] == board[y][2] and board[y][0] != '_':
            return board[y][0]  # Who won
    for x in range(0, len(board), 1):  # Check columns
        if board[0][x] == board[1][x] and board[1][x] == board[2][x] and board[0][x] != '_':
            return board[0][x]
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != '_':  # Check diagonals
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != '_':  # Check diagonals
        return board[0][0]
    return 'n'


while True:
    if stage == 0 or stage == 2:  # show the board
        printBoard(board)
        stage += 1
        if stage > 3:
            stage = 0
    elif stage == 1:  # The first player's move: X
        if won() != 'n':
            print(won() + ' has won!')
            wantsTo = input('Want to play again? (y/n): ').lower()
            if wantsTo == 'n':
                break
            else:
                board = [['_', '_', '_'],
                         ['_', '_', '_'],
                         ['_', '_', '_']]
                stage = 0
        else:
            if not any('_' in x for x in board):
                print("It's a draw!")
                wantsTo = input('Want to play again? (y/n): ').lower()
                if wantsTo == 'n':
                    break
                else:
                    board = [['_', '_', '_'],
                             ['_', '_', '_'],
                             ['_', '_', '_']]
                    stage = -1
        ps = True
        nextMove = int(input('X please put your square choice: '))
        chk = indx(nextMove)
        if board[chk['y']][chk['x']] != '_':
            ps = False
        if ps:
            board[chk['y']][chk['x']] = 'X'
            stage += 1
        if stage > 3:
            stage = 0
    elif stage == 3:  # The second player's move: O
        if won() != 'n':
            print(won() + ' has won!')
            wantsTo = input('Want to play again? (y/n): ').lower()
            if wantsTo == 'n':
                break
            else:
                board = [['_', '_', '_'],
                         ['_', '_', '_'],
                         ['_', '_', '_']]
                stage = -1
        else:
            if not any('_' in x for x in board):
                print("It's a draw!")
                wantsTo = input('Want to play again? (y/n): ').lower()
                if wantsTo == 'n':
                    break
                else:
                    board = [['_', '_', '_'],
                             ['_', '_', '_'],
                             ['_', '_', '_']]
                    stage = 0
        ps = True
        nextMove = int(input('O please put your square choice: '))
        chk = indx(nextMove)
        if board[chk['y']][chk['x']] != '_':
            ps = False

        if ps:
            board[chk['y']][chk['x']] = 'O'
            stage += 1
            if stage > 3:
                stage = 0