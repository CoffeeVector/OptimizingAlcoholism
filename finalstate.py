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

print final(5, 5)
print "capcount: " + str(capcount)
print "botcount: " + str(botcount)
