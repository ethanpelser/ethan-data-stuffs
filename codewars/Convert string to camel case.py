import re
def to_camel_case(text):
    joiner=""
    newer_text=""
    new_text=re.split("-|_",text)
    for counter, i in enumerate(new_text):
        if counter==0:
            newer_text=i
        else:
            newer_text+= str(i).capitalize()
    return newer_text