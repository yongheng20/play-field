import numpy as np

matrix = np.random.random([100000, 5])
list = []
for li in matrix:
    list.append(min(li))

print "expectation of minimum number is: {0}".format(np.average(list))
