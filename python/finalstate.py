#!/usr/bin/python
import matplotlib.pyplot as plt
cap = 3
bot = 1
capcount = 0
botcount = 0

def final(a, b):
    global capcount
    global botcount
    if a >= cap:
        capcount = capcount + 1
        return final(a - 3, b + 1)
    elif b >= bot:
        botcount = botcount + 1
        return final(a + 1, b - 1)
    return (a, b)

finalVectors = [final(i, i) for i in range(30)]

caps = [i for i,j in finalVectors]
bots = [j for i,j in finalVectors]

x = range(30)

plt.plot(x, bots, label="Bottles left over")
plt.xticks(x)
plt.legend()
plt.savefig("bots.png")
plt.clf()
plt.plot(x, caps, label="Caps left over")
plt.xticks(x)
plt.legend()
plt.savefig("caps.png")
