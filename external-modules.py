import random
import math
#random.randint(start, end) - prints ay integer between start to end
#random.random - prints any random number between 0-1, you can multiply it with perticular number to make it between certain numbers.
#random.choice - prints anything of that choice

lst1=['will get project in jan', 'will not get project in jan']

print(random.randint(1,5))
print(math.floor(random.random()*100))
print(random.choice(lst1))

