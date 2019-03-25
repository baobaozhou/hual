from bulid_dictionary import *
import re

'''
匹配有关系的cpdp
'''


def match_cpdp():
    dict_2 = bulid_cpdp_dict()
    name_list = get_name('./dict_cpdp')
    with open('./deal_data/tag_model', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            temp = line.split('\t')
            temp_7 = []
            with open('./result_data/match_cpdp', 'a', encoding='utf-8')as f:
                if re.match(u'(.*)\\{{(.*)\\}}(.*)', temp[4]):
                    temp_2 = re.findall(u'(?<=\\{{)[^\\}}]+', temp[4])
                    if all(i not in name_list for i in temp_2):
                        f.write(line)
                    else:
                        for i in temp_2:
                            if i in name_list:
                                if temp[0] == 'cd':
                                    try:
                                        temp_1 = dict_2[i]['cd'].split('\t')
                                    except:
                                        continue
                                    temp_1.remove('')
                                    for j in temp_1:
                                        temp_5 = j.split(',')
                                        result_str = line.replace('ComplexProperty', temp_5[0]).replace('datatype',
                                                                                                        temp_5[1])
                                        f.write(result_str)
                                elif temp[0] == 'c':
                                    try:
                                        temp_3 = dict_2[i]['cd'].split('\t')
                                    except:
                                        continue
                                    temp_3.remove('')
                                    for j in temp_3:
                                        temp_6 = j.split(',')
                                        temp_7.append(temp_6[0])
                                    temp_8 = list(set(temp_7))
                                    for m in temp_8:
                                        result_str = line.replace('ComplexProperty', m)
                                        f.write(result_str)
                                elif temp[0] == 'd':
                                    try:
                                        temp_4 = dict_2[i]['d'].split('\t')
                                    except:
                                        continue
                                    temp_4.remove('')
                                    for k in temp_4:
                                        result_str = line.replace('datatype', k)
                                        f.write(result_str)
                                else:
                                    f.write(line)
                            else:
                                continue
                else:
                    f.write(line)


'''
匹配词表
'''


def match_vocab():
    dict_3 = bulid_vocab_dict()
    with open('./result_data/match_cpdp', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            temp_4 = line.split('\t')
            with open('./result_data/match_vocab', 'a', encoding='utf-8')as f_1:
                if re.match(u'(.*)\\<(.*)\\>(.*)', temp_4[4]):
                    temp = re.findall(u'(?<=\\<)[^\\>]+', temp_4[4])
                    # temp中没有同义词
                    if all(i not in dict_3.keys() for i in temp):
                        f_1.write(line)
                    # temp中有同义词
                    else:
                        for i in temp:
                            if i in dict_3.keys():
                                temp_1 = dict_3[i]
                                temp_2 = temp_1.split(',')
                                for j in temp_2:
                                    temp_3 = line.replace(i, j)
                                    f_1.write(temp_3)
                            else:
                                continue
                else:
                    f_1.write(line)


if __name__ == '__main__':
    match_cpdp()
    match_vocab()
