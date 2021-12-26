def find_nb(m):
    total= m
    counter=0
    while total > 0 or total < 0 :
        if total < 0:
            return -1
        else:
            counter+=1
            total=total-counter**3
    return counter