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
