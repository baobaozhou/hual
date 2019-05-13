# coding: utf-8

"""
加载词典
"""


class LoadDict:

    @staticmethod
    def LoadBuildDictContainKey(path):
        """
        加载词典包含key
        :param path: 字典路径，字典键值对以空格分隔开
        :return: 字典
        """
        dictionary = {}
        with open(path, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                string = ''
                temp = line.strip('\n')
                splitData = temp.split(' ')
                for i in splitData:
                    string += i + '\t'
                    dictionary.update({splitData[0]: string})
        return dictionary

    @staticmethod
    def LoadBuildDictNokey(path):
        """
        加载词典不包含key
        :param path: 字典路径，字典键值对以空格分隔开
        :return: 字典
        """
        dictionary = {}
        with open(path, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                string = ''
                temp = line.strip('\n')
                splitData = temp.split(' ')
                for i in splitData:
                    if splitData.index(i) != 0:
                        string += i + '\t'
                        dictionary.update({splitData[0]: string})
        return dictionary

    @staticmethod
    def LoadBuildDictEveryWords(path):
        """
        加载词典每个value均作为key
        :param path: 字典路径，字典键值对以空格分隔开
        :return: 字典
        """
        dictionary = {}
        with open(path, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                temp = line.strip('\n')
                splitData = temp.split(' ')
                # 每个词都作为key
                length = len(splitData)
                for j in range(length):
                    string = ''
                    for i in splitData:
                        if splitData.index(i) != j:
                            string += i + '\t'
                            dictionary.update({splitData[j]: string})
                        else:
                            continue
        return dictionary
