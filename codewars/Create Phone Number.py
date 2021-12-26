def create_phone_number(n):
    phone="("
    for counter, i in enumerate(n) :
        c=str(i)
        phone+=c
        if counter == 2:
            phone+=") "
        if counter == 5:
            phone+="-"
    return phone