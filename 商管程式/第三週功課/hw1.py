bank1=int(input())
bank2=int(input())
transfer=int(input())
if transfer>bank1 :
    bank2+=bank1
    bank1=0
else :
    bank2+=transfer
    bank1-=transfer
print(bank1,bank2)