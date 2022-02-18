with open ('ask7.txt' , "r") as f:
    D = {}
    for line in f:
        D = (line)
        print(D)

    choise = input("give your choise : x , y , name ") 

    for key in D :

        if choise == "x":
            print( max ( D[x] ) )
            print( min ( D[x] ) )
        elif choise == "y":
            print( max ( D[y] ) )
            print( min ( D[y] ) )
        elif choise == "name":
            print( max ( D[name] ) )
            print( min ( D[name] ) )


    


































