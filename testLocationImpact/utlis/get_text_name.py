import os

'''
得到指定路径下文件名
'''


def get_name(path):
    temp = []
    for files in os.listdir(path):
        temp.append(files)
    return temp
