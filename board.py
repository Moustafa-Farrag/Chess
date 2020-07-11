# self.color + " " + str(self.pos) + " " + self.kind
import pieces as pi


class Board:

    def __init__(self, board, currentPlayer, player1king, player2king):
        self.currentPlayer = currentPlayer
        self.board = board
        self.selPiece = pi.pieces((0, 0))
        self.player1King = player1king
        self.player2King = player2king
        self.canMove = set()
        return

    def set_currentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
        return

    def moveTo(self, pos, player):
        if self.selPiece.color == "non":
            return False
        print(self.canMove, pos)
        if pos in self.canMove:
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
            self.canMove.clear()
            self.select(pos)
            if self.player1King.pos in self.canMove:
                print("KKKKKKKKKKKKKKKKKKKKKKKKKK")
            elif self.player2King.pos in self.canMove:
                print("KKKKKKKKKKKKKKKKKKKKKKKKKK")
            self.resetSecBoard()
            self.canMove.clear()
            return True
        self.resetSecBoard()
        self.canMove.clear()
        return False

    def changeSecBoard(self):
        for i in self.canMove:
            if self.board[i[0]][i[1]].color == "non":
                self.board[i[0]][i[1]].kind = "*"

    def resetSecBoard(self):
        for i in self.canMove:
            if self.board[i[0]][i[1]].color == "non":
                self.board[i[0]][i[1]].kind = "-"

    def select(self, pos1):
        if self.currentPlayer.color != self.board[pos1[0]][pos1[1]].color:
            # print(self.currentPlayer.color,
            # self.board[pos1[0]][pos1[1]].color,
            # self.board[pos1[0]][pos1[1]].kind)
            return
        x, y = pos1
        self.resetSecBoard()
        self.canMove = set(self.board[pos1[0]][pos1[1]].select_piece(self))
        self.changeSecBoard()
        self.selPiece = self.board[pos1[0]][pos1[1]]
        return
