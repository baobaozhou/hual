import collections

'''
加载词表
'''


def load_vocab_data(path_1, path_2):
    list_1 = []
    list_2 = []
    list_3 = []
    with open(path_1, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            tmp = line.split('\t')
            # print(tmp)
            del tmp[0]
            if len(tmp) == 2:
                list_3.append(tmp[0])
    d = collections.Counter(list_3)
    for k, v in d.items():
        if v > 1:
            list_1.append(k)
    length = len(list_1)
    # 用list存储不同的变量
    for i in range(length):
        list_2.append('')
    with open(path_2, 'a', encoding='utf-8')as f_2:
        with open(path_1, 'r', encoding='utf-8')as f_1:
            for line_1 in f_1.readlines():
                temp_1 = line_1.split('\t')
                del temp_1[0]
                if len(temp_1) == 2:
                    if temp_1[0] not in list_1:
                        f_2.write(temp_1[0] + '\t' + temp_1[1].strip('\n') + '\n')
                    else:
                        n = 0
                        while n < length:
                            if list_1[n] == temp_1[0]:
                                list_2[n] += temp_1[1].strip('\n') + ','
                            n = n + 1
            for i, j in zip(list_2, list_1):
                temp_2 = i.strip(',')
                temp_3 = temp_2.split(',')
                temp_4 = list(set(temp_3))
                temp_5 = ','.join(temp_4)
                f_2.write(j + '\t' + temp_5 + '\n')
