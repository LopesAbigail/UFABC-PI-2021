x = float(input())
f = 0

if x <= 1:
    f = 1
elif x <= 5:
    f = x
elif x <= 10:
    f = x ** 2
else:
    f = x ** 3
print("f(x) = %.2f" % f)
