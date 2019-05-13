# coding: utf-8

import xlrd

"""
Excel格式文件读操作
"""


class LoadExcelFile:

    @staticmethod
    def SaveCols(dataPath, tableNumber, colsNumber, savePath):
        """
        保存Excel文件的某一行
        :param dataPath: Excel文件路径
        :param tableNumber: sheet页
        :param colsNumber: 第几行
        :param savePath: 保存路径
        """
        workbook = xlrd.open_workbook(dataPath)
        table = workbook.sheets()[tableNumber]
        nrows = table.nrows
        with open(savePath, 'a', encoding='utf-8')as f:
            for i in range(nrows):
                temp = table.row_values(i)
                f.write(temp[colsNumber] + '\n')

    @staticmethod
    def SaveData(dataPath, tableNumber, savePath):
        """
        保存sheet页的内容
        :param dataPath:
        :param tableNumber:
        :param savePath:
        """
        workbook = xlrd.open_workbook(dataPath)
        table = workbook.sheets()[tableNumber]
        nrows = table.nrows
        with open(savePath, 'a', encoding='utf-8')as f:
            for i in range(nrows):
                temp = table.row_values(i)
                temp_1 = '\t'.join(temp)
                f.write(temp_1 + '\n')
