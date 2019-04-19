from utlis.load_file import *

t = load_data('resultData/testdata')
with open('1', 'a', encoding='utf-8')as f:
    for i in t:
        t1 = i.split('\t')
        f.write(t1[1])