MENU={
    "espreso":{
        "ingredients":{
            "water":50,
            "coffee":18,

        },
        "cost":100,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,


        },
        "cost":200,

    },
    "cappachino":{
        "ingredients":{
            "water":200,
            "milk":100,
            "coffee":24,
        
         },
    "cost":300,
    }
}
profit=0
resources={
    "water":300,
    "milk":200,
    "coffee":100,
}

def  is_resources_sufficient(order_ingredients):
    for items in order_ingredients:
        if order_ingredients[items] > resources[items]:
            print(f"sorry! there are no enough [items]")
            return False
    return True

def process_coins():
    print("please insert coins")
    total=int(input("how many 10 rs note" ))*10
    total+=int(input("how many 20 rs note"))*20
    total+=int(input("how many 50 rs notes"))*50
    total+=int(input("how many 100 rs notes"))*100
    total+=int(input("how many 500 rs notes"))*500
    total+=int(input("how many 2000 rs notes"))*2000
    return total

def is_transcation_successful(money_recieved,drink_cost):
    if money_recieved >= drink_cost:
        change= round(money_recieved - drink_cost,2)
        print(f"here is {change}in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("money is not enough .Money refunded")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]- order_ingredients[item]
    print(f" here is your drink {drink_name} \N{Hot Beverage}.enjoy")

is_on=True
while is_on:
    choice=input("what would you like(espreso/latte/cappachino):")
    if choice=="off":
        is_on=False
    elif choice=="report":
        print(f"water:{resources['water']} ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"money: rs{profit}")
    else:
        drink=MENU[choice]
        if is_resources_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transcation_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])




    