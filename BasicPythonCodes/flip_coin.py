import decorators
import random

heads_count = 0
tails_count = 0

total_flip_count = decorators.take_input("Enter no of time you want to flip a coin")

for current_flip_count in range(0, total_flip_count):
    if round(random.random()) == 1:
        heads_count+=1
    else:
        tails_count+=1


print(f'Percent of heads =  {(heads_count/total_flip_count)*100 }')
print(f'Percent of tails =  {(tails_count/total_flip_count)*100 }')

