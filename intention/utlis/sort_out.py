'''
去重并排序
'''


def sort_out(temp_list):
    temp = list(set(temp_list))
    temp.sort(key=temp_list.index)
    return temp
