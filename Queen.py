import pieces as pi


class Queen(pi.pieces):

    def __init__(self, color, pos):
        pi.pieces.__init__(self, pos)
        self.color = color
        self.kind = "Q"
        return

    def select_piece(self, Board):
        x = self.pos[0]
        y = self.pos[1]

        for i in range(1, 8):
            if x+i > 7:
                break
            print(x+i, y, Board.board[x+i][y].kind, Board.board[x+i][y].color)
            if Board.board[x+i][y].color != 'non':
                if Board.board[x+i][y].color != self.color:
                    self.selecMove.add((x+i, y))
                break
            self.selecMove.add((x+i, y))
        for i in range(1, 8):
            if x-i < 0:
                break
            print(x-i, y, Board.board[x-i][y].kind, Board.board[x-i][y].color)
            if Board.board[x-i][y].color != 'non':
                if Board.board[x-i][y].color != self.color:
                    self.selecMove.add((x-i, y))
                break
            self.selecMove.add((x-i, y))
        for i in range(1, 8):
            if y-i < 0:
                break
            print(x, y-i, Board.board[x][y-i].kind, Board.board[x][y-i].color)
            if Board.board[x][y-i].color != 'non':
                if Board.board[x][y-i].color != self.color:
                    self.selecMove.add((x, y-i))
                break
            self.selecMove.add((x, y-i))
        for i in range(1, 8):
            if y+i > 7:
                break
            print(x, y+i, Board.board[x][y+i].kind, Board.board[x][y+i].color)
            if Board.board[x][y+i].color != 'non':
                if Board.board[x][y+i].color != self.color:
                    self.selecMove.add((x, y+i))
                break
            self.selecMove.add((x, y+i))
        print(self.selecMove)

        for i in range(1, 8):
            if y+i > 7 or x+i > 7:
                break
            if Board.board[x+i][y+i].color != 'non':
                if Board.board[x+i][y+i].color != self.color:
                    self.selecMove.add((x+i, y+i))
                break
            self.selecMove.add((x+i, y+i))

        for i in range(1, 8):
            if y-i < 0 or x-i < 0:
                break
            if Board.board[x-i][y-i].color != 'non':
                if Board.board[x-i][y-i].color != self.color:
                    self.selecMove.add((x-i, y-i))
                break
            self.selecMove.add((x-i, y-i))

        for i in range(1, 8):
            if y+i > 7 or x-i < 0:
                break
            if Board.board[x-i][y+i].color != 'non':
                if Board.board[x-i][y+i].color != self.color:
                    self.selecMove.add((x-i, y+i))
                break
            self.selecMove.add((x-i, y+i))

        for i in range(1, 8):
            if y-i < 0 or x+i > 7:
                break
            if Board.board[x+i][y-i].color != 'non':
                if Board.board[x+i][y-i].color != self.color:
                    self.selecMove.add((x+i, y-i))
                break
            self.selecMove.add((x+i, y-i))

        print(self.selecMove)
        return self.selecMove
