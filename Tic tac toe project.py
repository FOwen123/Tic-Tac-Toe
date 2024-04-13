board = [' ' for x in range(10)]

def insertletter(letter, pos):
    board[pos] = letter

def isspacefree(pos):
    return board[pos] == ' '

def printboard(board):
    print('    |    |')
    print(' ' + board[1] + '  | ' + board[2] + '  | ' + board[3])
    print('    |    |')
    print('---------------')
    print('    |    |')
    print(' ' + board[4] + '  | ' + board[5] + '  | ' + board[6])
    print('    |    |')
    print('---------------')
    print('    |    |')
    print(' ' + board[7] + '  | ' + board[8] + '  | ' + board[9])
    print('    |    |')

def winner(bo, le): # <-- bo=board and le=letter
    return (bo[1] == le and bo[2] == le and bo[3] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[1] == le and bo[4] == le and bo[7] == le) or (bo[2] == le and bo[5] == le and bo[8] == le) or (bo[3] == le and bo[5] == le and bo[9] == le) or (bo[1] == le and bo[5] == le and bo[9] == le) or (bo[3] == le and bo[5] == le and bo[7] == le)

def playermove():
    run = True
    while run:
        move = input("Please select a position to place an \'X\' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if isspacefree(move):
                    run = False
                    insertletter('X', move)
                else:
                    print("Sorry, this place is occupied!")
            else:
                print("Please type a number within the range!")
        except:
            print("Please type a number!")


def compmove():
    possiblemoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for x in possiblemoves:
            boardCopy = board[:]
            boardCopy[x] = let
            if winner(boardCopy, let):
                move = x 
                return move
    
    cornersOpen = []
    for x in possiblemoves:
        if x in [1, 3, 7, 9]:
            cornersOpen.append(x)

    if len(cornersOpen) > 0:
        move = selectrandom(cornersOpen)
        return move

    if 5 in possiblemoves:
        move = 5
        return move

    edgesOpen = []
    for x in possiblemoves:
        if x in [2, 4, 6, 8]:
            edgesOpen.append(x)

    if len(edgesOpen) > 0:
        move = selectrandom(edgesOpen)
        
    return move

def selectrandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isboardfull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print("Welcome to Tic Tac Toe!")
    start_game = input("Do you want to play the game(yes/no)?")
    if start_game == "Yes" or "yes":
        printboard(board)

        while not(isboardfull(board)):
            if not(winner(board, "O")):
                playermove()
                printboard(board)
            else:
                print("Sorry, O\'s won this time!")
                break

            if not(winner(board, "X")):
                move = compmove()
                if move == 0:
                    print("Tie Game!")
                else:
                    insertletter('O', move)
                    print("Computer placed an \'O\' in position", move, ":")
                    printboard(board)
            else:
                print("X\'s won this time! Good job!")
                break

        if isboardfull(board):
            print("Tie Game!")
    else:
        print("Bye....")

if __name__ == "__main__":
    main()