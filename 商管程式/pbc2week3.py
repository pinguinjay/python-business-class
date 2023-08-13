#輸入牆壁n面和m次油漆。以空格隔開
n,m = map(int,input().split())
#create n面牆，預設顏色為1的list
#第一面牆壁的編號為0，第二面牆壁的編號為1，以此類推。最後一面牆壁的編號為n-1
walls = [1]*n
#接下來的m行每行依順序輸入漆的牆壁的起點號碼、漆的牆壁的終點號碼，以及顏色代碼
paints = []
for i in range(m):
    #輸入漆的牆壁的起點號碼、漆的牆壁的終點號碼，以及顏色代碼。以空格隔開
    start,end,color = map(int,input().split())
    paints.append([start,end,color])
    #將起點到終點的牆壁都塗上顏色
results = []
#開始塗顏色，從第一次塗到第m次。
for i in range(m):
    for j in range(paints[i][0]-1,paints[i][1]):
        walls[j] = paints[i][2]
#將塗完顏色的牆壁數量與顏色代碼加入results
for i in range(m):
    result_raw = [str(walls.count(paints[i][2]))," ",str(paints[i][2])]
    results.append(''.join(map(str,result_raw)))
result_join = ";".join(map(str,results))
print(result_join)
