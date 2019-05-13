# coding: utf-8

from utlis.GetFileContent import *

import requests
import re

url = 'http://115.182.62.171:2781/bot/training_assistant_jtzf_full_new/simulator/nlu'
header = {
    'Authorization': 'eyJ0eXBlIjoiand0IiwiYWxnIjoiSFM1MTIifQ.eyJsYXN0TG9naW5UaW1lIjoiMjAxOS0wNS0wOCAxNDo1NzowMCIsInJvbGUiOnsibmFtZSI6InNlbmlvciIsImlkIjozfSwibmlja05hbWUiOiLlkajkvJrlhagiLCJwZXJtaXNzaW9ucyI6WyJjb3JwdXMiLCJib3QiLCJmYXEiLCJpbnRlbnQiLCJkYXRhIiwiZGlhbG9nIiwibW9yZSJdLCJleHBUaW1lIjoiMjAxOS0wNS0wOSAxNzowNTo1NiIsIm5hbWUiOiJodWlxdWFuIiwiaWQiOjYxLCJpc0FkbWluaXN0cmF0b3IiOmZhbHNlLCJsYXN0TG9naW5JUCI6IjE2Ni4xMTEuMTM5LjEwNCJ9.1x4PHAFrQWJ8UxxJG-06NEddST7WpPvIwxnRftUpOgPr6pkBJK8vW1Uz_D8pGZ8bgApXAcUBCXqZtcCpXwGkqQ',
    'Content-Type': "application/json"}

dataList = GetFileContent.GetData('generationData/splitData')

with open('generationData/nerData', 'a', encoding='utf-8')as f:
    for j in dataList:
        tempList = []
        temp = j.strip('\n')
        postData = temp.encode('utf-8')
        r = requests.post(url=url, data=postData, headers=header)
        t = re.findall('"pQuery":"(.*?)"', r.text)
        try:
            f.write(t[0] + '\n')
        except:
            continue
