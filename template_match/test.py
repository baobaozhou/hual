list_1 = []
with open('./result_data/match_vocab', 'r', encoding='utf-8')as f:
    for line in f.readlines():
        temp = line.split('\t')
        del temp[0]
        temp_2 = '\t'.join(temp)
        temp_3 = temp_2.replace('<', '[').replace('>', ']')
        list_1.append(temp_3)
list_2 = list(set(list_1))
list_2.sort(key=list_1.index)        
with open('grammar', 'a', encoding='utf-8')as f_1:
    for i in list_2:
        f_1.write(i)
