
import random

def randInt(max=100):
    print(int(random.random() * max))

randInt()
randInt(max=50)

def randInt(min):
    print(int(random.random() * min) + min)

randInt(min=50)
