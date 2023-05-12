a=int(input())
statment="" #最後表達
payback=1000 - a
pay500= payback//500
payback1=payback-500*pay500
if pay500!=0:
    statment="500,"+" "+str(pay500)+"; "
else: 
    statment=statment

pay100= payback1//100
payback2=payback1-100*pay100
if pay100!=0:
    statment=statment+"100,"+" "+str(pay100)+"; "
else: 
    statment=statment
    
pay50=payback2//50
payback3=payback2-50*pay50
if pay50!=0:
    statment=statment+"50,"+" "+str(pay50)+"; "
else: 
    statment=statment
    
pay10=payback3//10
payback4=payback3-10*pay10
if pay10!=0:
    statment=statment+"10,"+" "+str(pay10)+"; "
else: 
    statment=statment
    
pay5= payback4//5
payback5=payback4-5*pay5
if pay5!=0:
    statment=statment+"5,"+" "+str(pay5)+"; "
else: 
    statment=statment
pay1= payback5//1
if pay1!=0:
    statment=statment+"1,"+" "+str(pay1)+"; "
else: 
    statment=statment

print(statment)