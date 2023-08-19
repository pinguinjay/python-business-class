m ,n, k =map(int,input().split(";"))
B =[]
for i in range(m) :
    score = list(map(int, input().split(",")))
    B.append(score)
def cal_rank(x, B, k) : #0<=x<=m-1
    c = 0#找出B[x]中不等於0的數量
    for score in B[x] :
        if score != 0 :
            c+=1

    rank =sum(B[x]) - k*c
    return rank
rank_list = []
rank_list_delete =[]
rank_list_add = []

for x in range(m) :
    rank = cal_rank(x, B, k)
    rank_list.append(rank)
    rank_list_delete.append(rank)
rank_list_delete_sorted = sorted(rank_list_delete)
first = rank_list_delete_sorted[-1]
second = rank_list_delete_sorted[-2]
third = rank_list_delete_sorted[-3]
if first != second :#前2不同
    first_indi = rank_list.index(first)
    rank_list_add.append(first_indi+1)
    if second != third :
        sec_indi = rank_list.index(second )
        rank_list_add.append(sec_indi+1)
        third_indi = rank_list.index(third )
        rank_list_add.append(third_indi+1)
        
    else :
        sec_indi = rank_list.index(second )
        rank_list_add.append(sec_indi+1)
        rank_list.pop(sec_indi)
        third_indi =rank_list.index(third)
        rank_list_add.append(third_indi+2)
        
else :
    first_indi = rank_list.index(first)
    rank_list_add.append(first_indi+1)
    rank_list.pop(first_indi)
    sec_indi = rank_list.index(second )
    rank_list_add.append(sec_indi+2)
    if second != third :
        sec_indi = rank_list.index(second )
        rank_list_add.append(sec_indi+2)
        third_indi = rank_list.index(third )
        rank_list_add.append(third_indi+2)
        
    else :
        sec_indi = rank_list.index(second )
        rank_list_add.append(sec_indi+2)
        rank_list.pop(sec_indi)
        third_indi =rank_list.index(third )
        rank_list_add.append(third_indi+3)
        
formatted_indices = ' '.join(map(str, rank_list_add))
print( formatted_indices)