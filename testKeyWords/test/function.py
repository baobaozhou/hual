# coding: utf-8

from utlis.GetFileContent import *

import re


def MatchRule(matchData):
    """
    匹配模板并返回结果
    :param matchData: query
    """
    dataList = GetFileContent.GetData('../generationData/dicarRule')
    # dataList = ['是否是时间	{{时间段}}	有']
    dataLength = len(dataList)
    count = 0
    for i in dataList:
        tag = 0
        regexSplit = i.strip('\n').split('\t')
        length = len(regexSplit)
        regexDict = RegexDict(regexSplit, length)
        for k, v in regexDict.items():
            if len(re.findall(k, matchData)) == v and re.match('.*{{' + k + '.*', matchData) is None:
                tag += 1
            else:
                continue
        if tag == len(regexDict):
            print(matchData + '\t' + i)
            # f.write(matchData + '\t' + i)
        else:
            count += 1
    if count == dataLength:
        string = matchData + '\t' + 'no' + '\n'
        print(string)
        # f.write(string)


def RegexDict(regexList, length):
    regexDict = dict()
    for j in range(1, length):
        if regexList[j] in regexDict:
            regexDict[regexList[j]] += 1
        else:
            regexDict[regexList[j]] = 1
    return regexDict


if __name__ == '__main__':
    # data = GetFileContent.GetData('data')
    for i in range(1000):
        if i < 1000:
            test = input()
            MatchRule(test)
    # for l in data:
    #     MatchRule(l.strip('\n'))

