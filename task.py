rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper='''
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

import random
game_image=[rock,paper,scissors]
choice=int(input("enter ur choice '0' for rock/'1' for paper,'2' for scissor"))
if choice>=0 and choice<3:
    print(game_image[choice])

computer_choice=random.randint(0,2)
print(computer_choice)
if computer_choice==0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''')
elif computer_choice==1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''')
elif computer_choice==2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''')
if computer_choice==0 and choice=="2":
    print("you lose")
elif computer_choice==2 and choice=="0":
    print("you won")
elif int(choice)<computer_choice:
    print("you lose")
elif computer_choice<int(choice):
    print("you win")
elif int(choice)==computer_choice:
    print("draw")



