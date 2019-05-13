# coding: utf-8

import os

"""
文件读取操作
"""


class GetFileContent:

    @staticmethod
    def GetName(path):
        """
        得到指定路径下文件名
        :param path: 文件路径
        :return:包含文件名字的列表
        """
        temp = []
        for files in os.listdir(path):
            temp.append(files)
        return temp

    @staticmethod
    def GetData(path):
        """
        加载数据
        :param path: 文件路径
        :return: 文件的列表
        """
        with open(path, 'r', encoding='utf-8')as f:
            contentList = f.readlines()
        return contentList
