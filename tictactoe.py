# 0 at the beginning to make using indexed easier
field = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def showField():
    print('\n', field[1], field[2], field[3], '\n', field[4], field[5],
          field[6], '\n', field[7], field[8], field[9], '\n',)


def placeX(n):
    field[n] = 'X'


def placeO(n):
    field[n] = 'O'


def winCheck():
    gameOver = False
    if(field[1] == field[2] == field[3]):
        print("Player ", field[1], " won the game.")
        gameOver = True
    if(field[4] == field[5] == field[6]):
        print("Player ", field[4], " won the game.")
        gameOver = True
    if(field[7] == field[8] == field[9]):
        print("Player ", field[7], " won the game.")
        gameOver = True
    if(field[1] == field[5] == field[9]):
        print("Player ", field[1], " won the game.")
        gameOver = True
    if(field[3] == field[5] == field[7]):
        print("Player ", field[3], " won the game.")
        gameOver = True
    if(field[1] == field[4] == field[7]):
        print("Player ", field[1], " won the game.")
        gameOver = True
    if(field[2] == field[5] == field[8]):
        print("Player ", field[2], " won the game.")
        gameOver = True
    if(field[3] == field[6] == field[9]):
        print("Player ", field[3], " won the game.")
        gameOver = True
    if(gameOver):
        return True
    else:
        return False


def playGame():
    while(not winCheck()):
        showField()
        input1 = int(input(
            "Enter the location where you want to place your symbol: (free ones are marked with numbers)"))
        placeX(input1)
    showField()
    print('over.')


playGame()
