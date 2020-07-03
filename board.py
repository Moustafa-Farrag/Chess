def main():
    rows, cols = (8,8)
    EasyForIf = { 1 : "p" , 2 : "r" , 3 : "h" , 4 : "b" , 5 : "K" , 6 : "q" , 0 : "E" }  

    arr1 = [0]*cols 
    solider = [1]*8;
    arr = []
    for i in range(8):
        arr.append(list(arr1))

    print (arr) 
    arr[1] = list(solider)
    arr[6] = list(solider)

    king = [0]*8 ; 
    for i in range(3):
        king[i] = king[7-i] = i+2


    arr[0] = list(king)
    arr[7] = list(king)
    arr[7][3] = 6; 
    arr[7][4] = 5; 
    arr[0][3] = 6;
    arr[0][4] = 5;
    for i in range(8):
            print(str(arr[i]).replace("," , ""))

    order = input("enter order: ");
    order = order.split(':');
    if order[0] == "sel":
        pass    #select(order[1])
    elif order[0] == "move":
        pass #move(order[1] , order[2])
    elif order[0] == "help":
        print(EasyForIf)

selecMove = set()

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
        if board[x+i][y] != ' ':
            #chek if color
            break;
        selecMov.append((x+i , y))
    for i in range(8):
        if x-i < 0:
            break;
        if board[x-i][y] != ' ':
            #chek if color
            break;
        selecmov.append((x-i , y))
    for i in range(8):
        if y-i < 0:
            break;
        if board[x][y-i] != ' ':
            #chek if color
            break;
        selecmov.append((x , y-i))
    for i in range(8):
        if y+i > 7:
            break;
        if board[x][y+i] != ' ':
            #chek if color
            break;
        selecmov.append((x , y+i))
    return 

def sBishop():

    return 
sKinght(1,2)
main()
