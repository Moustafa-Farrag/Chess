from colorama import Fore, init
import pieces as pi
import board as bo
import player as pl
import os

init(autoreset=True)


def create_board():

    player1Name = input("enter player1 name: ")
    player2Name = input("enter player2 name: ")

    player1 = pl.player(player1Name, "white")
    player2 = pl.player(player2Name, "black")

    r, c = (8, 8)
    EasyForIf = {1: "P", 2: "R", 3: "H", 4: "B", 5: "K", 6: "Q", 0: "E"}
    b = list()
    for i in range(r):
        rr = list()
        for j in range(c):
            if i < 2:
                one = pi.pieces("black", (i, j), "P")
                player1.add_piece(one)
            elif i > 5:
                one = pi.pieces("white", (i, j), "P")
                player2.add_piece(one)
            else:
                one = pi.pieces("non", (i, j), "-")

            rr.append(one)

        b.append(rr)

    for i in range(3):
        b[0][i].kind = EasyForIf[i+2]
        b[0][7-i].kind = EasyForIf[i+2]
        b[7][i].kind = EasyForIf[i+2]
        b[7][7-i].kind = EasyForIf[i+2]

    b[0][4].kind = EasyForIf[5]
    b[0][3].kind = EasyForIf[6]
    b[7][4].kind = EasyForIf[5]
    b[7][3].kind = EasyForIf[6]
    myBoard = bo.Board(b, player1, b[0][4], b[7][4])
    counter = 0
    while True:

        if counter % 2 == 0:
            myBoard.currentPlayer = player1
            print(Fore.RED + "turn of :" + player1.name)
        else:
            myBoard.currentPlayer = player2
            print(Fore.BLUE + "turn of :" + player2.name)

        print("   1 2 3 4 5 6 7 8")
        for i in range(8):
            for j in range(8):
                if j == 0:
                    print(chr(ord('a') + i) + ")", end=' ')
                if b[i][j].color == "white":
                    print(Fore.RED + b[i][j].kind, end=' ')
                elif b[i][j].color == "black":
                    print(Fore.BLUE + b[i][j].kind, end=' ')
                else:
                    print(b[i][j].kind, end=' ')
            print(" ")

        # print(myBoard.selecMove)
        myInput = input("enter your order: ")
        arrIn = myInput.split(":")
        if arrIn[0] == "s":
            InP = arrIn[1].strip().split(" ")
            x = ord(InP[0]) - ord('a')
            myBoard.select((x, int(InP[1]) - 1))
        elif arrIn[0] == "m":
            InP = arrIn[1].strip().split(" ")
            done = False
            if counter % 2 == 0:
                x = ord(InP[0]) - ord('a')
                done = myBoard.moveTo((x, int(InP[1]) - 1), player2)
            else:
                x = ord(InP[0]) - ord('a')
                done = myBoard.moveTo((x, int(InP[1]) - 1), player1)

            if done is True:
                counter += 1
        elif arrIn[0] == "stop":
            break

        os.system('cls' if os.name == 'nt' else 'clear')
    return


create_board()
