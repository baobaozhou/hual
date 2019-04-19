import requests
import re
from utlis.load_file import *
from utlis.sort_out import *

url = 'http://115.182.62.171:2781/bot/training_assistant_jtzf_full/simulator/nlu'
header = {
    'Authorization': 'eyJ0eXBlIjoiand0IiwiYWxnIjoiSFM1MTIifQ.eyJsYXN0TG9naW5UaW1lIjoiMjAxOS0wNC0xNiAxODoyMDoxNiIsInJvbGUiOnsibmFtZSI6InNlbmlvciIsImlkIjozfSwibmlja05hbWUiOiLlkajkvJrlhagiLCJwZXJtaXNzaW9ucyI6WyJjb3JwdXMiLCJib3QiLCJmYXEiLCJpbnRlbnQiLCJkYXRhIiwiZGlhbG9nIiwibW9yZSJdLCJleHBUaW1lIjoiMjAxOS0wNC0xOCAxOTowNzo1NSIsIm5hbWUiOiJodWlxdWFuIiwiaWQiOjYxLCJpc0FkbWluaXN0cmF0b3IiOmZhbHNlLCJsYXN0TG9naW5JUCI6IjE2Ni4xMTEuMTM4Ljg3In0._NPJH2xEg75clAPcjDBgqEDs1Io_BiGTcCc0xLGy9o3b8oDKGdBr_iCaDtGFEsXnM60LLbaOqy9h_PwfjnRtKw',
    'Content-Type': "application/json"}
data_list = load_data('splitdata')
with open('ostestresult', 'a', encoding='utf-8')as f:
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
