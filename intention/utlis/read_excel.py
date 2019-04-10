import xlrd

'''
保存列
'''


def save_cols(data_path, table_number, cols_number, save_path):
    workbook = xlrd.open_workbook(data_path)
    table = workbook.sheets()[table_number]
    nrows = table.nrows
    with open(save_path, 'a', encoding='utf-8')as f:
        for i in range(nrows):
            temp = table.row_values(i)
            f.write(temp[cols_number] + '\n')


'''
保存列
'''


def save_cols_2(data_path, table_number, cn1, cn2, cn3, save_path):
    workbook = xlrd.open_workbook(data_path)
    table = workbook.sheets()[table_number]
    nrows = table.nrows
    with open(save_path, 'a', encoding='utf-8')as f:
        for i in range(nrows):
            temp = table.row_values(i)
            f.write(temp[cn1] + '\t' + temp[cn2] + '\t' + temp[cn3] + '\n')


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
