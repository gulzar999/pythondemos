import random
rock = '''

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = input("what do you choose?\nType 0 for Rock, 1 for Paper or 2 for Scissors.\n")
computer_choice = random.randint(0,2)
print(f"computer chose {computer_choice}")

if user_choice == 0 and computer_choice == 2:
    print("you win")
elif computer_choice == 0 and user_choice == 2:
    print("you loose")
#elif user_choice < computer_choice:
    #22print("you loose")
elif computer_choice == user_choice:
    print("its a draw")
else:
    print("you typed an invalid number, you loose")