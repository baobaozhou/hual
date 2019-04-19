from utlis.load_file import *
from utlis.JiebaResult import *
from utlis.Cartesian import *
import re


def SplitData():
    data = load_data('originalData/data')
    with open('generationData/splitdata', 'a', encoding='utf-8')as f:
        for i in data:
            t = i.strip('\n')
            t1 = t.replace(' ', '')
            t2 = t1.split('，')
            for j in t2:
                f.write(j + '\n')


def JiebaData():
    t = load_data('generationData/splitdata')
    with open('generationData/jiebadata', 'a', encoding='utf-8')as f:
        for i in t:
            t1 = i.strip('\n')
            t2 = JieBaRe(t1)
            f.write(t2 + '\n')


def DicaerData():
    t = load_data('originalData/rule')
    for i in t:
        temp = []
        t1 = i.strip('\n').split('\t')
        t2 = re.findall('(?<=\\()[^\\)]+', t1[3])
        length = len(t2)
        for i in range(length):
            t3 = t2[i].split('|')
            temp.append(t3)
        tag = t1[1].replace('replace=', '')
        cartesian = Cartesian(temp)
        cartesian.assemble(tag)



if __name__ == '__main__':
    DicaerData()
