from game_data import data
import random
#from art import logo,vs
#from replit import clear
 
def get_random_account():
    return random.choice(data)
def format_data(account):
    name=account["name"]
    description=account["descrption"]
    country=account["country"]
    return f"{name}, a{descrption},from{country}"
def check_answer(guess, a_follower,b_follower):
    if a_follower  > b_followers:
        return guess == "a"
    else:
        return guess =="b"

def game():
 #   print(logo)
    score=0
    game_should_continue =True
    account_a=get_random_account()
    account_b=get_random_account()
    
    while game_should_continue:
        account_a= account_b
        account_b=get_random_account()
    print(f"compare A:{format_data(account_a)}.")
    print(vs)
    print(f"aganist b:{formate_data(account_b)}")
    guess=input("who has more followers. Type A OR B.lower")()
    a_follower_count= account_a["follower_count"]
    b_follower_count=account_b["follower_count"]

    clear()
 #   print(logo)
    if is_correct:
        score+=1
        print(f"your correct current score :{score}")
    else:
            game_should_continue=false
            print(f"sorry that's wrong . final score:{score}")
game()



























