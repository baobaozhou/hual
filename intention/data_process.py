from utlis.read_excel import *
from utlis.load_file import *
from utlis.sort_out import *
from utlis.clean_template import *


temp = save_cols('./origin_data/data.xlsx', 0, 1, './origin_data/temp_data')
clean_template('./origin_data/temp_data', './generate_result/temp_data')
query_temp = save_data('./origin_data/data.xlsx', 0, './origin_data/query_temp')

temp_1 = load_data('./origin_data/temp_data')
zhou =[]

for i in temp_1:
    zhou.append(i)
hui = sort_out(zhou)

with open('./origin_data/temp', 'a', encoding='utf-8')as f:
    for j in hui:
        f.write(j)

