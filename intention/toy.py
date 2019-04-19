import collections
import re
from utlis.load_file import *

t = load_data('rule')

with open('data', 'a', encoding='utf-8')as f:
    for i in t:
        temp = []
        t1 = re.findall('(?<=\\[)[^\\]]+', i)
        for j in t1:
            temp.append(j)
        if temp.count('v') == 2:
            t2 = re.sub('v', '*', i, data)
            t3 = t2.replace('v', 'v2')
            t4 = t3.replace('*', 'v1')
            if temp.count('n') == 2:
                t5 = re.sub('n', '*', t4, data)
                t6 = t5.replace('n', 'n2')
                t7 = t6.replace('*', 'n1')
                f.write(t7)
            else:
                f.write(t4)
        elif temp.count('v') == 3:
            t2 = re.sub('v', '*', i, data)
            t3 = re.sub('v', '**', i, data)
            t4 = t2.replace('v', 'v3')
            t5 = t4.replace('*', 'v1').replace('**', 'v2')
            if temp.count('n') == 2:
                t6 = re.sub('n', '*', t4, data)
                t7 = t6.replace('n', 'n2')
                t8 = t7.replace('*', 'n1')
                f.write(t8)
            else:
                f.write(t5)
        else:
            if temp.count('n') == 2:
                t1 = re.sub('n', '*', i, data)
                t2 = t1.replace('n', 'n2')
                t3 = t2.replace('*', 'n1')
                f.write(t3)
            else:
                f.write