fruits = ["banana","khasma","peach","pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+"pie")


Names = ["Asma"]
for Name in Names:
    print(Name)
    print(Name +"gulzar""shaik""sameen")
    print(Name + "gulzar","shaik","sameen")

# student_scores = input().split()
# for n in range (0,len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# highest_score =0
# for score in student_scores:
#     if score > highest_score:
#         highest_score = score

#for loop with range
for number in range (1,10,3):
    print(number)

# total = 0
# for number in range( 1, 500):                                   
#      total += number
#      print(total)

#fizzbuzz game:

target = 200
for number in range(1,target + 1):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0 :
    print("Fizz")
  elif number % 5 == 0 :
    print("Buzz")
  else:
    print(number)

#password generator
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u']
# symbols = ['@', '#', '$', '%', '&', '*']
# numbers = ['1', '2', '3', '4', '5', '6', '7']
# print("welcome to password generator")
# nr_letters = int(input("how many letters would you like in your password?\n"))
# nr_symbols = int(input("how many symbols would you like in your password\n"))
# nr_numbers = int(input("how many numbers would you like in your password\n"))

# password_list = []
# for char in range(1, nr_letters +1):
#   password_list.append(random.choice(letters))
#    #print(random_char)
# for char in range(1, nr_symbols +1):
#   password_list.append(random.choice(symbols))
#   # print(random_char)
# for char in range (1, nr_numbers +1):
#   password_list.append(random.choice(numbers))
#   # password += nr_numbers + nr_symbols + nr_letters
#   print(password_list)
#   random.shuffle(password_list)
#   print(password_list)

#   password = ""
#   for char in password_list:
#      password += char
#   print(f"your password is: {password}")

#function
# def converter(usd_val):
#    inr_val =usd_val * 83
#    print(usd_val, "usd =" , inr_val, "INR")
# ("converter 73")

# print("asma")

# def greet():
#    print("hello")
#    print("how is your day")
#    print("how are you?")
# greet()

# # function with input
# def greet_with_name(Asma):
#    print(f"hellow{Asma}")
#    print(f"how are you{Asma}")
# greet_with_name("Asma")
                             

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
# 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# #TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#       position =  alphabet.index(letter)
#       new_position = position + shift_amount
#       new_lettet = alphabet[new_position]
#       cipher_text  += new_lettet
#   print(f"The encoded text is {cipher_text}")
  

#     #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
#     #e.g. 
#     #plain_text = "hello"
#     #shift = 5
#     #cipher_text = "mjqqt"
#     #print output: "The encoded text is mjqqt"

#     ##HINT: How do you get the index of an item in a list:
#     #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

#     ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛                 

# #TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.  
# encrypt(plain_text=text,shift_amount=shift)

# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}



#nesting
# c""" apitals = {
#    "asma": "paris",
#    "germany":"Arizona",
# }

# travel_log ={
#    "asma":{"cities_visited":["paris", "lille","usa"],"total_visits":12},
#    "germany":{"cities_visited":["Arizona","jena","TUM","LUM","Bremen"],"total_visits":5},
# }       

# travel_log = [
#   {
#     "country":"asma",
#     "cities_visited":["paris","lille","dijon"],
#     "total_visits": 12

#   },

#   {
#   "country":"germany",
#   "cities_visited":["Arizona","jena","TUM"],
#   "total_visit":5
#   },
# ] """


def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        print("Leap year")
      else:
        print("Not leap year")
    else:
      print("Leap year")
  else:
    print("Not leap year")
  

def days_in_month(year,month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
  if month == 1 and is_leap(year):
    return 29
  else:
    return month_days[month - 1]
  

year = int(input(2024)) # Enter a year
month = int(input("2")) # Enter a month
days = days_in_month(year, month)
print(days)

#calculator
def add(n1, n2):
  return n1 + n2
def subtract(n1, n2):
  return n1 - n2
def multiply(n1, n2):
  return n1 * n2
def divide(n1,n2):
  return n1 / n2

operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide
}
def calculator ():
  num1 = int(input("What's the first number?:"))
  for symbol in operations:
    print(symbol)
  should_continue = True
while should_continue:
  operation_symbol = input("pick an operation from the line above:")
  num2 = int(input("what is the second number?:"))
  calculation_function = operations[operation_symbol]
  answer = calculation_function(num1, num2)

  print(f"{num1} {operation_symbol} {num2} = {answer}")
  if input (f"Type 'y to continue calculating with {answer}, or type 'n' to start a new
  calculation: ") == "y":
    num1 = answer
  else:
    should_continue = False
    calculator()

calculator()



operation_symbol = input("pick another operation:")
num3 = int(input("what's the next number?:"))
calculation_function = operations[operation_symbol]
answer = calculation_function(calculation_function(num1, num2,),num3)

print(f"{first_answer} {operation_symbol} {num3} =  {second_answer}")


