# coding: utf-8
import re
from utlis.load_file import *
from utlis.sort_out import *

'''
数量
'''


def amount():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/数量')

    temp_1 = dict_data['数量']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/数量', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('数量' + '\t' + i)
                else:
                    continue


'''
人物
'''


def character():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/人物')

    temp_1 = dict_data['哪位']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/人物', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('人物' + '\t' + i)
                else:
                    continue


'''
条件
'''


def condition():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/条件')

    temp_1 = dict_data['条件']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['要']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['什么']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    def fun(z):
        for j in temp_1_1:
            if re.match('(.*)' + j + '(.*)', z):
                return 1
            else:
                continue

    def fun_1(h):
        for k in temp_2_1:
            for l in temp_3_1:
                if re.match('(.*)' + k + '(.*)' + l + '(.*)', h):
                    return 1
                else:
                    continue

    with open('./intention_result/条件', 'a', encoding='utf-8')as f:
        for i in word:
            if fun_1(i) == 1:
                f.write('条件内容' + '\t' + i)
            elif fun(i) == 1:
                f.write('条件' + '\t' + i)
            else:
                continue


'''
确认
'''


def confirm():
    word = load_data('./origin_data/temp')
    word_1 = load_data('./origin_data/query_temp')
    dict_data = load_build_dict('./characteristic_word/确认')
    zhou = []

    temp_1 = dict_data['能']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['能否']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['吗']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    for j in temp_1_1:
        for l in temp_3_1:
            for z in word_1:
                h = z.split('\t')
                if re.match('(.*)' + j + '(.*)' + l + '$', h[0]):
                    zhou.append(h[1])
                else:
                    continue

    for k in temp_2_1:
        for i in word:
            if re.match('(.*)' + k + '(.*)', i) or re.match('(.*)v]\\[不]\\[v]$', i):
                zhou.append(i)
            else:
                continue

    hui = sort_out(zhou)

    with open('./intention_result/确认', 'a', encoding='utf-8')as f:
        for o in hui:
            f.write('确认' + '\t' + o)


'''
内容
'''


def content():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/内容')

    temp_1 = dict_data['什么']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['有']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['解释']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    temp_4 = dict_data['内容']
    temp_4_1 = temp_4.split('\t')
    temp_4_1.remove('')

    def fun(z):
        for j in temp_1_1:
            for k in temp_2_1:
                if re.match('(.*)' + k + '(.*)' + j + '(.*)', z):
                    return 1
                else:
                    continue

    def fun_1(h):
        for j in temp_1_1:
            for l in temp_3_1:
                if re.match('(.*)' + l + '(.*)' + j + '(.*)', h):
                    return 1
                else:
                    continue

    def fun_2(o):
        for m in temp_4_1:
            if re.match('(.*)' + m + '(.*)', o):
                return 1
            else:
                continue

    with open('./intention_result/内容', 'a', encoding='utf-8')as f:
        for i in word:
            if fun(i) == 1:
                f.write('内容' + '\t' + i)
            elif fun_1(i) == 1:
                f.write('内容' + '\t' + i)
            elif fun_2(i) == 1:
                f.write('内容' + '\t' + i)
            else:
                continue


'''
定义
'''


def definition():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/定义')

    temp_1 = dict_data['什么']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['定义']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    def fun(z):
        for j in temp_1_1:
            if re.match('(.*)\\[n]\\[是(.*)' + j + '(.*)', z) or re.match('\\[' + j + ']\\[是(.*)', z) or re.match(
                    '(.*)\\{{entity}}\\[是(.*)' + j + '(.*)', z):
                return 1
            else:
                continue

    def fun_1(h):
        for k in temp_2_1:
            if re.match('(.*)' + k + '(.*)', h):
                return 1
            else:
                continue

    with open('./intention_result/定义', 'a', encoding='utf-8')as f:
        for i in word:
            if fun(i) == 1:
                f.write('定义' + '\t' + i)
            elif fun_1(i) == 1:
                f.write('定义' + '\t' + i)
            else:
                continue


'''
程度
'''


def degree():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/程度')

    temp_1 = dict_data['程度']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/程度', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('程度' + '\t' + i)
                else:
                    continue


'''
评价
'''


def evalution():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/评价')

    temp_1 = dict_data['评价']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['如何']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    def fun(z):
        for j in temp_1_1:
            if re.match('(.*)' + j + '(.*)', z):
                return 1
            else:
                continue

    def fun_1(h):
        for k in temp_2_1:
            if re.match('(.*)\\[n]\\[' + k + ']$', h) or re.match('(.*)\\{{entity}}\\[' + k + ']$', h):
                return 1
            else:
                continue

    with open('./intention_result/评价', 'a', encoding='utf-8')as f:
        for i in word:
            if fun_1(i) == 1:
                f.write('评价' + '\t' + i)
            elif fun(i) == 1:
                f.write('评价' + '\t' + i)
            else:
                continue


'''
寒暄
'''


def greeting():
    word_1 = load_data('./origin_data/query_temp')
    dict_data = load_build_dict('./characteristic_word/寒暄')
    zhou = []

    temp_1 = dict_data['你好']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['谢谢']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    for j in temp_1_1:
        for k in temp_2_1:
            for i in word_1:
                h = i.split('\t')
                if re.match(j + '$', h[0]) or re.match(k, h[0]):
                    zhou.append(h[1])
                else:
                    continue

    hui = sort_out(zhou)

    with open('./intention_result/寒暄', 'a', encoding='utf-8')as f:
        for l in hui:
            f.write('寒暄' + '\t' + l)


'''
地点
'''


def location():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/地点')

    temp_1 = dict_data['哪里']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/地点', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('地点' + '\t' + i)
                else:
                    continue


'''
方法
'''


def method():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/方式')

    temp_1 = dict_data['如何']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['方式']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    def fun(z):
        for j in temp_1_1:
            if re.match('(.*)' + j + '(.*)v(.*)', z) or re.match('(.*)' + j + '\\{{entity(.*)', z) or re.match(
                    '(.*)' + j + '\\[n(.*)', z):
                return 1
            else:
                continue

    def fun_1(h):
        for k in temp_2_1:
            if re.match('(.*)' + k + '(.*)', h):
                return 1
            else:
                continue

    def fun_2(o):
        for l in temp_1_1:
            if re.match('(.*)' + l + '(.*)办]$', o):
                return 1
            else:
                continue

    with open('./intention_result/方式', 'a', encoding='utf-8')as f:
        for i in word:
            if fun(i) == 1:
                f.write('方式' + '\t' + i)
            elif fun_1(i) == 1:
                f.write('方式' + '\t' + i)
            elif fun_2(i) == 1:
                f.write('解决方法' + '\t' + i)
            else:
                continue


'''
流程
'''


def process():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/流程')

    temp_1 = dict_data['流程']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/流程', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('流程' + '\t' + i)
                else:
                    continue


'''
原因
'''


def reason():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/原因')

    temp_1 = dict_data['怎']
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

    def fun(z):
        for j in temp_1_1:
            for k in temp_2_1:
                if re.match('(.*)' + j + '(.*)' + k + '(.*)', z):
                    return 1
                else:
                    continue

    def fun_1(h):
        for l in temp_3_1:
            if re.match('(.*)' + l + '(.*)', h):
                return 1
            else:
                continue

    def fun_2(o):
        for m in temp_4_1:
            if re.match('(.*)' + m + '(.*)', o):
                return 1
            else:
                continue

    with open('./intention_result/原因', 'a', encoding='utf-8')as f:
        for i in word:
            if fun(i) == 1:
                f.write('原因' + '\t' + i)
            elif fun_1(i) == 1:
                f.write('原因' + '\t' + i)
            elif fun_2(i) == 1:
                f.write('原因' + '\t' + i)
            else:
                continue


'''
推荐
'''


def recommend():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/推荐')

    temp_1 = dict_data['推荐']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/推荐', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('推荐' + '\t' + i)
                elif re.match('(.*)值(.*)v(.*)', i):
                    f.write('推荐' + '\t' + i)
                else:
                    continue


'''
关系
'''


def relation():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/关系')

    temp_1 = dict_data['关系']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    with open('./intention_result/关系', 'a', encoding='utf-8')as f:
        for j in temp_1_1:
            for i in word:
                if re.match('(.*)' + j + '(.*)', i):
                    f.write('关系' + '\t' + i)
                else:
                    continue


'''
时间
'''


def time():
    word = load_data('./origin_data/temp')
    dict_data = load_build_dict('./characteristic_word/时间')

    temp_1 = dict_data['几天']
    temp_1_1 = temp_1.split('\t')
    temp_1_1.remove('')

    temp_2 = dict_data['多久']
    temp_2_1 = temp_2.split('\t')
    temp_2_1.remove('')

    temp_3 = dict_data['时间']
    temp_3_1 = temp_3.split('\t')
    temp_3_1.remove('')

    def fun(z):
        for j in temp_1_1:
            if re.match('(.*)' + j + '(.*)', z):
                return 1
            else:
                continue

    def fun_1(h):
        for k in temp_2_1:
            if re.match('(.*)' + k + '(.*)', h):
                return 1
            else:
                continue

    def fun_2(o):
        for l in temp_3_1:
            if re.match('(.*)' + l + '(.*)', o):
                return 1
            else:
                continue

    with open('./intention_result/时间', 'a', encoding='utf-8')as f:
        for i in word:
            if fun(i) == 1:
                f.write('时间' + '\t' + i)
            elif fun_1(i) == 1:
                f.write('时间' + '\t' + i)
            elif fun_2(i) == 1:
                f.write('时间' + '\t' + i)
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
