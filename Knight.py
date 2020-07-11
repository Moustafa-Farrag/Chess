import pieces as pi


class Knight(pi.pieces):

    def __init__(self, color, pos):
        pi.pieces.__init__(self, pos)
        self.color = color
        self.kind = "H"
        return

    def select_piece(self, Board):
        x = self.pos[0]
        y = self.pos[1]
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
        self.checkColorMove(Board, self.color)
        print(self.selecMove)
        return self.selecMove
