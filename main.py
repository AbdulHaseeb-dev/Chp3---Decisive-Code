#Rock Paper Scissor game
import random
random_choice = random.randint(0, 2)
print('The computer chooses', random_choice)


#practice
bank_balance = 50
ferrari_cost = 20
decision = bank_balance > ferrari_cost
print(decision)

if bank_balance >= ferrari_cost:
  print('Why not?')
  print('Go ahead, buy it')
else:
  print('Sorry')
  print('Try again next week')