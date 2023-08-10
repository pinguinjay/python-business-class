#去掉中文
#需要幾個小傑牌鳳黃禮盒 x1 (兩個蛋黃酥、四個鳳梨酥)
Yellow = int(input()) 
#需要幾個小傑牌傳統禮盒 x2 (三個蛋黃酥、三個鳳梨酥)
Traditional =  int(input())
#員工可以做幾個蛋黃酥
egg_output = int(input())
#員工可以做幾個鳳梨酥
pineapple_output = int(input())
#蛋黃酥需求量
egg_requirement = 2*Yellow  + 3*Traditional
#鳳梨酥需求量
pineapple_requirement = 4*Yellow + 3*Traditional
#計算所需人力
egg_worker = int()
pineapple_worker = int()
while egg_worker*egg_output < egg_requirement :
    egg_worker +=1
while pineapple_worker*pineapple_output < pineapple_requirement :
    pineapple_worker +=1
print(str(egg_requirement)+","+str(pineapple_requirement)+","+str(egg_worker)+","+str(pineapple_worker))


