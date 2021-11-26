print("======|Welcome to Bank|=======")
print("     Bank : 100,500,1000      ")
money = int(input("Enter your money : "))
user= 0
user = money
while user < 20000 :
    if user/1000 != 0:
        num=int(user/1000)
        print(f"1000 : {num}")
        user%=1000
    
    if user/500 != 0 :
        num=int(user/500)
        print(f"500 : {num}")
        user %=500
        
    if user/100 != 0 :
        num=int(user/100)
        print(f"100 : {num}")
        user%=100
    break
else : print("Error")
print("==============================")
print(f"Withdraws : {money}")
print("==========|Thankyou|==========")
