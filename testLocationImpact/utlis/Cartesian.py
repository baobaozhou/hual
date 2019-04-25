# coding: utf-8

"""
笛卡尔积算法实现
"""


class Cartesian:
    def __init__(self, dataGroup):
        """
        初始化
        :param dataGroup:
        """
        self.dataGroup = dataGroup
        # 二维数组从后往前下标值
        self.counterIndex = len(dataGroup) - 1
        # 每次输出数组数值的下标值数组(初始化为0)
        self.counter = [0 for i in range(0, len(self.dataGroup))]

    def CountLength(self):
        """
        计算数组长度
        :return:
        """
        i = 0
        length = 1
        while i < len(self.dataGroup):
            length *= len(self.dataGroup[i])
            i += 1
        return length

    def Handle(self):
        """
        递归处理输出下标
        """
        # 定位输出下标数组开始从最后一位递增
        self.counter[self.counterIndex] += 1
        # 判断定位数组最后一位是否超过长度，超过长度，第一次最后一位已遍历结束
        if self.counter[self.counterIndex] >= len(self.dataGroup[self.counterIndex]):
            # 重置末位下标
            self.counter[self.counterIndex] = 0
            # 标记counter中前一位
            self.counterIndex -= 1
            # 当标记位大于等于0，递归调用
            if self.counterIndex >= 0:
                self.Handle()
            # 重置标记
            self.counterIndex = len(self.dataGroup) - 1

    def Assemble(self):
        """
        排列组合输出
        """
        resultList = []
        length = self.CountLength()
        i = 0
        while i < length:
            attrList = []
            j = 0
            while j < len(self.dataGroup):
                attrList.append(self.dataGroup[j][self.counter[j]])
                j += 1
            temp = '\t'.join(attrList)
            resultList.append(temp)
            self.Handle()
            i += 1
        return resultList
