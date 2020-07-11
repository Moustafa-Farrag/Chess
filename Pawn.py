import pieces as pi


class Pawn(pi.pieces):

    def __init__(self, color, pos):
        pi.pieces.__init__(self, pos)
        self.color = color
        self.kind = "P"
        return

    def select_piece(self, Board):
        x = self.pos[0]
        y = self.pos[1]
        if self.color == "white":
            print("white")
            if Board.board[x-1][y].color == "non":
                self.selecMove.add((x-1, y))
                if not Board.board[x][y].firstMove:
                    if Board.board[x-2][y].color == "non":
                        self.selecMove.add((x-2, y))
            if Board.board[x-1][y-1].color == "black":
                self.selecMove.add((x-1, y-1))
            if Board.board[x-1][y+1].color == "black":
                self.selecMove.add((x-1, y+1))
        elif self.color == "black":
            if Board.board[x+1][y].color == "non":
                self.selecMove.add((x+1, y))
                if not Board.board[x][y].firstMove:
                    if Board.board[x+2][y].color == "non":
                        self.selecMove.add((x+2, y))
            if Board.board[x+1][y-1].color == "white":
                self.selecMove.add((x+1, y-1))
            if Board.board[x+1][y+1].color == "white":
                self.selecMove.add((x+1, y+1))

        return self.selecMove
