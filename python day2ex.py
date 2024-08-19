#pizza_size=input("what size pizza do u want ? small,large,medium")
#pizza_shape=input("what shape do u want? heart ,square,rectangle")
#pizza_toppings=input("what toppings do u want ?sweetcorn,mushroom,olives")

#bill=0
#if pizza_size=="small":
 #   bill+=150
#elif pizza_size=="medium":
 #   bill+=200
#else:
 #    pizza_size="large"
    # bill+=250
#print(f"bill is {bill}")

#if pizza_toppings=="sweetcorn":
 #   bill+=20
#elif pizza_toppings=="mushroom":
 #   bill+=50
#elif pizza_toppings=="olives":
 #   bill+=100
#print(f"pizza size is {pizza_size} shape is {pizza_shape} topping is {pizza_toppings} and bill amount is {bill}")        
#

""" print("welcome to treasure island")
choice_1= input("whaich side you have to take right or left").lower()
  """
""" if choice_1=="right":
   print("you fell into a hole.game over")
else:
    choice_1=="left"
    print("you can go forward.")
    choice_path=input("by boat or aeroplane")
    if choice_path=="boat":
      print("your out shark has eaten you")
    else:
     choice_path=="aeroplane"
     print("you successfully landed on island") """
     #
""" print("welcome to treasure island.Here you have to find the treasure.")
choice=input("right or left").lower()
if choice=="right":
    print("you fell into a hole.Game is over.")
else:
    choice="left"
    choice=input("swim or wait")
    if choice=="swim":
        print("your eaten by crocodile.Game over")  
    else:
        choice=input("colourful doors red,yellow or blue")
        if choice=="red":
            print("you have fired.Game over")
        elif choice=="blue": """
"""             print("you have eaten by beast.Game over")
        elif choice=="yellow":
            print("you have won the game.")
        else:
            print("game over")      """   
#random number
import random


#
""" mystr="republic day"
print(mystr.count('r'))random_integer=random.randint(1,10)
print(random_integer)

random_float=round(random.random(),3)
print(random_float)
print(random_float*2)
love_score=random.randint(1,50)
print(love_score)
#
astring="hello world"
print ("the single quotation" '')
print(len(astring))    
#
mystr="Republic day"
print(mystr.index('R'))
#
mystr="january 26"
print(mystr[0:]) """

""" name="shaik asma gulzar"
first_name=name[:5]
middle_name=name[6:10]
last_name=name[11:]
#middle_name=last_name
print( middle_name)
print(first_name)
print(last_name) """
#
""" asma="new opperchunity"
print(asma.upper())
print ('asma starts with ("New opperchunity")')
print (asma=="New opperchunity")
print(4>5)
print(10==10)
print(7<4) 
row1=["🥲", "🥲", "🥸"]
row2=["🥸", "🥸", "🥸"]
row3=["🥸", "🥸", "🥸"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("where do you want to put the treasue ?")
horizantal=int(position[0])
verticle=int(position[1])
map[verticle -1][horizantal -1]="x"
print(f"{row1}\n{row2}\n{row3}")
select_row=map[verticle -1]
select_row=map[horizantal -1]  """
 
""" fruites= ["apple","peach","pear"]
for fruite in fruites:
    print(fruite)
    print(fruite+ "pie")
    print(fruite) 
print("asma" +" "+" introvent")
print("hello world\nhello world")
print("hello"+ input ("what is your name?" ))
 """
mystr="asma"
print(mystr[::-2])

print("hello"[4])

""" a=input("a:")
b=input("b:")
print("a:"+a)
print("b:"+b) """

""" firstnumber=int(input(" enter firstnumber"))
secondnumber=int(input(" enter secondnumber"))
thirdnumber=int(input(" enter thirdnumber")) 

if firstnumber  > secondnumber and firstnumber  > thirdnumber :
    print("maximum number=",firstnumber)
elif secondnumber > firstnumber and secondnumber > thirdnumber:
    print ("maximum number=",secondnumber)
elif thirdnumber > firstnumber and thirdnumber > secondnumber:
    print("maximum number=",thirdnumber) 
else: 
    print("you have not inputed proper values")
 """
""" english_marks=int(input("  enter english marks"))
science_marks=int(input(" enter science marks"))
maths_marks=int(input("  enter maths marks"))
totalmarks=english_marks+science_marks+maths_marks    
average_marks =totalmarks//3      
print("total marks= ",totalmarks)
print("average marks=", average_marks)
 """
""" grade=""
if average_marks >= 90 :
    grade="A+"
    print(" grade= ",grade)
elif average_marks >=70 :
    grade="A"
    print("grade= ",grade)
elif average_marks>=60:
    grade="B"
    print("grade= ",grade)
elif average_marks>=50:
    grade="C"
    print("grade= ",grade)
elif average_marks<50:
    grade="D"
    print("grade= ",grade)       
else:
    print("proper values please")
 """
import random
random_integer=random.randint(100,200)
print(random_integer)
random_float=random.random()
print(random_float)
random_float*5
random_float=random.randint(200,300)
print(random_float)

#password genrator project
""" import random
letters=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'v', 'w',
         'x', 'y', 'z']
numbers=['0','1', '2', '3', '4', '5', '6', '7', '8', '9',]
symbols=['#', '$', '&', '*', '^', '!', '@', '+', '-']
print("welcom to python password genrator")
nr_letters=int(input("how letters do you want in your password\n"))
nr_symbol=int(input("how many symbol do you want in your password\n"))
nr_numbers=int(input("how many numbers do you want in your password\n"))
#password=''
password_list=[]
for char in range(1, nr_letters +1):
    password_list+=random.choice(letters)

for char in range(1, nr_symbol +1):
    password_list+=random.choice(symbols)

for char in range(1, nr_numbers +1):
    password_list+=random.choice(numbers)

print(password_list)
 """
""" def my_code():
    print("this is my code")
    len=int(input("print"))
my_code() """


""" def addtwo_numbers(one,two):
    sum=one+two
    print(f"sum of {one}+{two}={sum}")
addtwo_numbers(6,7)
addtwo_numbers(30,400)

#write a function to take input of two num and display there multiplicatin.

def mutiplytwo_numbers(one,two):
    multiply=one*two
    print(f"product of {one}*{two}={multiply}")
mutiplytwo_numbers(5,30)

def multiplythree_numbers(one,two,three):
    multiply=one*two*three
    print(f"product of {one}*{two}*{three}={multiply}")
multiplythree_numbers(100,75,89) """

# #write a function to divide two numbers and get the quotient
# def dividetwo_numbers(first,second):
#     quotient=first/second
#     print(f"quotient of {first}/{second}= {quotient}")
# dividetwo_numbers(200,30)

""" x=1
y=2.89
z=1j
q="asma"
asma=["noodles", "manchuria", "maggie"]
 """
# """ print(type(x))
# #print(type(x+y))
# #print(type(x+z))
# print(type(y))
# print(type(z))
# print(type(q))
# print(type(asma))
# print(type(x+q)) """

#function with returing value
# def square_value(side):
#     square=side*side
#     return square
# squr=square_value(69)
# print(f"square value={squr}")

# def subracting_value(one,two):
#     subraction=one-two
#     return subraction
# sub=subracting_value(56,32)
# print(f"subracting value={sub}")

""" x="programmer"
print(len(x))
print("we are the VIKINGS of the north \n we are the VIKINGS of the north.") """

#list=["car","bus","bike","scooter"]
#def loop(x):
#   print(x)

from random import randint
def check_answer(guess,answer):
    if guess > answer:
        print("too high")
    elif guess < answer:
        print("too low")
    else:
        print(f"you got the correct{answer}")
#make function to make it easy or hard
def set_difficulty():
    level=input("choose difficulity. Type 'easy' or 'hard':")
    if level=="easy":
        turns=EASY_LEVEL_TURNS
    else:
        turns=HARD_LEVEL_TURNS
#CHOOSING A RANDOM NUMBER BETWEEN 1 AND 100
def game(): 
    print("welcom to the random number guessing game")
    print("iam thinking of a number between 1 and 100")
    answer=randint(1,100)
    print ("psst the correct answer is {answer}")
    turns=set_difficulty()
    print(f"you have{turns} attempt to guess the number")
    guess=0
    while guess!=answer:
        guess=int(input("make a guess"))
        check_answer(guess,answer)
game()











    



























