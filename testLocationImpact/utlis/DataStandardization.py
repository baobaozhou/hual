'''
中文符号转英文
'''
import unicodedata


def TranslateDefine(dataString):
    table = {ord(f): ord(dataString) for f, dataString in zip(
        u'，。！？【】（）％＃＠＆１２３４５６７８９０',
        u',.!?[]()%#@&1234567890')}
    t = dataString.translate(table)
    return t


def TranslateKc(dataString):
    # C、D、KC、KD
    t = unicodedata.normalize('NFKC', dataString)
    return t
