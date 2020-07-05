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
        self.selecMov = set()
        self.selecMove = set()
        return

    def set_currentPlayer(self, currentPlayer):
        self.currentPlayer = currentPlayer
        return

    def move(self, pos1, pos2):
        self.board[0].move(pos1)
        return

    def select(self, pos1):
        if self.board[pos1[0]][pos1[1]].kind == "p":
            pass
        elif self.board[pos1[0]][pos1[1]].kind == "K":
            pass
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

    def sKinght(self ,x, y):
        newX = x - 2
        newY = y + 1
        self.selecMove.add((newX , newY))
        newY = y - 1
        self.selecMove.add((newX , newY))
        #first one
        newX = x + 2
        newY = y + 1
        self.selecMove.add((newX , newY))
        newY = y - 1
        self.selecMove.add((newX , newY))
        #first two
        newY = y + 2
        newX = x + 1
        self.selecMove.add((newX , newY))
        newX = x - 1
        self.selecMove.add((newX , newY))
        #fitst three
        newY = y - 2
        newX = x + 1
        self.selecMove.add((newX , newY))
        newX = x - 1
        self.selecMove.add((newX , newY))
        # checkBoardBords()
        self.check_limit()
        print (self.selecMove)
        pass
        return

    def sRook(self ,x ,y):
        for i in range(8):
            if x+i > 7:
                break;
           # if board[x+i][y] != ' ':
           #     break;
            self.selecMove.add((x+i , y))
        for i in range(8):
            if x-i < 0:
                break;
           # if board[x-i][y] != ' ':
                #chek if color
           #     break;
            self.selecMove.add((x-i , y))
        for i in range(8):
            if y-i < 0:
                break;
           # if board[x][y-i] != ' ':
                #chek if color
           #     break;
            self.selecMove.add((x , y-i))
        for i in range(8):
            if y+i > 7:
                break;
           # if board[x][y+i] != ' ':
                #chek if color
           #     break;
            self.selecMove.add((x , y+i))
        print (self.selecMove)
        return

    def sBishop(self ,x ,y):
        for i in range(8):
            if y+i > 7 or x+i > 7:
                break;
            #if board[x+i][y+i] != ' ':
            #    break;
            self.selecMove.add((x+i , y+i))

        for i in range(8):
            if y-i < 0 or x-i < 0:
                break;
            #if board[x-i][y-i] != ' ':
                #chek if color
            #    break;
            self.selecMove.add((x-i , y-i))

        for i in range(8):
            if y+i > 7 or x-i < 0 :
                break;
            #if board[x-i][y+i] != ' ':
                #chek if color
            #    break;
            self.selecMove.add((x-i , y+i))

        for i in range(8):
            if y-i < 0 or x+i > 7  :
                break;
            #if board[x+i][y-i] != ' ':
            #    break;
            self.selecMove.add((x+i , y-i))

        print (self.selecMove)
        return

    def sQueen(self, x, y):
        self.sRook(x,y)
        self.sBishop(x,y)
        return

    def sKing(self ,x,y):
        self.selecMove.add((x+1,y))
        self.selecMove.add((x-1,y))
        self.selecMove.add((x,y+1))
        self.selecMove.add((x,y-1))
        self.selecMove.add((x-1,y-1))
        self.selecMove.add((x+1,y-1))
        self.selecMove.add((x+1,y+1))
        self.selecMove.add((x-1,y+1))
        # checkBoardBords()
        print (self.selecMove)
        return


def create_board():

    player1Name = input("enter player1 name: ")
    player2Name = input("enter player2 name: ")

    player1 = player(player1Name, "white")
    player2 = player(player2Name, "balck")

    r, c = (8, 8)
    EasyForIf = {1: "p", 2: "r", 3: "h", 4: "b", 5: "K", 6: "q", 0: "E"}
    b = list()
    for i in range(r):
        rr = list()
        for j in range(c):
            if i < 2:
                one = pieces("white", (i, j), "p")
                player1.add_piece(one)
            elif i > 5:
                one = pieces("black", (i, j), "p")
                player2.add_piece(one)
            else:
                one = pieces("non", (i, j), "non")

            rr.append(one)

        b.append(rr)

    for i in range(3):
        b[0][i].kind = EasyForIf[i+2]
        b[0][7-i].kind = EasyForIf[i+2]
        b[7][i].kind = EasyForIf[i+2]
        b[7][7-i].kind = EasyForIf[i+2]

    for i in range(8):
        for j in range(8):
            print(b[i][j], end=' ')
        print(" ")
    
    bbb = Board(b ,player1) 
    bbb.sBishop(1 ,2)
    return

create_board()



#main()
#sKing(1,2)
#sQueen(1 ,2)
#sKinght(1,2)
#for i in selecMove:
#    board[i[0]][i[1]] = 9
#for i in range(8):
#    print(str(board[i]).replace("," , ""))
