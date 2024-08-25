def trans(text, replaceA, replaceB):
    oldA, newA = replaceA
    oldB, newB = replaceB
    res = []
    for i in range(len(text)):
        if text[i] == oldA:
            res.append(newA)
        elif text[i] == oldB:
            res.append(newB)
        else:
            res.append(text[i])
    text_trans = ''
    for i in range(len(res)):
        text_trans = text_trans + res[i]
    return text_trans


# Code principal
print(trans('ABBAB', ('A','AB'), ('B','BA')))
print(trans('piton', ('i','y'), ('t','th')))