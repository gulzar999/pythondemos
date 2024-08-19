step=1
# word_list=["aardvark","baboon","camel"]
# #TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# import random
# chosen_word=random.choice(word_list)

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
# guess=input("guess a letter:").lower()

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
# for letter in chosen_word:
#     if letter==guess:
#         print("right")
#     else:
#         print("wrong")
# #STEP2
# import random
# word_list=["aardvark","baboon","camel"]
# chosen_word=random.choice(word_list)
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
# display=[]
# word_length=len(chosen_word)
# for _ in range(word_length):
#     display += "-"
# guess=input("guess a letter:").lower()
# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
# for position in range  (word_length):
#     letter=chosen_word[position]
#     #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#     if letter==guess:
#         display[position] =letter
#         #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display) 
# #Step 4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']
# end_of_game= False
# word_list=["ardvark", "baboon", "camel"]
# chosen_word=random.choice(word_list)
# word_length=len(chosen_word)
# #TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
# #Set 'lives' to equal 6.
# lives=6
# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')
# disply=[]
# for _ in range(word_length):
#     disply += "-"
# while not end_of_game:
#     guess = input("guess a letter: ").lower()

#     #Check guessed letter
#     for position in  range (word_length):
#         letter=chosen_word[position]
#         # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter==guess:
#             disply[position]=letter
       
#             #TODO-2: - If guess is not a letter in the chosen_word,
#     #Then reduce 'lives' by 1. 
#     #If lives goes down to 0 then the game should stop and it should print "You lose."
#     if guess not in chosen_word:
#         lives-=1
#         if lives==0:
#           end_of_game=True
#           print("you lose.")

#     #Join all the elements in the list and turn it into a String.
#     print (f"{''.join(disply)}")
#     #Check if user has got all letters.
#     if "_" not in disply:
#         end_of_game=True
#         print("you win")
#     #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
#     print(stages[lives])

# import random
# #use the word list and insert the word list in "hangman_words.py"
# from hangman_words import word_list
# chosen_word=random.choice(word_list)
# word_length=len(chosen_word)
# end_of_game=False
# lives=6

# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
# from hangman_art import logo
# print(logo)

# #testing code
# #print(f'pssst, the solution is {chosen_word}.')

# #creat blank
# display=[]
# for _  in range (word_length):
#     display+= "_"
# while not end_of_game:
#     guess=input("guess a letter:").lower()
   

#    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.

#     if guess in display:
#        print(f" you have already gussed {guess}") 
#     for position in range(word_length):
#        letter=chosen_word[position]
#        if letter ==guess:
#            display[position]=letter 
#         #Check if user is wrong.
#     if guess not in chosen_word:  
#             #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f"if you gussed{guess},that is not in the word.you lose a life ")

#         lives=-1
#         if lives== 0:
#             end_of_game= True
#             print("you lose")
#    #Join all the elements in the list and turn it into a String.        
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "-"  not in display:
#        end_of_game=True
#        print("you win")
#      #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     from hangman_art import stages
#     print(stages[lives])


# def formate_name(f_name,l_name):
#      formated_f_name= f_name.title()
#      formated_l_name= l_name.title()
#      return f"{formated_f_name} {formated_l_name}"
# print(formate_name(input("what is your first name"),
# input("what is your last name")))

def greet():
    print("hello asma")
    print("what are you doing sameer")
    print("how is your day asma")
greet()

def greet_with_name(name,location):
    print(f"hello {name}" )
    print(f"how do you do {location}")
greet_with_name("name","location")
greet_with_name(name="yesdani",location="bujkhalifa dubai returns")

#class and objects
class human():
    def __init__ (self,name,age):
        self.name=name
        self.age=age
h1=human("asma",4)
h2=human("shaik",4)
print(h1.name)
print(h1.name,h2.age)

#caluclator:
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return( n1 / n2)

operations={
"+":add,
"-":subtract,
"*":multiply,
"/":divide
}

num1=int(input("what is the first number?:"))
for symbol in operations:
    print(symbol)
operation_symbol=input("pick up an opertaion from the above line:")

num2=int(input("what is the second number?:"))
caluclate_function=operations[operation_symbol]
answer=caluclate_function(num1,num2)
first_answer= caluclate_function(num1,num2)

operation_symbol=input("pick uo another operation:")
num3=int(input("what is another number?:"))
caluclate_function=operations[operation_symbol]
second_answer=caluclate_function(caluclate_function(num1,num2),num3)        
print(f"{first_answer} {operation_symbol} {num3}={second_answer}")


       













                   
                   



 
 


