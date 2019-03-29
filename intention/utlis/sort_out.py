'''
utf-8去重并排序
'''


def sort_out(path):
    temp = []
    with open(path, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            temp.append(line)
    temp_1 = list(set(temp))
    temp_1.sort(key=temp.index)
    return temp_1


'''
gbk
'''


def sort_out_1(path):
    temp = []
    with open(path, 'r', encoding='gbk')as f:
        for line in f.readlines():
            temp.append(line)
    temp_1 = list(set(temp))
    temp_1.sort(key=temp.index)
    return temp_1
