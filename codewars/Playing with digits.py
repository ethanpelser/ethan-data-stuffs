def dig_pow(n, p):
    l=0
    n=str(n)
    for counter, i in enumerate(n):
        l+=int(i)**(p+counter)
    if int(l)%int(n)==0:
        return int(l)/int(n)
    else:
        return -1