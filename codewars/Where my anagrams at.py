def anagrams(word, words):
    my_array = []
    for i in words:
        if sorted(word) == sorted(i):
            my_array.append(i)
        else:
            continue
    return my_array
