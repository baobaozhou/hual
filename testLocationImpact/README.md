# 1.data

dir originalData
--- data #query  --- rule #regex

dir generatioanData 
--- dicarData #expandRegex --- jieBaData --- splitData

dir resultData --- osTestResult --- testJieBaResult

# 2.script

<1> 数据清理

python PreData.py

<2> 线上测试

python OsTest.py

<3> 线下测试

python TestLocationImpact.py 

3.requirement

python >= 3.6.0
