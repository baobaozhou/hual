'''
gbk加载数据
'''


def load_data(path):
    with open(path, 'r', encoding='gbk')as f:
        content_list = f.readlines()
    return content_list


'''
utf-8加载数据
'''


def load_data_1(path):
    with open(path, 'r', encoding='utf-8')as f:
        content_list = f.readlines()
    return content_list


'''
加载词典
'''


def load_build_dict(path):
    dict = {}
    with open(path, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            temp_2 = ''
            temp = line.strip('\n')
            temp_1 = temp.split(' ')
            for i in temp_1:
                temp_2 += i + '\t'
                dict.update({temp_1[0]: temp_2})
            # 每个词都作为key
            # length = len(temp_1)
            # for j in range(length):
            #     temp_2 = ''
            #     for i in temp_1:
            #         if temp_1.index(i) != j:
            #             temp_2 += i + '\t'
            #             dict.update({temp_1[j]: temp_2})
            #         else:
            #             continue
    return dict
