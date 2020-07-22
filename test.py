from unittest.mock import patch
from unittest import TestCase
import random as r

def get_input():
    rand = range(1,9)
    return (str(r.choice(rand)))


import board as b
import our_ai as ai
import board as b
import our_ai as ai
from collections import defaultdict

def game():
    moves = defaultdict(dict)
    status=False
    turn = 'X'
    count = 0
    g = b.gameBoard.copy()
    vals = b.value.copy()
    for i in range(9999):
        b.printBoard(g)
        if status==True:
            #restart(g)
            break
        if turn == 'X':
            print("It's your turn," + turn + ".Move to which place?")
            val = 3
            move = get_input()
            moves[count]['Test']=move
        else:
            val = 5
            move = playai(vals,g)
            print("Ai played to place " + move)
            moves[count]['AI']=move


        if g[move] == ' ':
            g[move] = turn
            vals[str(move)] = val
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue


        if count >= 5:
            if g['7'] == g['8'] == g['9'] != ' ':  # across the top
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['4'] == g['5'] == g['6'] != ' ':  # across the middle
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['1'] == g['2'] == g['3'] != ' ':  # across the bottom
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['1'] == g['4'] == g['7'] != ' ':  # down the left side
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['2'] == g['5'] == g['8'] != ' ':  # down the middle
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['3'] == g['6'] == g['9'] != ' ':  # down the right side
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['7'] == g['5'] == g['3'] != ' ':  # diagonal
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break
            elif g['1'] == g['5'] == g['9'] != ' ':  # diagonal
                b.printBoard(g)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                status = True
                break

            moves[count]['winner']=turn

                #Tie.
        if count == 9:
            status=True
            print("\nGame Over.\n")
            print("It's a Tie!!")
            moves[count]['winner']="TIE"

        # Change
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

    print(moves)
            #Restart.
   # if (status==True):
    #    restart(g)

    return moves
def restart(g):
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in b.board_keys:
            g[key] = " "

        game()
def playai(vals,g):
    m =ai.ai(vals)
    move=str(m)
    if g[move] != ' ':
        playai(vals,g)
    return move

def test():
    for i in range(9):
        r = game()
        print(r)

if __name__ == "__main__":
    test()





