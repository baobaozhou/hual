from utlis.load_file import *
from utlis.read_excel import *
import os

save_cols_2('./origin_data/test.xlsx', 0, 0, 1, 2, './generate_result/pre_property_data')

save_data('./origin_data/test.xlsx', 0, './generate_result/test_data')

content = load_data('./generate_result/test_data')

with open('./generate_result/annotation_rule', 'a', encoding='utf-8')as f:
    for i in content:
        temp = i.strip('\n').split('\t')
        if len(temp[3]) != 0:
            f.write(temp[2] + '\t' + temp[3] + '\n')

os.remove('./generate_result/test_data')

