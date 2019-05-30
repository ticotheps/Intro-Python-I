# 1. Create a list of 10 random numbers between -25 and 25

import random

random_list = []

for x in range(10):
    random_list.append(random.randint(-25, 25))

print(random_list)

# 2. Use the list from question 1 and, utilizing a list comprehension, 
#    create a new list that only contains the negative numbers.

y = [i for i in random_list if i < 0]

print(y)
