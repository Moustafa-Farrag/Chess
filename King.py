import pieces as pi


class King(pi.pieces):

    def __init__(self, color, pos):
        pi.pieces.__init__(self, pos)
        self.color = color
        self.kind = "K"
        return

    def select_piece(self, Board):
        x = self.pos[0]
        y = self.pos[1]
        self.selecMove.add((x+1, y))
        self.selecMove.add((x-1, y))
        self.selecMove.add((x, y+1))
        self.selecMove.add((x, y-1))
        self.selecMove.add((x-1, y-1))
        self.selecMove.add((x+1, y-1))
        self.selecMove.add((x+1, y+1))
        self.selecMove.add((x-1, y+1))
        self.check_limits()
        self.checkColorMove(Board, self.color)
        print(self.selecMove)
        return self.selecMove
