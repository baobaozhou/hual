import re

'''
加载模板
'''


def tag_model(path_1, path_2):
    with open(path_1, 'r', encoding='utf-8')as f:
        for line in f.readlines():
            # patten = re.compile('')
            temp_3 = line.split('\t')
            with open(path_2, 'a', encoding='utf-8')as f:
                if re.match(r'(.*)ComplexProperty(.*)datatype', temp_3[3]):
                    temp = line.replace('{{ComplexProperty}}', '<ComplexProperty>').replace('{{datatype}}',
                                                                                            '<datatype>')
                    f.write('cd' + '\t' + temp)
                elif re.match(r'(.*)ComplexProperty', temp_3[3]):
                    temp_1 = line.replace('{{ComplexProperty}}', '<ComplexProperty>')
                    f.write('c' + '\t' + temp_1)
                elif re.match(r'(.*)datatype', temp_3[3]):
                    temp_2 = line.replace('{{datatype}}', '<datatype>')
                    f.write('d' + '\t' + temp_2)
                else:
                    f.write('bl' + '\t' + line)
