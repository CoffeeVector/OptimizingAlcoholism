#!/usr/bin/python3
import numpy as np
import matplotlib.pyplot as plt

t = np.array([[-3, 1],
              [1, -1]])

def transaction(a, b):
    return np.dot(t, np.array([[a],[b]])) + [[5], [5]]

ok = [] # ok points that have already been checked
check = [(0, 0)] # ok points, but may lead to more
tmp = []
while not len(check) == 0:
    for i in check:
        if not i in ok:
            ok.append(i)
        tran = transaction(i[0], i[1] + 1)
        if tran[0] >=0 and tran[1] >=0:
            tmp.append((i[0], i[1] + 1))
        tran = transaction(i[0] + 1, i[1])
        if tran[0] >=0 and tran[1] >=0:
            tmp.append((i[0] + 1, i[1]))
    check = tmp
    tmp = []

plt.scatter([i[0] for i in ok], [i[1] for i in ok], c=(0, 1, 0))
plt.scatter([5], [10], c=(1, 0, 0))
plt.xlabel('Bottle-based transactions')
plt.ylabel('Cap-based transactions')
plt.xticks(range(6))
plt.yticks(range(11))
plt.savefig('debt.png')
