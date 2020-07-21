gameBoard = {'7': ' ', '8': ' ', '9': ' ',
             '4': ' ', '5': ' ', '6': ' ',
             '1': ' ', '2': ' ', '3': ' '}

value_c = gameBoard.copy

#value = {k: 0 if not v else v for k, v in gameBoard.values()}

value = {'7': 0, '8': 0, '9': 0,
             '4': 0, '5': 0, '6': 0,
             '1': 0, '2': 0, '3': 0}
board_keys = []

for key in gameBoard:
    board_keys.append(key)


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

