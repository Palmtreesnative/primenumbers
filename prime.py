from math import sqrt as rc

nombre = 1
inutile = 1
i = 2

while inutile == 1:
    a = 0
    racine = round(rc(nombre), 0) + 1

    for diviseur in range(1, int(racine)):
        if nombre % diviseur == 0:
            a+=1

        if a > 1:
            break

    if a == 1:
        print(nombre, "is prime.")

    i = 6 - i
    nombre += i
