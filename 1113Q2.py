
#輸入並建立一個list
bread_list = [ ]
n = int(input())
#連續輸入麵包值
for i in range(n)  :
    x = int(input())
    bread_list.append(x) 

day = 0#第幾天
breadnumber = 0#麵包剩多少

for i in range(len(bread_list)) :
    breadnumber += bread_list[i] #計算麵包有多少
    day+=1
    if breadnumber<0: #賣不夠時
        print(day)
        break
    elif i==(len(bread_list)-1) and breadnumber>=0: #當道最後一天且麵包有剩
        print(breadnumber)
        break
