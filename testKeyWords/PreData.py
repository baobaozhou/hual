# coding: utf-8

from utlis.GetFileContent import *
from utlis.JieBaResult import *
from utlis.Cartesian import *
from utlis.DataStandardization import *
from utlis.SortOut import *

import re

"""
数据清理
"""


class PreData:

    @staticmethod
    def SplitData(originDataPath, splitDataPath):
        """
        以最小单位','切割语句
        :param originDataPath: 原始语料的路径
        :param splitDataPath:  切割结果的路径
        """
        data = GetFileContent.GetData(originDataPath)
        tempList = []
        for i in data:
            temp = i.strip('\n')
            tempStandardization = DataStandardization.TranslateDefine(temp)
            tempSplit = re.split(r',|\?|\!|\.', tempStandardization)
            for k in tempSplit:
                if k == '':
                    continue
                else:
                    tempList.append(k)
        sortList = SortOut.SortOut(tempList)
        with open(splitDataPath, 'a', encoding='utf-8')as f:
            for l in sortList:
                f.write(l + '\n')

    @staticmethod
    def JieBaData(originDataPath, jieBaDataPath, jieBaDictPath):
        """
        语句分词
        :param jieBaDictPath:  分词词典
        :param originDataPath: 原始预料路径
        :param jieBaDataPath:  分词结果路径
        """
        data = GetFileContent.GetData(originDataPath)
        with open(jieBaDataPath, 'a', encoding='utf-8')as f:
            for i in data:
                temp = i.strip('\n')
                tempJieBa = JieBaResult.JieBaResult(temp, jieBaDictPath)
                f.write(tempJieBa + '\n')

    @staticmethod
    def DicarData(originDataPath, dicarDataPath):
        """
        生成正则对应的笛卡尔积
        :param originDataPath: 原始预料路径
        :param dicarDataPath:  笛卡尔积路径
        """
        data = GetFileContent.GetData(originDataPath)
        for i in data:
            temp = []
            t1 = i.strip('\n').split('\t')
            t2 = re.findall('(?<=\\()[^\\)]+', t1[3])
            length = len(t2)
            for j in range(length):
                t3 = t2[j].split('|')
                temp.append(t3)
            tag = t1[1].replace('replace=', '')
            cartesian = Cartesian(temp)
            dicarList = cartesian.Assemble()
            with open(dicarDataPath, 'a', encoding='utf-8')as f:
                for k in dicarList:
                    f.write(tag + '\t' + k + '\n')


if __name__ == '__main__':
    PreData.SplitData('originalData/data', 'generationData/splitData')
    # python Ner.py
    PreData.JieBaData('generationData/nerData', 'generationData/jieBaData', 'originalData/jieBaDict')
    PreData.DicarData('originalData/rule', 'generationData/dicarRule')
