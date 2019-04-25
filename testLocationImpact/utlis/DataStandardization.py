# coding: utf-8

import unicodedata

"""
字符标准化处理操作
"""


class DataStandardization:

    @staticmethod
    def TranslateDefine(dataString):
        """
        中文符号转英文
        :param dataString: 待转化的字符串
        :return: 转化的字符串
        """
        table = {ord(f): ord(dataString) for f, dataString in zip(
            u'，。！？【】（）％＃＠＆１２３４５６７８９０',
            u',.!?[]()%#@&1234567890')}
        t = dataString.translate(table)
        return t

    @staticmethod
    def TranslateKc(dataString):
        """
        中文符号转英文
        :param dataString: 待转化的字符串
        :return: 转化的字符串
        """
        # C、D、KC、KD
        t = unicodedata.normalize('NFKC', dataString)
        return t
