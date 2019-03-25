from utlis.get_text_name import get_name
from utlis.load_dictionary import load_vocab_data

'''
构造其他类字典
'''


def bulid_cpdp_dict():
    temp_list = get_name('./dict_cpdp')
    result_dict = {}
    for i in temp_list:
        tag = ''
        tag_1 = ''
        tag_2 = ''
        dict = {}
        with open('./dict_cpdp/' + i, 'r', encoding='utf-8')as f:
            for line in f.readlines():
                tmp = line.split('\t')
                if tmp[0] == 'd':
                    tag_2 += tmp[2].strip('\n') + '\t'
                    dict = {'d': tag_2}
                elif tmp[0] == 'cd':
                    tag += tmp[1] + ',' + tmp[2].strip('\n') + '\t'
                    dict['cd'] = tag
                # 没有c的
                # elif tmp[0] == 'c':
                #     tag_1 += tmp[2].strip('\n') + '\t'
                #     dict['c'] = tag_1
            result_dict.update({i: dict})

    return result_dict


'''
构造词表字典
'''


def bulid_vocab_dict():
    load_vocab_data('./origin_data/synonymyTable.txt', './deal_data/dict_vocab')
    dict = {}
    with open('./deal_data/dict_vocab', 'r', encoding='utf-8')as f:
        for line in f.readlines():
            tmp = line.split('\t')
            tmp_1 = tmp[1].strip('\n')
            dict.update({tmp[0]: tmp_1})
        return dict


if __name__ == '__main__':
    print(bulid_cpdp_dict())
    print(bulid_vocab_dict())
