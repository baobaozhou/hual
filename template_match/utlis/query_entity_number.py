import re

'''
查询所有实体类
'''


def query_entity(path):
    temp_list = []
    with open(path, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            temp = re.findall(u'(?<=\\{{)[^\\}}]+', line)
            for i in temp:
                if re.match(u'[\u4e00-\u9fff]+', i):
                    temp_list.append(i)
        entity_list = list(set(temp_list))
        entity_list.sort(key=temp_list.index)
    return entity_list
