from utlis.get_text_name import *
from utlis.sort_out import *
from utlis.load_file import *


def match_data(intetion_result_path, save_path):
    dir_list = get_name(intetion_result_path)
    zhou = []
    for i in dir_list:
        with open(intetion_result_path + i, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                zhou.append(line)
    hui = sort_out(zhou)
    with open(save_path, 'a', encoding='utf-8')as f_1:
        for j in hui:
            f_1.write(j)


def result(tag_data_path, query_temp_path, save_pth):
    content = load_data(tag_data_path)
    content_1 = load_data(query_temp_path)
    with open(save_pth, 'a', encoding='utf-8')as f:
        for i in content_1:
            temp = i.split('\t')
            temp_2 = i.strip('\n')
            a = ''
            for j in content:
                temp_1 = j.split('\t')
                if temp_1[1] == temp[1]:
                    a += temp_1[0]
                else:
                    continue
            f.write(temp_2 + '\t' + a + '\n')


if __name__ == '__main__':
    match_data('./intention_result/', './generate_result/tag_data')
    result('./generate_result/tag_data', './origin_data/query_temp', './generate_result/result_data')

