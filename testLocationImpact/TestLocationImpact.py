# coding: utf-8

from utlis.GetFileContent import *

import re


def MatchRule(matchData):
    """
    匹配模板并返回结果
    :param matchData: query
    """
    with open('resultData/testJieBaResult', 'a', encoding='utf-8')as f:
        dataList = GetFileContent.GetData('generationData/dicarRule')
        dataLength = len(dataList)
        count = 0
        for i in dataList:
            tag = 0
            tempList = i.strip('\n').split('\t')
            length = len(tempList)
            for j in range(1, length):
                if re.search(tempList[j], matchData):
                    tag += 1
                else:
                    continue
            if tag == len(tempList) - 1:
                string = matchData + '\t' + i + '\n'
                f.write(string)
            else:
                count += 1
        if count == dataLength:
            string = matchData + '\t' + 'no' + '\n'
            f.write(string)


if __name__ == '__main__':
    data = GetFileContent.GetData('generationData/jieBaData')
    for k in data:
        temp = k.strip('\n')
        MatchRule(temp)

