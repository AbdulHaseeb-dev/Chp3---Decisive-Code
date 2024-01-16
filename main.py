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

#practice no.2
number_of_scoops = input('Enter the number of scoops of ice cream you would like to get') 
if int(number_of_scoops) == 0:
  print("You didn't want any ice cream?")
  print('We have lots of flavors.')
elif int(number_of_scoops) == 1:
  print('A single scoop for you, coming up.')
elif int(number_of_scoops) == 2:
  print('Oh, two scoops for you!')
elif int(number_of_scoops) >= 3:
  print("Wow, that's a lot of scoops!")
else:
  print("I'm sorry I can't give you negative scoops.")