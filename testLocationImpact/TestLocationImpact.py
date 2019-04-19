import re
from utlis.load_file import *
from utlis.sort_out import *


def MatchRule(matchData):
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
            return matchData + '\t' + t[0] + '\n'
        tag1 += 1
        if tag1 == len(data) and sum == 0:
            return matchData + '\t' + 'no' + '\n'


if __name__ == '__main__':
    t = load_data('generationData/splitdata')
    with open('resultData/testdata', 'a' ,encoding='utf-8')as f:
        for i in t:
            temp = i.strip('\n')
            t1 = MatchRule(temp)
            f.write(t1)


