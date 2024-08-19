from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(guess,answer,turns):
    if guess > answer:
        print("Too high")
        return turns-1
    elif guess < answer:
        print("Too low")    
        return turns-1
    else:
        print(f"you got it answer was {answer}")
#make function to make it easy or hard
def set_difficulty():
    level=input("choose difficulity. Type 'easy' or 'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
#CHOOSING A RANDOM NUMBER BETWEEN 1 AND 100
def game(): 
    print("welcom to the random number guessing game")
    print("iam thinking of a number between 1 and 100")
    answer=randint( 1, 100)
    print ("pssst the correct answer is {answer}")
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        guess=int(input("make a guess"))
        turns=check_answer(guess,answer,turns)
        if turns == 0:
            print("you run out of guesses. You lose the game")
            return 
        elif guess!=answer:
            print("guess again")

game()

