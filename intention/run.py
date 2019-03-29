from utlis.get_text_name import *
from utlis.load_file import *
from utlis.sort_out import *


def match_data(dir_list, word_list, dir_path, save_path):
    res_list = []
    for i in dir_list:
        with open(dir_path + i, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                temp = line.strip('\n')
                res_list.append(temp)
    with open(save_path, 'a', encoding='utf-8')as f_1:
        for k in word_list:
            temp_2 = k.strip('\n')
            for l in res_list:
                temp_1 = l.split('\t')
                if temp_1[0] == temp_2:
                    f_1.write(l + '\n')
                else:
                    continue


if __name__ == '__main__':
    dir_list = get_name('./intention_result')
    word_list = load_data('./origin_data/data.txt')
    match_data(dir_list, word_list, './intention_result/', './generate_result/result')
    temp = sort_out('./generate_result/result')
    with open('./generate_result/tag_data', 'a', encoding='utf-8')as f_2:
        for m in temp:
            f_2.write(m)
    temp_1 = sort_out_1('./origin_data/data.txt')
    with open('./generate_result/data', 'a', encoding='utf-8')as f_3:
        for n in temp_1:
            f_3.write(n)

    data = load_data_1('./generate_result/data')
    tag_data = load_data_1('./generate_result/tag_data')
    temp = []
    for j in tag_data:
        temp_1 = j.strip('\n')
        temp_2 = temp_1.split('\t')
        temp.append(temp_2[0])
    with open('./generate_result/no_tag_data', 'a', encoding='utf-8')as f:
        for i in data:
            temp_3 = i.strip('\n')
            if temp_3 not in temp:
                f.write(temp_3 + '\n')
    os.remove('./generate_result/result')