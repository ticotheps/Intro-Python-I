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


# 3. Create a tuples with 3 of your favorite foods, loop through the 
#    tuple and print out each item.
#    tuples = read-only type of list in python

z = ("spaghetti", "cheese burgers", "pizza")

for i in z:
    print(i)

# 4. Create a set of 10 random numbers between 1 and 100, search the 
#    set for the value 50 and then print out a statement indicating 
#    whether or not the set contains 50.

random_set = random.sample(range(1,100), 10)

print(random_set)

c = [i for i in random_set if i == 50]

if len(c) > 0:
    print("The set DOES contain the number 50")
else:
    print("The set does not contain the number 50")

# 5. Create a dictionary containing some of your favorite books or
#    movies and a numerical rating from 1 to 5 for each item.

fav_movies = {
  "Wedding Crashers": 3,
  "Aquaman": 4,
  "Crazy Rich Asians": 5
}

print(fav_movies)