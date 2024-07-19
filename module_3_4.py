def single_root_words(root_word,*other_words):
    same_words=[]
    for i in other_words:
        y = i.count(root_word)
        if y>=1:
            same_words.append(i)
        else:
            continue
    for j in other_words:
        f=j.lower()
        t=root_word.lower()
        z = t.count(f)
        if z>=1:
            same_words.append(j)
        else:
            continue
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
