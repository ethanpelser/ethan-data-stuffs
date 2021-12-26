def beeramid(bonus, price):
    counter = 0
    q = 0
    possible = bonus//price

    if possible < 1:
        return 0
    while q < possible:
        counter+=1
        q = q +counter**2

    if q == possible:
        return counter
    else:
        return counter - 1