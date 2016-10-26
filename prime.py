from math import sqrt as rc

nb = 1
b = 2

while nb < 100000:
    a = 0

    for i in range(2, int(round(rc(nb), 0) + 1)):
        if nb % i == 0:
            a += 1
            break

    #if a == 0: print(nb, "is prime.")
    b = 6 - b
    nb += b
