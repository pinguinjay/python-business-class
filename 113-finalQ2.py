#input
#n個物品，B為背包容量
n, B = map(int, input().split(" ")) 
#每個物品的重量
w_item = list(map(int, input().split(" "))) 
#每個物品的價值
v_item = list(map(int, input().split(" "))) 
#是否攜帶，1為攜帶，0為不攜帶。預設全為攜帶
x = [1]*n
#建立list，紀錄第i個物品的總重量，總價值
weight_total = [0]*n
value_total = [0]*n

#求總重
for i in range(n) : 
    weight_total[i] = w_item[i]*x[i]
    value_total[i] = v_item[i]*x[i]

#找出[[index, weight , value]]的排序list
def useList1ToSortedBydescending(list1, list2):
    list_index_lst1_lst2 = []
    if len(list1) == len(list2) :
        for index, (value1, value2) in enumerate(zip(list1, list2)):
             #預設第一個index為是0。value1為weight，value2為value
            list_index_lst1_lst2.append([index, value1, value2]) 
        #排序，先以value1(weight)由大到小，再以value2(value)由小到大
        #因先捨棄最重，如果同重，則捨棄價值最低
        #lambda x: (-x[1], x[2])，-x[1]為value1(weight)由大到小，x[2]為value2(value)由小到大
        sorted_list = sorted(list_index_lst1_lst2, key=lambda x: (-x[1], x[2]))
        return sorted_list

#開始演算
#先根據weight由大到小，value由小到大排序
#sorted_list = [[index, weight , value]]
sorted_list = useList1ToSortedBydescending(weight_total, value_total)# [(2, 1, 3), (0, 0, 1), (3, 0, 4), (1, -6, 5)]
#計算總重量與總價值
sum_weight = sum(weight_total) #總重
sum_value = sum(value_total) #總價值

while sum_weight>B : #在超過重量的狀況下重複算
    for i in range(n) : #從index = 0 開始刪除
        index2zero = sorted_list[i][0] #找到要刪除的index
        x[index2zero] , weight_total[index2zero], value_total[index2zero]= 0 ,0 ,0 #把weight value歸0

        sum_weight = sum(weight_total) #算重量總和
        sum_value = sum(value_total) #算價值總和

        if sum_weight <= B : #如果重量小於等於B，則跳出迴圈
            break

#output
seperator = " " #空格格開
#用join把list合併 且轉成string
x_result = seperator.join(map(str,x)) #0 0 1......1 0 0
print(x_result, sum_weight, sum_value)
