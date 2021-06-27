l1 = []
l2 = []
with open('./source_BIO_2014_cropus.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        l1.append(line.strip().split(" "))

with open('./target_BIO_2014_cropus.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        l2.append(line.strip().split(" "))

with open('./org.txt', 'w', encoding='utf-8') as f:
    for i, vs in enumerate(l1):
        for in_i, each_font in enumerate(vs):
            if l2[i][in_i] not in ["B_ORG", "I_ORG"]:
                flag = "O"
            elif l2[i][in_i] == "B_ORG":
                flag = "B-ORG"
            elif l2[i][in_i] == "I_ORG":
                flag = "I-ORG"
            f.write(each_font + " " + flag + '\n')
        f.write('\n')
