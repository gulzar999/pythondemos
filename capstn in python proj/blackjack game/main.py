import random
#from  replit import clear
from art import logo

def deal_card():
   """ returns a ramdom card from deck"""
   cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
   card=random.choice(cards)
   return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score >21 and computer_score >21:
        return "you went over. You lose"
    
    if user_score==computer_score:
        return "draw"
    elif computer_score==0:
        return "you lose opponent has blackjack"
    elif user_score==0:
        return "you win with a blackjack"
    elif user_score >21:
        return " you lose"
    elif computer_score>21:
        return "oppnent went over. You win"
    elif user_score > computer_score:
        return " you win"
    else:
        return "you lose"

def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_gameover=False
    
    for _ in range (2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_gameover:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print (f"your cards= {user_cards},your score={user_score}")
        print (f"computer first score:{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_gameover=True
        else:
            user_should_deal=input("type 'y' to get another card, type 'n' to pass : ")
            if user_should_deal=="y":
                user_cards.append(deal_card())
            else:
                is_gameover=True
    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score=calculate_score(computer_cards)
    print(f" your final hand is {user_cards}, final score is {user_score}")
    print(f" computer final hand{ computer_cards},final score is {computer_score}")
    print( compare(user_score,computer_score) )

while input("do you want to play another game type 'y'or 'n':")=='y':
    play_game()

#local scope
def drink_portion():
    portion_strength=2
    print(portion_strength)
drink_portion()
print(portion_strength)


   
