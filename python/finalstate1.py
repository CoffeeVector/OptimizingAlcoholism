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

finalVectors = [final(i, i) for i in range(10)]

caps = [i for i,j in finalVectors]
bots = [j for i,j in finalVectors]

x = range(10)

plt.plot(x, bots, label="Bottles left over")
plt.xticks(x)
plt.legend()
plt.savefig("bots1.png")
plt.clf()
plt.plot(x, caps, label="Caps left over")
plt.xticks(x)
plt.legend()
plt.savefig("caps1.png")
