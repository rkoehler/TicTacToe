def createBoard (aBoard):
    for Line1 in range(0,3):
            print(aBoard[Line1], end = "")
    print()
    for Line2 in range(3,6):
            print(aBoard[Line2], end = "")
    print()
    for Line3 in range(6,9):
            print(aBoard[Line3], end = "")
    print()

def xGame (aBoard, pos , piece):
    aBoard[pos] = piece

def clearBoard (aBoard):
    for i in range(0,8):
        aBoard[i] = ' - '


def hasSpaces(aBoard):
    for i in range(0,9):
        if aBoard[i] == ' - ' :
            return True
    return False

def checkWinner (Board, piece):

    positionsToCheck = [[0,1,2],[3,4,5],[6,7,8],[0,4,8],[2,4,6],[0,3,6],[1,4,7],[2,5,8]]
    for charPos in positionsToCheck:
        if compareRow(Board[charPos[0]], Board[charPos[1]], Board[charPos[2]]):
            return True
    return False
def compareRow (one, two, three):
    if one == two and two == three:
        return True
    else:
        return False