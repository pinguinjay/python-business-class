
#如果要依序回傳綜合評價前三高的賣方，我們會回傳 3、1、4。請注意因為賣方 1 和賣方 4 的綜合評價分數一樣，我們會把編號小的賣方 1 放在前面
#舉例
#list1 = [0,-6,1,0]
#list2 = [1,5,3,4]

list1 = [0,-6,1,0]
list2 = [1,5,3,4]
list_index_lst1_lst2 = []
#dict1 = dict()
#dict2 = dict() #{3: 1, 1: 0, 4: 0, 5: -6}
def useList1ToSortedBydescending(list1, list2):
    if len(list1) == len(list2) :
        for index, (value1, value2) in enumerate(zip(list1, list2)):
            list_index_lst1_lst2.append([index+1, value1, value2]) #+1是預設第一個index為1不是0
        #從value降冪排序，再從value降冪排序
        sorted_list = sorted(list_index_lst1_lst2, key=lambda x: (-x[1], x[2]))
        return sorted_list
sorted_list = useList1ToSortedBydescending(list1, list2)# [(2, 1, 3), (0, 0, 1), (3, 0, 4), (1, -6, 5)]
