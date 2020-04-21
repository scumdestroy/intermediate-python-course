import random


dice_rolls = int(input("how many dice ye rollin?? ummm....? "))
dice_size = int(input('How many sides on them lucky boulders? well...? '))
dice_sum = 0

for i in range(1,dice_rolls):
  roll = random.randint(1,6)
  dice_sum += roll
  if roll == 1:
  	print('piss poor job mate, a bloody "one"')
  elif roll == 6:
  	print('bloody brilliant that roll, six six six the name')
  else:
  	print(f'You rolled a {roll}')

print(f'You rolled a total of {dice_sum}')