a=int(input())
payback=1000 - a
pay500= payback//500
payback1=payback-500*pay500
pay100= payback1//100
payback2=payback1-100*pay100
pay50=payback2//50
payback3=payback2-50*pay50
pay10=payback3//10
payback4=payback3-10*pay10
pay5= payback4//5
payback5=payback4-5*pay5
pay1= payback5//1
print(pay500)
print(pay100)
print(pay50)
print(pay10)
print(pay5)
print(pay1)
print(pay500, pay100, pay50, pay10, pay1)