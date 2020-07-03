board = []
selecMove = set()

def main():

    rows, cols = (8,8)
    EasyForIf = { 1 : "p" , 2 : "r" , 3 : "h" , 4 : "b" , 5 : "K" , 6 : "q" , 0 : "E" }  

    arr1 = [0]*cols 
    solider = [1]*8;
    for i in range(8):
        board.append(list(arr1))

    #print (arr) 
    board[1] = list(solider)
    board[6] = list(solider)

    king = [0]*8 ; 
    for i in range(3):
        king[i] = king[7-i] = i+2


    board[0] = list(king)
    board[7] = list(king)
    board[7][3] = 6; 
    board[7][4] = 5; 
    board[0][3] = 6;
    board[0][4] = 5;
    for i in range(8):
           print(str(board[i]).replace("," , ""))

    order = input("enter order: ");
    order = order.split(':');
    if order[0] == "sel":
        pass    #select(order[1])
    elif order[0] == "move":
        pass #move(order[1] , order[2])
    elif order[0] == "help":
        print(EasyForIf)


def sKinght(x , y):
    newX = x - 2 
    newY = y + 1 
    selecMove.add((newX , newY))
    newY = y - 1 
    selecMove.add((newX , newY))
    #first one
    newX = x + 2 
    newY = y + 1 
    selecMove.add((newX , newY))
    newY = y - 1 
    selecMove.add((newX , newY))
    #first two 
    newY = y + 2 
    newX = x + 1 
    selecMove.add((newX , newY))
    newX = x - 1 
    selecMove.add((newX , newY))
    #fitst three
    newY = y - 2 
    newX = x + 1 
    selecMove.add((newX , newY))
    newX = x - 1 
    selecMove.add((newX , newY))
    checkBoardBords(selecMove)
    print (selecMove) 
    pass 

def checkBoardBords(selecMove):
    deleted = list()

    for i in selecMove:
        if i[0] < 0 or i[0] > 7:
            deleted.append(i)
            continue
        elif i[1] < 0 or i[1] > 7:
            deleted.append(i)
            continue

    for i in deleted:
        selecMove.discard(i)

    return 

def sRook(x ,y):
    for i in range(8):
        if x+i > 7:
            break;
       # if board[x+i][y] != ' ':
       #     break;
        selecMove.add((x+i , y))
    for i in range(8):
        if x-i < 0:
            break;
       # if board[x-i][y] != ' ':
            #chek if color
       #     break;
        selecMove.add((x-i , y))
    for i in range(8):
        if y-i < 0:
            break;
       # if board[x][y-i] != ' ':
            #chek if color
       #     break;
        selecMove.add((x , y-i))
    for i in range(8):
        if y+i > 7:
            break;
       # if board[x][y+i] != ' ':
            #chek if color
       #     break;
        selecMove.add((x , y+i))
    print (selecMove) 
    return 

def sBishop(x ,y):
    for i in range(8):
        if y+i > 7 or x+i > 7:
            break;
        #if board[x+i][y+i] != ' ':
        #    break;
        selecMove.add((x+i , y+i))

    for i in range(8):
        if y-i < 0 or x-i < 0:
            break;
        #if board[x-i][y-i] != ' ':
            #chek if color
        #    break;
        selecMove.add((x-i , y-i))

    for i in range(8):
        if y+i > 7 or x-i < 0 :
            break;
        #if board[x-i][y+i] != ' ':
            #chek if color
        #    break;
        selecMove.add((x-i , y+i))

    for i in range(8):
        if y-i < 0 or x+i > 7  :
            break;
        #if board[x+i][y-i] != ' ':
        #    break;
        selecMove.add((x+i , y-i))
        #print('sssssssss')
    
    for i in selecMove:
        board[i[0]][i[1]] = 9
    print (selecMove) 
    return 

def sQueen(x,y):
    sRook(x,y) 
    sBishop(x,y)
    return

main()
sQueen(1 ,2)
#sKinght(1,2)
for i in range(8):
    print(str(board[i]).replace("," , ""))
