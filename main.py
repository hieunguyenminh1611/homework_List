My_UniqueList = []
My_LeftOvers = []

while True :
    Var = input("Enter: ")
    if Var == 'done' :
        break
    else:
        if Var not in My_UniqueList:
            My_UniqueList.append(Var)
        else :
            My_LeftOvers.append(Var)
        print(My_UniqueList)
        print(My_LeftOvers)
