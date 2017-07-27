a = input("input number a: ")
b = input("input number b: ")
x1, y1 = 1, 0
x2, y2 = 0, 1

r = a % b
q = a / b

if r != 0:
    a = b
    b = r
    while True:
        x3 = x1 - x2*q
        y3 = y1 - y2*q
        x1, y1 = x2, y2
        x2, y2 = x3, y3
        r = a % b
        q = a / b
        print x1, y1, x2, y2, a, b, q, r
        if r == 0:
            break
        a = b
        b = r

print "\nThe greatest common divisor of input number is {0}.".format(b)
print "And that {0}*a + {1}*b = {2}.".format(x2, y2, b)
