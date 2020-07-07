# self.color + " " + str(self.pos) + " " + self.kind
import pieces as pi


class Board:

    def __init__(self, board,  currentPlayer):
        self.currentPlayer = currentPlayer
        self.board = board
        self.selPiece = pi.pieces("non", (0, 0), "-")
        self.selecMove = set()
        return

    def set_currentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
        return

    def moveTo(self, pos, player):
        if self.selPiece.color == "non":
            return
        print(self.selecMove, pos)
        if pos in self.selecMove:
            pos1 = self.selPiece.pos
            self.selPiece.move_piece(pos)
            self.board[pos[0]][pos[1]].move_piece(pos1)
            if self.board[pos[0]][pos[1]].color == "non":
                temp = self.board[pos[0]][pos[1]]
                self.board[pos[0]][pos[1]] = self.selPiece
                self.board[pos1[0]][pos1[1]] = temp
            else:
                temp = self.board[pos[0]][pos[1]]
                self.board[pos[0]][pos[1]] = self.selPiece
                self.board[pos1[0]][pos1[1]] = temp
                player.Allpieces.discard(temp)
                pass
            self.board[pos1[0]][pos1[1]].color = "non"
            self.board[pos1[0]][pos1[1]].kind = "-"
        self.resetSecBoard()
        self.selecMove.clear()
        return

    def changeSecBoard(self):
        for i in self.selecMove:
            if self.board[i[0]][i[1]].color == "non":
                self.board[i[0]][i[1]].kind = "*"

    def resetSecBoard(self):
        for i in self.selecMove:
            if self.board[i[0]][i[1]].color == "non":
                self.board[i[0]][i[1]].kind = "-"

    def checkColorMove(self, color):
        deleted = set()
        for i in self.selecMove:
            if self.board[i[0]][i[1]].color == color:
                deleted.add(i)
        for i in deleted:
            self.selecMove.discard(i)

    def select(self, pos1):
        if self.currentPlayer.color != self.board[pos1[0]][pos1[1]].color:
            return
        x, y = pos1
        self.resetSecBoard()
        self.selecMove.clear()
        if self.board[pos1[0]][pos1[1]].kind == "P":
            self.sPawn(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "K":
            self.sKing(x, y)
        elif self.board[pos1[0]][pos1[1]].kind == "R":
            print("ROOOOK")
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
                if self.board[x-2][y].color == "non":
                    if not self.board[x][y].firstMove:
                        self.selecMove.add((x-2, y))
            if self.board[x-1][y-1].color == "black":
                self.selecMove.add((x-1, y-1))
            if self.board[x-1][y+1].color == "black":
                self.selecMove.add((x-1, y+1))
        elif p.color == "black":
            if self.board[x+1][y].color == "non":
                self.selecMove.add((x+1, y))
                if self.board[x+2][y].color == "non":
                    if not self.board[x][y].firstMove:
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
        self.checkColorMove(self.board[x][y].color)
        print(self.selecMove)
        pass
        return

    def sRook(self, x, y):
        for i in range(1, 8):
            if x+i > 7:
                break
            print(x+i, y, self.board[x+i][y].kind, self.board[x+i][y].color)
            if self.board[x+i][y].color != 'non':
                if self.board[x+i][y].color != self.board[x][y].color:
                    self.selecMove.add((x+i, y))
                break
            self.selecMove.add((x+i, y))
        for i in range(1, 8):
            if x-i < 0:
                break
            print(x-i, y, self.board[x-i][y].kind, self.board[x-i][y].color)
            if self.board[x-i][y].color != 'non':
                if self.board[x-i][y].color != self.board[x][y].color:
                    self.selecMove.add((x-i, y))
                break
            self.selecMove.add((x-i, y))
        for i in range(1, 8):
            if y-i < 0:
                break
            print(x, y-i, self.board[x][y-i].kind, self.board[x][y-i].color)
            if self.board[x][y-i].color != 'non':
                if self.board[x][y-i].color != self.board[x][y].color:
                    self.selecMove.add((x, y-i))
                break
            self.selecMove.add((x, y-i))
        for i in range(1, 8):
            if y+i > 7:
                break
            print(x, y+i, self.board[x][y+i].kind, self.board[x][y+i].color)
            if self.board[x][y+i].color != 'non':
                if self.board[x][y+i].color != self.board[x][y].color:
                    self.selecMove.add((x, y+i))
                break
            self.selecMove.add((x, y+i))
        print(self.selecMove)
        return

    def sBishop(self, x, y):
        for i in range(1, 8):
            if y+i > 7 or x+i > 7:
                break
            if self.board[x+i][y+i].color != 'non':
                if self.board[x+i][y+i].color != self.board[x][y].color:
                    self.selecMove.add((x+i, y+i))
                break
            self.selecMove.add((x+i, y+i))

        for i in range(1, 8):
            if y-i < 0 or x-i < 0:
                break
            if self.board[x-i][y-i].color != 'non':
                if self.board[x-i][y-i].color != self.board[x][y].color:
                    self.selecMove.add((x-i, y-i))
                break
            self.selecMove.add((x-i, y-i))

        for i in range(1, 8):
            if y+i > 7 or x-i < 0:
                break
            if self.board[x-i][y+i].color != 'non':
                if self.board[x-i][y+i].color != self.board[x][y].color:
                    self.selecMove.add((x-i, y+i))
                break
            self.selecMove.add((x-i, y+i))

        for i in range(1, 8):
            if y-i < 0 or x+i > 7:
                break
            if self.board[x+i][y-i].color != 'non':
                if self.board[x+i][y-i].color != self.board[x][y].color:
                    self.selecMove.add((x+i, y-i))
                break
            self.selecMove.add((x+i, y-i))

        print(self.selecMove)
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
        self.checkColorMove(self.board[x][y].color)
        print(self.selecMove)
        return
