import random
from random import randint
numerating = random.randrange(0, 100)
enum = enumerate(int(numerating))
for i in enumerate(int(numerating)):
    print(i)
print(list(enum))