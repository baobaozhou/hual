#处理语料
输入： 原始语料
dir originalData  
--- data 原问题
--- rule 正则
--- jieBaDict 分词字典
输出： 处理语料
dir generatioanData
--- dicarData
--- jieBaData
--- splitData
--- nerData
#线上测试
python OsTest.py
输入： splitData
输出： osResult

#线下测试
python TestLocationImpact.py 批量输出
输入： jieBaData
输入： dicarRule
输出： testResult
python ./test/function.py 单条测试 

#require
python >= 3.6.0
