# coding: utf-8
import re
from utlis.load_file import *
from utlis.load_file import load_build_dict

'''
数量
'''


def amount():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['数量']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    for j in temp_1_1:
        for i in word:
            with open('./intention_result/数量', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '数量' + '\n')
                else:
                    continue


'''
人物
'''


def character():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['谁']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['哪位']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    # 人物1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/人物', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '人物' + '\n')
                else:
                    continue
    # 人物2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/人物', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '人物' + '\n')
                else:
                    continue


'''
条件
'''


def condition():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['要求']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['要']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['什么']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    # 条件1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/条件', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '条件' + '\n')
                else:
                    continue
    # 条件2
    for k in temp_2_1:
        for l in temp_3_1:
            for i in word:
                with open('./intention_result/条件', 'a', encoding='utf-8')as f:
                    temp = i.strip('\n')
                    if re.match('(.*)' + k + '(.*)' + l + '(.*)', temp):
                        f.write(temp + '\t' + '条件' + '\n')
                    else:
                        continue


'''
确认
'''


def confirm():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['能']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['能否']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['吗']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    # 确认1
    for j in temp_1_1:
        for l in temp_3_1:
            for i in word:
                with open('./intention_result/确认', 'a', encoding='utf-8')as f:
                    temp = i.strip('\n')
                    if re.match('(.*)' + j + '(.*)' + l + ']$', temp):
                        f.write(temp + '\t' + '确认' + '\n')
                    else:
                        continue
    # 确认2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/确认', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '确认' + '\n')
                else:
                    continue


'''
内容
'''


def content():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['什么']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['包括']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    # 内容1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/内容', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)有(.*)' + j + '(.*)', temp) or re.match('(.*)可(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '内容' + '\n')
                else:
                    continue

    # 内容2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/内容', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '内容' + '\n')
                else:
                    continue


'''
定义
'''


def definition():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['什么']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['定义']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    # 定义1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/定义', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)是(.*)' + j + '(.*)', temp) or re.match('(.*)' + j + '(.*)是(.*)', temp):
                    f.write(temp + '\t' + '定义' + '\n')
                else:
                    continue
    # 定义2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/定义', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '定义' + '\n')
                else:
                    continue


'''
程度
'''


def degree():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['程度']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    for j in temp_1_1:
        for i in word:
            with open('./intention_result/程度', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '程度' + '\n')
                else:
                    continue


'''
评价
'''


def evalution():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['评价']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['如何']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    # 评价1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/评价', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '评价' + '\n')
                else:
                    continue
    # 评价2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/评价', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)n(.*)' + k + ']$', temp):
                    f.write(temp + '\t' + '评价' + '\n')
                else:
                    continue


'''
寒暄
'''


def greeting():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['你好']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['谢谢']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    # 寒暄1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/寒暄', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '寒暄' + '\n')
                else:
                    continue
    # 寒暄2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/寒暄', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '寒暄' + '\n')
                else:
                    continue


'''
地点
'''


def location():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['哪里']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    # 地点1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/地点', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '地点' + '\n')
                else:
                    continue


'''
方法
'''


def method():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['如何']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['方式']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    # 方式1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/方式', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)v(.*)', temp):
                    f.write(temp + '\t' + '方式' + '\n')
                else:
                    continue
    # 方式2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/方式', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '方式' + '\n')
                else:
                    continue


'''
流程
'''


def process():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['流程']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    # 流程1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/流程', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '流程' + '\n')
                else:
                    continue


'''
原因
'''


def reason():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['怎么']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['不']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['为什么']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    temp_4 = dict_data['原因']
    temp_4_1 = temp_4.split('\t')
    temp_4_1.remove('')

    # 原因1
    for j in temp_1_1:
        for k in temp_2_1:
            for i in word:
                with open('./intention_result/原因', 'a', encoding='utf-8')as f:
                    temp = i.strip('\n')
                    if re.match('(.*)' + j + '(.*)' + k + '(.*)', temp):
                        f.write(temp + '\t' + '原因' + '\n')
                    else:
                        continue
    # 原因2
    for l in temp_3_1:
        for i in word:
            with open('./intention_result/原因', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + l + '(.*)', temp):
                    f.write(temp + '\t' + '原因' + '\n')
                else:
                    continue
    # 原因3
    for m in temp_4_1:
        for i in word:
            with open('./intention_result/原因', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + m + '(.*)', temp):
                    f.write(temp + '\t' + '原因' + '\n')
                else:
                    continue


'''
推荐
'''


def recommend():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['推荐']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    # 推荐1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/推荐', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '推荐' + '\n')
                elif re.match('(.*)值得(.*)v(.*)', temp):
                    f.write(temp + '\t' + '推荐' + '\n')
                else:
                    continue


'''
关系
'''


def relation():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['关系']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    # 关系1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/关系', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '关系' + '\n')
                else:
                    continue


'''
时间
'''


def time():
    word = load_data('./origin_data/data.txt')
    dict_data = load_build_dict('./origin_data/intention_dict_data')

    temp_1 = dict_data['多久']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['时间']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['几点']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    # 时间1
    for j in temp_1_1:
        for i in word:
            with open('./intention_result/时间', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + j + '(.*)', temp):
                    f.write(temp + '\t' + '时间' + '\n')
                else:
                    continue
    # 时间2
    for k in temp_2_1:
        for i in word:
            with open('./intention_result/时间', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + k + '(.*)', temp):
                    f.write(temp + '\t' + '时间' + '\n')
                else:
                    continue
    # 时间3
    for l in temp_3_1:
        for i in word:
            with open('./intention_result/时间', 'a', encoding='utf-8')as f:
                temp = i.strip('\n')
                if re.match('(.*)' + l + '(.*)', temp):
                    f.write(temp + '\t' + '时间' + '\n')
                else:
                    continue


if __name__ == '__main__':
    amount()
    character()
    condition()
    confirm()
    content()
    definition()
    degree()
    evalution()
    greeting()
    location()
    method()
    process()
    reason()
    recommend()
    relation()
    time()

