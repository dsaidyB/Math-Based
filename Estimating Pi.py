import math
import random

tries = 10000000

countX = 0

for i in range(0, tries):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if (x**2 + y**2 <= 1):
        countX += 1

pi = 4*countX/tries     #could also use y but in the condition, it includes both
print("Pi is about", pi)        #3.14153584
print()
print("Pi is actually about", math.pi)

# n*sin(pi/n)

# 2 X 2 sqaure --> 1 radius circle
# As = 4
# Ac = pi
# 4 * Ac/As = pi