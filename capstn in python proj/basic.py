##print("asmaam")
print("welcome to roller coster riding")
height = int(input("what is your height in cm?" ))

if height >= 120:
    print("you can ride the roller coster")
    age = int(input("what is your age?"))
    if age < 12:
        print("child ticket are rs 50")
    elif age <= 18:
        print("please pay rs100")
    else:
        bill = 13
        print("please pay rs77")
    wants_photo = input("do you want a photo? Y or N?")
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill is rs{bill}")
        
else:
##  ("you can't ride the rollercoster")

    
print("welcome to tresure island")
print("your mission is to find the treasure.")
choice1= input('you\'re at a crossroad, where do you want to go ? Type "left" or "right".').lower()
if choice1 == "left" or choice1 =="right":
    
              
else:
    print("you fell into a hole. Game over")