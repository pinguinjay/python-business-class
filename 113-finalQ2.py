n, B = map(int, input().split(" "))
w_item = list(map(int, input().split(" ")))
v_item = list(map(int, input().split(" ")))
x = [1]*n#是否攜帶
weight_total = [0]*n
value_total = [0]*n
for i in range(n) : #求總重
    weight_total[i] = w_item[i]*x[i]
    value_total[i] = v_item[i]*x[i]
#找出[[index, weight , value]]的排序list

def useList1ToSortedBydescending(list1, list2):
    list_index_lst1_lst2 = []
    if len(list1) == len(list2) :
        for index, (value1, value2) in enumerate(zip(list1, list2)):
            list_index_lst1_lst2.append([index, value1, value2]) #是預設第一個index為是0
        #從value降冪排序，再從value降冪排序
        sorted_list = sorted(list_index_lst1_lst2, key=lambda x: (-x[1], x[2],-x[0]))
        return sorted_list
sorted_list = useList1ToSortedBydescending(weight_total, value_total)# [(2, 1, 3), (0, 0, 1), (3, 0, 4), (1, -6, 5)]
#上面ok
sum_weight = sum(weight_total) #總重
sum_value = sum(value_total) #總價值
while sum_weight>B : #在超過重量的狀況下重複算
    for i in range(n) : #從index = 0 開始刪除
        index2zero = sorted_list[i][0] #找到要刪除的index
        x[index2zero] , weight_total[index2zero], value_total[index2zero]= 0 ,0 ,0 #把weight value歸0

        sum_weight = sum(weight_total) #算重量總和
        sum_value = sum(value_total) #算價值總和

        if sum_weight <= B :
            break
seperator = " " #空格格開
x_result = seperator.join(map(str,x))
print(x_result, sum_weight, sum_value)
