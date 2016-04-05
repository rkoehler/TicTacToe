#Robert 2/23/16
#TicTacToe
#create a tictactoe board
#Top left is pos 0 bottom right is pos 8
#prompt user where they want to input an "0"
# replace space with "0"

import TTTLib

Board = [' - ',' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ', ' - ']

menuSelection = "-2"


while menuSelection != "3":
    print("Main Menu: ")
    print()
    print('1. Single Player')
    print('2. Two players')
    print('3. Quit')
    menuSelection = input('Please select a number: ')

    
    while menuSelection =="1":
        piece = 'X'
        TTTLib.createBoard(Board)
        pos = int(input("Please give me a number from 0 to 8 or press 9 to clear the board: "))
        if pos >= 0 and pos <= 8:
            TTTLib.xGame(Board, pos, piece)
            print()
        elif pos == 9:
            TTTLib.clearBoard(Board)
        else:
            print('Your number does not fall within that range.')

        if not hasSpaces(Board):
            menuSelection = '-2'
            TTTLib.createBoard(Board)
            print('All the spaces are filled. Game Over!')
    
    while menuSelection == "2":
        playingGame = True
        print("Who goes first?")
        firstTurn = input("X or O: ")
        while playingGame == True: 
            TTTLib.createBoard(Board)
            if TTTLib.checkWinner (Board, firstTurn):
                print("Someone won")
                    #print winner
                    #kick out to main menu
            pos = int(input("Please give me a number from 0 to 8 or press 9 to clear the board: "))
            if 0 <= pos and pos <= 8:
                TTTLib.xGame(Board, pos, firstTurn)#or oGame(Board,pos)
                print()
                if firstTurn == 'X':
                    firstTurn = 'O'

                else:
                    firstTurn = "X"
            elif pos == 9:
                TTTLib.clearBoard(Board)
            else:
                print('Your number does not fall within that range.')
       
                
            if not TTTLib.hasSpaces(Board):
                    menuSelection = '-2'
                    TTTLib.createBoard(Board)
                    print('All the spaces are filled. Game Over!')
                    playingGame = False
 

        

        #O's would be the same except oGame instead of xGame


#figure out what the fuction to clear the screen is
#add validation to input DONE
#figure out how to write a loop so we play all turns
#figure out how to alternate turns
