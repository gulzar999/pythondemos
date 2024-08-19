enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function:{enemies}")


player_health =10
def drink_portion():
    portion_strength = 2
    print(player_health)

drink_portion()

#global variable
#they function inside and out side of the function
x =4
print(x)     

#local variable()
#A local varaible only used inside the particular function only
def hello():

    x = 5
    print(f"the local x is {x}")
    print("hello asma")

print (f"the global x is {x}")
hello()
print(f"the global x is {x}")


Asmagulzar_shaik=56

def shaik_asma():
    x =20
    print(f"the number x is {x}")
shaik_asma()
    

print(f"Asmagulzar_shaik is {56}")
print(f"Asmagulzar_shaik is {20}")

