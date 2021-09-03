theBoard = {'1': ' ', '2': ' ', '3': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '7': ' ', '8': ' ', '9': ' '}

def printBoard(board):
    print(' {} | {} | {} '.format(board['1'], board['2'], board['3']))
    print('---+---+---')
    print(' {} | {} | {} '.format(board['4'], board['5'], board['6']))
    print('---+---+---')
    print(' {} | {} | {} '.format(board['7'], board['8'], board['9']))

printBoard(theBoard)

userInput = input("input a number from 1 to 9.")
print(userInput)

currentTurn = 'X'

theBoard[userInput] = "x"
printBoard(theBoard)