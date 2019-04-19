# import requests
#
# postdata = {'query': '张先生？'}
#
# url = 'http://115.182.62.171:2781/bot/training_assistant_jtzf_full/simulator/nlu'
# header = {'Authorization': 'eyJ0eXBlIjoiand0IiwiYWxnIjoiSFM1MTIifQ.eyJsYXN0TG9naW5UaW1lIjoiMjAxOS0wNC0xMSAwOToyMjoxNyIsInJvbGUiOnsibmFtZSI6InNlbmlvciIsImlkIjozfSwibmlja05hbWUiOiLlkajkvJrlhagiLCJwZXJtaXNzaW9ucyI6WyJjb3JwdXMiLCJib3QiLCJmYXEiLCJpbnRlbnQiLCJkYXRhIiwiZGlhbG9nIiwibW9yZSJdLCJleHBUaW1lIjoiMjAxOS0wNC0xMSAxNjoyMzowMiIsIm5hbWUiOiJodWlxdWFuIiwiaWQiOjYxLCJpc0FkbWluaXN0cmF0b3IiOmZhbHNlLCJsYXN0TG9naW5JUCI6IjE2Ni4xMTEuMTM4Ljg3In0.QW-Egm5HBhvE2DlJQDvOMKIQhsDP-Yh_t76J6Q5VSa6fCDluCyjKUzxb6BUk3rlZSy8hXmld4K_mApmOAPvC7w'}
# r = requests.post(url=url, data=postdata, headers=header)
#
# print(r.text.encode('utf-8'))


import collections
import re
from utlis.load_file import *

t = load_data('data')

for i in t:
    temp = []
    t1 = re.findall('(?<=\\[)[^\\]]+', i)
    for j in t1:
        temp.append(j)
    if temp.count('v') == 2:
        t2 = re.sub('v', '*', i, 1)
        t3 = t2.replace('v', 'v2')
        t4 = t3.replace('*', 'v1')
        if temp.count('n') == 2:
            t5 = re.sub('n', '*', t4, 1)
            t6 = t5.replace('n', 'n2')
            t7 = t6.replace('*', 'n1')
            print(t7)
        else:
            print(t4)
    elif temp.count('v') == 3:
        t2 = re.sub('v', '*', i, 1)
        t3 = re.sub('v', '**', i, 1)
        t4 = t2.replace('v', 'v3')
        t5 = t4.replace('*', 'v1').replace('**', 'v2')
        if temp.count('n') == 2:
            t6 = re.sub('n', '*', t4, 1)
            t7 = t6.replace('n', 'n2')
            t8 = t7.replace('*', 'n1')
            print(t8)
        else:
            print(t5)
    else:
        if temp.count('n') == 2:
            t1 = re.sub('n', '*', i, 1)
            t2 = t1.replace('n', 'n2')
            t3 = t2.replace('*', 'n1')
            print(t3)
        else:
            print(i)



