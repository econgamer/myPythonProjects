import itertools

boardPos = [0,1,2,3,4,5,6,7,8]

player1Turn = True;

while True:

    #For display - simple
    it = iter(boardPos)
    for x in it:
        # print ([x, next(it), next(it)])
        print (x,'|', next(it),'|', next(it))
        print ('---------')



    if player1Turn:
        try:
            player1Input = int(input('Player1, What is your prefer position?'))
            player1Turn = False
            if(boardPos[player1Input] != "O" and boardPos[player1Input] != "X"):
                print(boardPos[player1Input])
                boardPos[player1Input] = "O";
                print("Yea")
            else:
                print("It has been occupied")
                player1Turn = True
                continue
        except:
            print("Please type in valid number")
            continue

    else:
        try:
            player2Input = int(input('Player2, What is your prefer position?'))
            player1Turn = True
            if(boardPos[player2Input] != "O" and boardPos[player2Input] != "X"):
                print(boardPos[player2Input])
                boardPos[player2Input] = "X";
                print("Yea")
            else:
                print("It has been occupied")
                player1Turn = False
                continue
        except:
            print("Please type in valid number")
            continue


    if(boardPos[0] == boardPos[1] == boardPos[2]
    or boardPos[3] == boardPos[4] == boardPos[5]
    or boardPos[6] == boardPos[7] == boardPos[8]
    or boardPos[0] == boardPos[3] == boardPos[6]
    or boardPos[1] == boardPos[4] == boardPos[7]
    or boardPos[2] == boardPos[0] == boardPos[8]
    or boardPos[0] == boardPos[4] == boardPos[8]
    or boardPos[2] == boardPos[4] == boardPos[6]):
        if(player1Turn):
            print('Player2 win!!!')
            break
        else:
            print('Player1 win!!!')
            break
