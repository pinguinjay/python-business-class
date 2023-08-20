# 讀入資料
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# 判斷是否是正方形
isSquare = 0
if abs(x1-x2) == abs(y1-y2) and abs(x1-x2) != 0:
    isSquare = 1

# 印出結果
print(isSquare, abs(x1-x2)*abs(y1-y2))
