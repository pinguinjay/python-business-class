# 輸入input
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

#判斷大小，如果x1>x2則交換
if x1 > x2:
    x1, x2 = x2, x1
    
#判斷大小，如果y1>y2則交換
if y1 > y2:
    y1, y2 = y2, y1
#建立四個點，逆時針順序
pontA = (x1, y1) #左下
pontB = (x2, y1) #右下
pontC = (x2, y2) #右上
pontD = (x1, y2) #左上
#計算長度
def calculate_length(point1, point2):
    #計算兩點距離
    length_square = (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2
    length = length_square**0.5
    return length
#計算面積
line1 = calculate_length(pontA, pontB)
line2 = calculate_length(pontB, pontC)
line3 = calculate_length(pontC, pontD)
line4 = calculate_length(pontD, pontA)
area = line1 * line2
#判斷是否為正方形
if line1 == line2 == line3 == line4 :
    print(str(1), str(int(area)))
else :
    print(str(0), str(int(area)))