#使用的函式庫
import math
#n多少天  money一開始多少錢
n, money = map(int, input().split(","))
#創建未來幾天股價的list
stock = list(map(int, input().split(",")))
#L股票買入線  U股票賣出線
L, U = map(int, input().split(","))
#假設持有股票
stock_in_hand = 0
#計算買賣
for day in range(n-1) :
    if stock[day]<=L: #股價不高於L，入股
        pay = math.floor(money/2) #算花多少錢買股
        stock_buy = math.floor(pay/stock[day])#算買幾股
        cost = stock[day]*stock_buy #總共花多少錢買股
        stock_in_hand += stock_buy #計算股票變化
        money = money - cost #算最後剩多少錢
    elif stock[day] >=U : #股價不低於U，賣股
        y = math.floor(stock_in_hand/2)#算要賣多少股
        gain = y*stock[day] #算可以賣多少錢
        stock_in_hand -= y #計算股票變化
        money += gain #算最後剩多少錢
    else : #L<當日股價<U，什麼都不做
        #沒變化
        stock_in_hand = stock_in_hand
        money = money

#最後一天
all_stock = stock_in_hand*stock[n-1] #算賣多少
money += all_stock #算最後剩多少錢
print(money)

