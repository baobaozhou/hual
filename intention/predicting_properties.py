from utlis.load_file import *
import re
import os

rule = load_data('./generate_result/annotation_rule')
data = load_data('./generate_result/pre_property_data')

with open('./generate_result/pre_result', 'a', encoding='utf-8')as f:
    for i in rule:
        temp = i.split('\t')
        temp_1 = temp[1].split(',')
        if len(temp_1) == 2:
            temp_2 = re.findall('cp=(.*)', temp_1[0])
            temp_2_1 = ''.join(temp_2)
            temp_3 = re.findall('dp=(.*)', temp_1[1])
            temp_3_1 = ''.join(temp_3)
            for j in data:
                zhou = j.strip('\n')
                temp_4 = zhou.split('\t')
                if temp_4[2] == temp[0]:
                    temp_5 = temp_4[1].split(' ')
                    if temp_2_1 == 'v':
                        for k in temp_5:
                            o = k.replace('vn', 'v')
                            temp_6 = re.findall('(.*)=v', o)
                            if len(temp_6) != 0:
                                temp_6_1 = ''.join(temp_6)
                                f.write(zhou + '\t' + 'cp=' + temp_6_1 + '\t' + 'dp=' + temp_3_1 + '\n')
                    elif temp_2_1 == 'v1':
                        temp_7 = []
                        for k in temp_5:
                            o = k.replace('vn', 'v')
                            temp_6 = re.findall('(.*)=v', o)
                            if len(temp_6) != 0:
                                temp_6_1 = ''.join(temp_6)
                                temp_7.append(temp_6_1)
                        f.write(zhou + '\t' + 'cp=' + temp_7[0] + '\t' + 'dp=' + temp_3_1 + '\n')
                    elif temp_2_1 == 'v2':
                        temp_7 = []
                        for k in temp_5:
                            o = k.replace('vn', 'v')
                            temp_6 = re.findall('(.*)=v', o)
                            if len(temp_6) != 0:
                                temp_6_1 = ''.join(temp_6)
                                temp_7.append(temp_6_1)
                        f.write(zhou + '\t' + 'cp=' + temp_7[1] + '\t' + 'dp=' + temp_3_1 + '\n')
        elif len(temp_1) == 1:
            temp_3 = re.findall('dp=(.*)', temp_1[0])
            temp_3_1 = ''.join(temp_3)
            for j in data:
                zhou = j.strip('\n')
                temp_4 = zhou.split('\t')
                if temp_4[2] == temp[0]:
                    f.write(zhou + '\t'*2 + 'dp=' + temp_3_1 + '\n')

t2 = load_data('./generate_result/pre_result')

with open('./generate_result/predict_result', 'a', encoding='utf-8')as f:
    for i in data:
        tem = i.split('\t')
        for j in t2:
            te = j.split('\t')
            if te[0] == tem[0]:
                f.write(j)
os.remove('./generate_result/pre_property_data')
os.remove('./generate_result/pre_result')
