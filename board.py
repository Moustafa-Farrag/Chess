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
    checkAllSteps(selecMove)
    print (selecMove) 
    pass 

def checkAllSteps(selecMove):
    counter = 0 
    for i in range(len(selecMove)):
        if selecMove[counter][0] < 0 or selecMove[counter][0] > 7:
            selecMove.remove(counter)
            continue
        elif selecMove[counter][1] < 0 or selecMove[counter][1] > 7:
            selecMove.remove(counter)
            continue
        counter += 1 
    return 

sKinght(1,2)
main()
