import jieba


def JieBaRe(stringData):
    t = jieba.cut(stringData)
    temp = ' '.join(t)
    return temp
