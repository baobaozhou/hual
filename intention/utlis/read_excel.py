import xlrd
from utlis.sort_out import *
'''
保存列
'''


def save_cols(data_path, table_number, cols_number, save_path):
    workbook = xlrd.open_workbook(data_path)
    table = workbook.sheets()[table_number]
    nrows = table.nrows
    zhou = []
    with open(save_path, 'a', encoding='utf-8')as f:
        for i in range(nrows):
            temp = table.row_values(i)
            zhou.append(temp[cols_number])
        hui = sort_out(zhou)
        for j in hui:
            f.write(j + '\n')


'''
保存行
'''


def save_data(data_path, table_number, save_path):
    workbook = xlrd.open_workbook(data_path)
    table = workbook.sheets()[table_number]
    nrows = table.nrows
    ncols = table.ncols
    with open(save_path, 'a', encoding='utf-8')as f:
        for i in range(nrows):
            temp = table.row_values(i)
            temp_1 = '\t'.join(temp)
            f.write(temp_1 + '\n')
