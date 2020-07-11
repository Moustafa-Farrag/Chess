class pieces:

    def __init__(self, pos):
        self.color = "non"
        self.pos = pos
        self.kind = "-"
        self.firstMove = False
        self.selecMove = set()
        return

    def __str__(self):
        return self.kind

    def move_piece(self, pos):
        self.pos = pos
        self.firstMove = True
        return

    def select_piece(self):
        return self.selecMove

    def checkColorMove(self, Board, color):
        deleted = set()
        for i in self.selecMove:
            print(Board.board[i[0]][i[1]].color, color)
            if Board.board[i[0]][i[1]].color == color:
                deleted.add(i)
        for i in deleted:
            self.selecMove.discard(i)

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
