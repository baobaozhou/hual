import requests
import re
from utlis.load_file import *
from utlis.sort_out import *

url = 'http://115.182.62.171:2781/bot/training_assistant_jtzf_full/simulator/nlu'
header = {
    'Authorization': 'eyJ0eXBlIjoiand0IiwiYWxnIjoiSFM1MTIifQ.eyJsYXN0TG9naW5UaW1lIjoiMjAxOS0wNC0yMiAwOTozNDozMCIsInJvbGUiOnsibmFtZSI6InNlbmlvciIsImlkIjozfSwibmlja05hbWUiOiLlkajkvJrlhagiLCJwZXJtaXNzaW9ucyI6WyJjb3JwdXMiLCJib3QiLCJmYXEiLCJpbnRlbnQiLCJkYXRhIiwiZGlhbG9nIiwibW9yZSJdLCJleHBUaW1lIjoiMjAxOS0wNC0yMiAxMTozNDozMSIsIm5hbWUiOiJodWlxdWFuIiwiaWQiOjYxLCJpc0FkbWluaXN0cmF0b3IiOmZhbHNlLCJsYXN0TG9naW5JUCI6IjE2Ni4xMTEuMTM4Ljg3In0.ibz9uZwF_Dy7q8XXcV7SaHlz1FaPxRiKWy1fA4ZkwdM21sJOw2XsxOJtf1j4n4QxcGS6l0dTA02GQsa8df-oKw',
    'Content-Type': "application/json"}
data_list = load_data('generationData/splitdata')
with open('resultData/ostestresult', 'a', encoding='utf-8')as f:
    for j in data_list:
        zhou = []
        temp = j.strip('\n')
        postdata = temp.encode('utf-8')
        r = requests.post(url=url, data=postdata, headers=header)
        t = re.findall('"key":"(.*?)"', r.text)
        for i in t:
            zhou.append(i)
        t1 = sort_out(zhou)
        t2 = '\t'.join(t1)
        f.write(temp + '\t' + t2 + '\n')
