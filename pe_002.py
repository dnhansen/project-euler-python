f1 = 1
f2 = 2
s = 2

f = f1 + f2
while f <= 4000000:
    f = f1 + f2
    if f % 2 == 0:
        s += f

    # Update f1 and f2
    f1 = f2
    f2 = f

print(s)
