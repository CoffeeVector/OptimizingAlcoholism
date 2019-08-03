import numpy as np

m = np.matrix([[-3, 1],
               [1, -1]])
inv = np.matrix([[-0.5, -0.5],
                 [-0.5, -1.5]])
print np.dot(m, inv)
init = np.matrix([[7],
                  [7]])
final_test = np.matrix([[2],
                        [0]])
diff = np.subtract(final_test, init)

print np.dot(inv, diff)
