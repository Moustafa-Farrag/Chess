# whate is the err


class pieces:

    def __init__(self, color, pos, kind):
        self.color = color
        self.pos = pos
        self.kind = kind
        self.firstMove = False
        return

    def move_piece(self, pos):
        self.pos = pos
        self.firstMove = True
        return

    def select_piece(self, pos):
        pass

    def __str__(self):
        return self.kind


# self.color + " " + str(self.pos) + " " + self.kind

class player:

    def __init__(self, name, color):
        self.Allpieces = set()
        self.name = name
        self.color = color
        self.time = 0
        return

    def remove_piece(self, pieces):
        self.Allpieces.discard(pieces)
        return

    def add_piece(self, pieces):
        self.Allpieces.add(pieces)
        return


class Board:

    def __init__(self, board,  currentPlayer):
        self.currentPlayer = currentPlayer
        self.board = board
        self.selPiece = pieces("non", (0, 0), "-")
        self.selecMove = set()
        return

    def set_currentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
        return

    def moveTo(self, pos):
        if self.selPiece.color == "non":
            return
        if pos in self.selecMove:
            pos1 = self.selPiece.pos
            self.selPiece.move_piece(pos)
            self.board[pos[0]][pos[1]].move_piece(pos1)
            if self.board[pos[0]][pos[1]].color == "non":
                temp = self.board[pos[0]][pos[1]]
                self.board[pos[0]][pos[1]] = self.selPiece
                self.board[pos1[0]][pos1[1]] = temp
                print("non")
                pass
        return

    def changeSecBoard(self):
        for i in self.selecMove:
            if self.board[i[0]][i[1]].color == "non":
                self.board[i[0]][i[1]].kind = "*"

    def resetSecBoard(self):
        for i in self.selecMove:
            if self.board[i[0]][i[1]].color == "non":
                self.board[i[0]][i[1]].kind = "-"

    def select(self, pos1):
        x, y = pos1
        self.resetSecBoard()
        self.selecMove.clear()
        if self.board[pos1[0]][pos1[1]].kind == "P":
            self.sPawn(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "K":
            self.sKing(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "R":
            self.sRook(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "Q":
            self.sQueen(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "H":
            self.sKinght(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "B":
            self.sBishop(x, y)
        print(self.selecMove)
        self.changeSecBoard()
        self.selPiece = self.board[pos1[0]][pos1[1]]
        return

    def check_limits(self):
        deleted = list()
        for i in self.selecMove:
            if i[0] < 0 or i[0] > 7:
                deleted.append(i)
            elif i[1] < 0 or i[1] > 7:
                deleted.append(i)

        for i in deleted:
            self.selecMove.discard(i)

        return

    def sPawn(self, x, y):
        p = self.board[x][y]
        if p.color == "white":
            print("white")
            if self.board[x-1][y].color == "non":
                self.selecMove.add((x-1, y))
                if self.board[x-1][y].color == "non":
                    self.selecMove.add((x-1, y))
            if self.board[x-1][y-1].color == "black":
                self.selecMove.add((x-1, y-1))
            if self.board[x-1][y+1].color == "black":
                self.selecMove.add((x-1, y+1))
        elif p.color == "black":
            if self.board[x+1][y].color == "non":
                self.selecMove.add((x+1, y))
                if self.board[x+2][y].color == "non":
                    self.selecMove.add((x+2, y))
            if self.board[x+1][y-1].color == "white":
                self.selecMove.add((x+1, y-1))
            if self.board[x+1][y+1].color == "white":
                self.selecMove.add((x+1, y+1))
        return

    def sKinght(self, x, y):
        newX = x - 2
        newY = y + 1
        self.selecMove.add((newX, newY))
        newY = y - 1
        self.selecMove.add((newX, newY))
        # first one
        newX = x + 2
        newY = y + 1
        self.selecMove.add((newX, newY))
        newY = y - 1
        self.selecMove.add((newX, newY))
        # first two
        newY = y + 2
        newX = x + 1
        self.selecMove.add((newX, newY))
        newX = x - 1
        self.selecMove.add((newX, newY))
        # fitst three
        newY = y - 2
        newX = x + 1
        self.selecMove.add((newX, newY))
        newX = x - 1
        self.selecMove.add((newX, newY))
        self.check_limits()
        print(self.selecMove)
        pass
        return

    def sRook(self, x, y):
        for i in range(8):
            if x+i > 7:
                break
            if self.board[x+i][y].color != 'non':
                if self.board[x+i][y].color != self.board[x][y].color:
                    self.selecMove.add((x+i, y))
                break
            self.selecMove.add((x+i, y))
        for i in range(8):
            if x-i < 0:
                break
            if self.board[x-i][y].color != 'non':
                if self.board[x-i][y].color != self.board[x][y].color:
                    self.selecMove.add((x-i, y))
                break
            self.selecMove.add((x-i, y))
        for i in range(8):
            if y-i < 0:
                break
            if self.board[x][y-i].color != 'non':
                if self.board[x][y-i].color != self.board[x][y].color:
                    self.selecMove.add((x, y-i))
                break
            self.selecMove.add((x, y-i))
        for i in range(8):
            if y+i > 7:
                break
            if self.board[x][y+i].color != 'non':
                if self.board[x][y+i].color != self.board[x][y].color:
                    self.selecMove.add((x, y+i))
                break
            self.selecMove.add((x, y+i))
        print(self.selecMove)
        return

    def sBishop(self, x, y):
        for i in range(8):
            if y+i > 7 or x+i > 7:
                break
            if self.board[x+i][y+i].color != 'non':
                if self.board[x+i][y+i].color != self.board[x][y].color:
                    self.selecMove.add((x+i, y+i))
                break
            self.selecMove.add((x+i, y+i))

        for i in range(8):
            if y-i < 0 or x-i < 0:
                break
            if self.board[x-i][y-i].color != 'non':
                if self.board[x-i][y-i].color != self.board[x][y].color:
                    self.selecMove.add((x-i, y-i))
                break
            self.selecMove.add((x-i, y-i))

        for i in range(8):
            if y+i > 7 or x-i < 0:
                break
            if self.board[x-i][y+i].color != 'non':
                if self.board[x-i][y+i].color != self.board[x][y].color:
                    self.selecMove.add((x-i, y+i))
                break
            self.selecMove.add((x-i, y+i))

        for i in range(8):
            if y-i < 0 or x+i > 7:
                break
            if self.board[x+i][y-i].color != 'non':
                if self.board[x+i][y-i].color != self.board[x][y].color:
                    self.selecMove.add((x+i, y-i))
                break
            self.selecMove.add((x+i, y-i))

        print(self.selecMov)
        return

    def sQueen(self, x, y):
        self.sRook(x, y)
        self.sBishop(x, y)
        return

    def sKing(self, x, y):
        self.selecMove.add((x+1, y))
        self.selecMove.add((x-1, y))
        self.selecMove.add((x, y+1))
        self.selecMove.add((x, y-1))
        self.selecMove.add((x-1, y-1))
        self.selecMove.add((x+1, y-1))
        self.selecMove.add((x+1, y+1))
        self.selecMove.add((x-1, y+1))
        self.check_limits()
        print(self.selecMove)
        return


def create_board():

    player1Name = input("enter player1 name: ")
    player2Name = input("enter player2 name: ")

    player1 = player(player1Name, "white")
    player2 = player(player2Name, "balck")

    r, c = (8, 8)
    EasyForIf = {1: "P", 2: "R", 3: "H", 4: "B", 5: "K", 6: "Q", 0: "E"}
    b = list()
    for i in range(r):
        rr = list()
        for j in range(c):
            if i < 2:
                one = pieces("black", (i, j), "P")
                player1.add_piece(one)
            elif i > 5:
                one = pieces("white", (i, j), "P")
                player2.add_piece(one)
            else:
                one = pieces("non", (i, j), "-")

            rr.append(one)

        b.append(rr)

    for i in range(3):
        b[0][i].kind = EasyForIf[i+2]
        b[0][7-i].kind = EasyForIf[i+2]
        b[7][i].kind = EasyForIf[i+2]
        b[7][7-i].kind = EasyForIf[i+2]

    myBoard = Board(b, player1)
    while True:
        for i in range(8):
            for j in range(8):
                print(b[i][j], end=' ')
            print(" ")

        print(myBoard.selecMove)
        i = int(input("enter selected: "))
        j = int(input("enter selected: "))
        myBoard.select((i, j))

    return


create_board()
