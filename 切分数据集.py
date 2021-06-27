import random


def split(full_list, shuffle=True, ratio=0.8):
    n_total = len(full_list)
    offset = int(n_total * ratio)
    if n_total == 0 or offset < 1:
        return [], full_list
    if shuffle:
        random.shuffle(full_list)
    sublist_1 = full_list[:offset]
    sublist_2 = full_list[offset:]
    return sublist_1, sublist_2


li = []
inner_li = []
with open('./org.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        if line.strip() != "":
            inner_li.append(line.strip())
        else:
            li.append(inner_li)
            inner_li = []

l1, l2 = split(li, shuffle=True, ratio=0.8)
l3, l4 = split(l2, shuffle=True, ratio=0.5)
with open('./epoch_my.train', 'w', encoding='utf-8') as f:
    for each in l1:
        for line in each:
            f.write(line + '\n')
        f.write('\n')

with open('./epoch_my.test', 'w', encoding='utf-8') as f:
    for each in l3:
        for line in each:
            f.write(line + '\n')
        f.write('\n')

with open('./epoch_my.dev', 'w', encoding='utf-8') as f:
    for each in l4:
        for line in each:
            f.write(line + '\n')
        f.write('\n')
