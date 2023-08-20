# 讀入資料
n, budget = input().split()
n = int(n)
budget = int(budget)
weight = input().split()
value = input().split()

# 初始化選擇
x = [1] * n

# 建立背包（為了之後排序方便，負號表示由大到小排）
backpack = [[-int(weight[i]), int(value[i]), -i, 1] for i in range(n)]

# 按照題目要求排序並依序刪除背包中的物品
while sum([-backpack[i][0] for i in range(n)]) > budget:
    backpack.sort()
    backpack[0][0] = 0
    backpack[0][1] = 0
    x[-backpack[0][2]] = 0

# 印出結果
for xi in x:
    print(xi, end=' ')
print(sum([-backpack[i][0] for i in range(n)]), sum([backpack[i][1] for i in range(n)]))
