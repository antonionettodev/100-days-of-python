"""
0 - pedra
1- papel
2 - tesoura
"""
import random

figures = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''',
]

player_choice = int(input('Qual você escolhe? 1- Pedra\n2- Papel\n3- Tesoura')) - 1
print('Jogador Escolhe:')
print(figures[player_choice])

computer_choice = random.randint(0,2)
print('Computador Escolhe:')
print(figures[computer_choice])

if player_choice == computer_choice:
    print('Empate')

if player_choice == 0 and computer_choice == 2:
    print('Você ganhou')
elif player_choice == 2 and computer_choice == 1:
    print('Você ganhou')
elif player_choice == 1 and computer_choice == 0:
    print('Você ganhou')

if computer_choice == 0 and player_choice == 2:
    print('Computador ganhou')
elif computer_choice == 2 and player_choice == 1:
    print('Computador ganhou')
elif computer_choice == 1 and player_choice == 0:
    print('Computador ganhou')