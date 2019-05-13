# coding: utf-8
import time

from utlis.GetFileContent import *
from utlis.SortOut import *

import re


def MatchRule(matchData, dicarPath):
    """
    匹配模板并返回结果
    :param dicarPath:
    :param matchData: query
    """
    matchResult = []
    dataList = GetFileContent.GetData(dicarPath)
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
            string = matchData + '\t' + regexSplit[0]
            matchResult.append(string)
        else:
            count += 1
    if count == dataLength:
        string = matchData + '\t' + 'no'
        matchResult.append(string)
    return matchResult


def RegexDict(regexList, length):
    """
    将关键词存为字典
    :param regexList:
    :param length:
    :return:
    """
    regexDict = dict()
    for i in range(1, length):
        if regexList[i] in regexDict:
            regexDict[regexList[i]] += 1
        else:
            regexDict[regexList[i]] = 1
    return regexDict


if __name__ == '__main__':
    sortResult = []
    # data = ['我 只 需要 {{时间段}} 向 您 做 个 简单 的 介绍']
    data = GetFileContent.GetData('generationData/jieBaData')
    for n in data:
        temp = n.strip('\n')
        testResult = MatchRule(temp, 'generationData/dicarRule')
        result = SortOut.SortOut(testResult)
        for j in result:
            sortResult.append(j)
    with open('resultData/testResult', 'a', encoding='utf-8')as f:
        for o in data:
            tempStrip = o.strip('\n')
            tempString = ''
            for m in sortResult:
                tempSplit = m.split('\t')
                if tempSplit[0] == tempStrip:
                    tempString += tempSplit[1] + ' '
            f.write(tempStrip + '\t' + tempString + '\n')
