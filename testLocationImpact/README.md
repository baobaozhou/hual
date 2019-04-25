1. data
<1> 原始语料
dir originalData  
--- data
--- rule
<2> 处理语料
dir generatioanData
--- dicarData
--- jieBaData
--- splitData
<3> 结果
dir resultData
--- osTestResult
--- testJieBaResult

2.script

<1> 数据清理
python PreData.py
<2> 线上测试
python OsTest.py
<3> 线下测试
python TestLocationImpact.py 

3.require
python >= 3.6.0
