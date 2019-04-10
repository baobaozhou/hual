import re
def clean_template(data_path, save_path):
    relu = ['t', 's', 'f', 'a', 'b', 'z', 'r', 'm', 'q', 'd', 'p', 'c', 'u', 'e', 'y', 'o', 'h', 'k', 'x', 'w', 'j',
            'l']
    with open(save_path, 'a', encoding='utf-8')as f_1:
        with open('./origin_data/temp_data', 'r', encoding='utf-8')as f:
            for line in f.readlines():
                temp = line.replace('{{entity}}', '[n]').strip('\n')
                temp_1 = re.findall('(?<=\\[)[^\\]]+', temp)
                if all(j not in relu for j in temp_1):
                    f_1.write(temp + '\n')
                else:
                    for j in temp_1:
                        if j in relu:
                            hui = temp.replace('[' + j + ']', '')
                            temp = hui
                        else:
                            continue
                    f_1.write(temp + '\n')
