#!/usr/bin/python
import matplotlib.pyplot as plt

cap = 4 - 1
bot = 2 - 1

capcount = 0
botcount = 0

def final(a, b):
    global capcount
    global botcount
    if a / cap > 0:
        capcount = capcount + (a / cap)
        return final(a % cap , b)
    elif b / bot > 0:
        botcount = botcount + (b / bot)
        return final(a, b % bot)
    return (a, b)

finalVectors = [final(i, i) for i in range(30)]

caps = [i for i,j in finalVectors]
bots = [j for i,j in finalVectors]

x = range(30)

plt.plot(x, bots)
plt.savefig("bots.png")
plt.plot(x, caps)
plt.savefig("caps.png")
