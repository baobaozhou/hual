# coding: utf-8

from utlis.GetFileContent import *
from utlis.SortOut import *

import requests
import re

url = 'http://115.182.62.171:2781/bot/training_assistant_jtzf_full/simulator/nlu'
header = {
    'Authorization': 'eyJ0eXBlIjoiand0IiwiYWxnIjoiSFM1MTIifQ.eyJsYXN0TG9naW5UaW1lIjoiMjAxOS0wNC0yNCAxNDozMDo1OCIsInJvbGUiOnsibmFtZSI6InNlbmlvciIsImlkIjozfSwibmlja05hbWUiOiLlkajkvJrlhagiLCJwZXJtaXNzaW9ucyI6WyJjb3JwdXMiLCJib3QiLCJmYXEiLCJpbnRlbnQiLCJkYXRhIiwiZGlhbG9nIiwibW9yZSJdLCJleHBUaW1lIjoiMjAxOS0wNC0yNCAxOTozMDoyMyIsIm5hbWUiOiJodWlxdWFuIiwiaWQiOjYxLCJpc0FkbWluaXN0cmF0b3IiOmZhbHNlLCJsYXN0TG9naW5JUCI6IjE2Ni4xMTEuMTM4Ljg3In0.6ecGRO9jjLZUMYJeGLJO1xN_UbUEGmm9IaSr73hAn0diy0Qomg7-mnrvUFLq-dxLxiUxgJ5sd-6zA7_2567qEw',
    'Content-Type': "application/json"}

dataList = GetFileContent.GetData('generationData/splitData')

with open('resultData/osTestResult', 'a', encoding='utf-8')as f:
    for j in dataList:
        tempList = []
        temp = j.strip('\n')
        postData = temp.encode('utf-8')
        r = requests.post(url=url, data=postData, headers=header)
        t = re.findall('"key":"(.*?)"', r.text)
        for i in t:
            tempList.append(i)
        tempSort = SortOut.SortOut(tempList)
        string = '\t'.join(tempSort)
        f.write(temp + '\t' + string + '\n')
