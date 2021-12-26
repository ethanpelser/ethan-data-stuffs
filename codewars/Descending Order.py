def descending_order(num):
    s=""
    num=str(num)
    list_1=[]
    for i in num:
        list_1.append(i)
    list_1.sort(reverse=True)
    return int(s.join(list_1))