# coding: utf-8

"""
去重并排序
"""


class SortOut:

    @staticmethod
    def SortOut(tempList):
        """
        去重并按照原先的List排序
        :param tempList:
        :return:
        """
        temp = list(set(tempList))
        temp.sort(key=tempList.index)
        return temp
