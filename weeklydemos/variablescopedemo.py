enemies=1
def increase_enemies():
    enemies=2
    print(f"enemies inside function{enemies}")

increase_enemies()
print(f"enemies outside function:{enemies}")

def drink_portin():
    portin_strength=2
    print("portin_strength")
drink_portin()
print(drink_portin)
#global scope
player_health=10
def game():
    def drink_portin():
        player_health=2
        print(player_health)
    drink_portin()
print("player_health")

#there is no block scope
game_level=3
def create_enemy():
    enemies=["zombie","wrost","alien"]
    if game_level < 5:
        new_enemy=enemies[0]
    print(new_enemy)

enemies=1
def increase_enemies():
    print(f"enemies inside function:{enemies}")
    return enemies+1
enemies=increase_enemies
print(f"enemies outside function:{enemies}")

#gobal constant
PI=3.14159
URL="https://www.google.com"
TWITTER_HANDLE="@yu_angela"



def check_even_odd(number):
    if number % 2==0:
        print("the number as 'even',number")
    else:
        print("the number as 'odd',number")
check_even_odd(3)

names=input("enter a list of names:").split()
for name in names:
    name=name.capitalize( )
print("The captalize names are:",names)