#!/usr/bin/python
import random
import math
random.randint.__doc__

def discriminant(a, b, c):
    delta = b * b - 4 * a * c 
    return delta

a = random.randint(-20,20)
b = random.randint(-50,50)
c = random.randint(-100,100)

discriminant(a, b, c)

