import collections
import re
from utlis.load_file import *
from utlis.get_text_name import *
from utlis.sort_out import *


def expand_template():
    t_na = get_name('./template_library')
    dict_data = load_build_dict('./template_data/template_dict')

    with open('./template_data/expand_template', 'a', encoding='utf-8')as f1:
        for u in t_na:
            with open('./template_library/' + u, 'r', encoding='utf-8')as f:
                for i in f.readlines():
                    temp = re.findall('(?<=\\[)[^\\]]+', i)
                    count = collections.Counter(temp)
                    count_1 = collections.Counter(temp)
                    for k, v in count.items():
                        count[k] = 0
                    for j in temp:
                        if count[j] == 0:
                            if j in dict_data.keys():
                                if count_1[j] == 2:
                                    count[j] = 1
                                    rule = re.compile(j)
                                    t3 = dict_data[j]
                                    t4 = t3.split('\t')
                                    t4.remove('')
                                    for k in t4:
                                        t5 = i.replace(j, k, 1)
                                        for l in t4:
                                            t6 = rule.split(t5)
                                            if len(t6) == 2:
                                                t7 = t5.replace(j, l)
                                                f1.write(t7.strip('\n') + '\t' + i)
                                            elif len(t6) == 3:
                                                t6.insert(2, '*')
                                                t6.insert(1, j)
                                                t8 = ''.join(t6)
                                                t9 = t8.replace('*', l)
                                                f1.write(t9.strip('\n') + '\t' + i)
                                else:
                                    t3 = dict_data[j]
                                    t4 = t3.split('\t')
                                    t4.remove('')
                                    for k in t4:
                                        t10 = i.replace(j, k)
                                        f1.write(t10.strip('\n') + '\t' + i)
                            else:
                                continue

def template_mapping():
    t = load_data('./template_data/temp_data')
    t1 = load_data('./template_data/expand_template')
    with open('./template_data/temp', 'a', encoding='utf-8')as f:
        for i in t1:
            t4 = i.split('\t')
            t3 = t4[0]
            temp = ['u', 'p', 'm']
            t2 = re.findall('(?<=\\[)[^\\]]+', t3)
            for k in temp:
                for j in t2:
                    if re.match('(.*)' + k + '(.*)', j):
                        t3 = t3.replace('[' + j + ']', '')
            for l in t:
                t5 = l.strip('\n')
                if t5 == t3:
                    f.write(t5 + '\t' + t4[1])
                else:
                    continue

    t6 = load_data('./template_data/temp')
    t7 = sort_out(t6)
    with open('./template_data/temp1', 'a', encoding='utf-8')as f:
        for u in t7:
            f.write(u)

    os.remove('./template_data/temp')



# t = load_data('./template_data/temp1')
# t1 = load_data('./template_data/temp_data')
# zhou = []
#
# for i in t:
#     t2 = i.split('\t')
#     zhou.append(t2[0])
#
# with open('./template_data/match_template', 'a', encoding='utf-8')as f:
#     for k in t1:
#         t3 = k.strip('\n')
#         if t3 in zhou:
#             for j in t:
#                 t4 = j.split('\t')
#                 if t4[0] == t3:
#                     f.write(t3 + '\t' + t4[1])
#                 else:
#                     continue
#         else:
#             f.write(k)


# if __name__ == '__main__':
    # expand_template()
    # template_mapping()
