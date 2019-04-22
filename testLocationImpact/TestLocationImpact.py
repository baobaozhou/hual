import re
import os
from utlis.load_file import *
from utlis.sort_out import *


def MatchRule(matchData):
    with open('resultData/testdata', 'a', encoding='utf-8')as f:
        data = load_data('generationData/dicaerRule')
        tag1 = 0
        sum = 0
        for i in data:
            t = i.strip('\n').split('\t')
            tag = 0
            for j in t:
                if t.index(j) == 0:
                    continue
                else:
                    if re.search(j, matchData):
                        tag += 1
                    else:
                        continue
            if tag == len(t) - 1:
                sum = 1
                string = matchData + '\t' + t[0] + '\n'
                f.write(string)
            tag1 += 1
            if tag1 == len(data) and sum == 0:
                string = matchData + '\t' + 'no' + '\n'
                f.write(string)


if __name__ == '__main__':
    t = load_data('generationData/jiebadata')
    for i in t:
        temp = i.strip('\n')
        MatchRule(temp)
    t2 = load_data('resultData/testdata')
    t3 = sort_out(t2)
    with open('resultData/testjiebaresult', 'a', encoding='utf-8')as f:
        for j in t3:
            f.write(j)
    os.remove('resultData/testdata')
