def duplicate_count(text):
    text = text.lower()
    total = 0
    counter = 0
    my_list = []
    new_list = []
    for z in text:
        my_list.append(z)

    for i in my_list:
        for counter, q in enumerate(my_list):
            if counter > 0:
                if i == q:
                    total += 1
                    break
                else:
                    continue
            else:
                continue
        counter = 0
        my_list = [s for s in my_list if s != i]

    return total