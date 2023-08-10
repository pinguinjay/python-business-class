def find_lowest(inlist,k) :
    lowest_point = list()
    if len(inlist) < (k+2+1) :
        return None
    else :
        for test_point in range(k,len(inlist)-k) :#選定一點
            forward_check = True
            backward_check = True
            for for_move in range(0,k) :#往前確認
                if inlist[test_point - 1 -for_move] <= inlist[test_point  -for_move] :
                    forward_check = False
            for back_move in range(0,k) :#往前確認
                if  inlist[test_point + 1 + back_move] <= inlist[test_point  + back_move] :
                    backward_check = False

            if backward_check == True and forward_check == True :
                lowest_point.append(test_point)
        if len(lowest_point) > 0 :
            return lowest_point
        else:
            return None

inlist = input().split(",")
inlist = [float(item) for item in inlist]

k = int(input())
if k<1 :
    k=2
lowest_point = find_lowest(inlist,k)
if lowest_point is None :
    print("NA")
else :
    for item in lowest_point:
        print(item)
