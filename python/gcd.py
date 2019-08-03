import matplotlib.pyplot as plt 
points = []

def gcd(a, b):
    points.append((a, b))
    if a > b:
        return gcd(a - b, b);
    elif a < b:
        return gcd(a, b - a);
    points.append((a, b))
    return a

print gcd(101, 23);
print points
x = []
y = []
for i in points:
    x.append(i[0])
    y.append(i[1])
print x
print y
plt.plot(x, y)
plt.show()
