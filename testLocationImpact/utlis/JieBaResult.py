# coding: utf-8

import jieba

"""
分词操作，更多用法详见 https://www.jianshu.com/p/e8b5d01ca073
"""


class JieBaResult:

    @staticmethod
    def JieBaResult(stringData, jieaBaDict):
        """
        使用默认模式对字符串分词
        :param stringData: 待分词的字符串
        :param jieaBaDict: 分词词典
        :return: 分词后的字符串
        """
        jieba.load_userdict(jieaBaDict)
        t = jieba.cut(stringData)
        splitData = ' '.join(t)
        return splitData
