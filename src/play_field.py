from pylab import *

X = range(1, 100, 1)
Y = []
for x in X:
    Y.append((0.666667**x)*x)

plot(X, Y)
show()
