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
for turn in range(1, 10):
    # If turn is even number then the character is circle.
    # If turn is odd number then the character is x.
    if (turn % 2) == 0:
        character = '0'
    else:
        character = 'X'

    userInput = input("input a number from 1 to 9.")
    theBoard[userInput] = character
    printBoard(theBoard)

# bugs
# 1. Cannot replace existing characters
# 2. When get 3 in a row, gets win and stops game.