def to_jaden_case(x):
    words=[]
    s=" "
    y=x.split(" ")

    for i in y:
        words.append(i.capitalize())
    m=s.join(words)
    return m