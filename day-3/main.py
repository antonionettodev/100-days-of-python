print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Bem vindo à ilha do tesouro.')
print('Sua missão é achar o tesouro.')

choice1 = input('Você chega em uma ilha, para qual lado você vai?\n1-Esquerda ou 2-Direita?')
if choice1 == '1':
    choice2 = input('Você vai p1ra esquerda e se depara com um rio.\n1-Nadar ou 2-Esperar?')
    if choice2 == '2':
      choice3 = input('Um barqueiro aparece e te oferece uma carona até um castelo com 3 portas, qual você escolhe?\n1- Vermelha 2- Amarela 3- Azul')
      if choice3 == '1':
          print('Você entra pela porta vermelha e a sala pega fogo.\nGAME OVER.')
      elif choice3 == '2':
          print('Você entra em uma sala cheia de moedas de ouro e encontra o tesouro.\nVOCÊ VENCEU.')
      elif choice3 == '3':
          print('Você entra em uma sala e é atacado por esqueletos.\nGAME OVER.')
    else:
        print('Você entra no rio mas não sabe nadar.\nGAME OVER.') 
else: 
    print('Você vai pra direita e cai em um buraco.\nGAME OVER.')