一  意图预测    
#用来处理原始语料
python data_process.py
输入： data.xlsx
输出： temp example: [r][v][怎么][v][n] 去重过前项
输出： query_temp example: 这是怎么回事儿 [r][v][怎么][v][n] 包含全部的问题
输出： temp_data 未去重的前项
输出： temp_data 位于template_data目录下的，去除不必要词性的前项 example： [v][怎么][v][n] 去掉了[r]

#得到意图分类的结果
python classifier_intention.py
输入： temp
输入： query_temp 部分意图需要匹配原query
输出： intention_result 包含预测的所有意图 example: 关系 {{entity}}[如何][关联][v][a]

#展示意图分类结果
python run.py
输入： query_temp
输入： intention_result
输出： result_data example: 高血脂能买保险吗 {{entity}}[能][v][n] 确认


二  预测合法属性
#提取标注规则
python extraction_annotation_rule.py
输入： test.xlsx
输出： annotation_rule example: [n][p:在][哪里][能][v] cp=v,dp=位置
输出： pre_property_data example: 我的业绩哪里找 [业绩=n, 哪里=r, 找=v] [n][p:在][哪里][v]

#预测合法属性
python predicting_properties.py
输入： annotation_rule
输入： pre_property_data
输出： predict_result example: 我的业绩哪里找	[业绩=n, 哪里=r, 找=v]	[n][p:在][哪里][v]	cp=找	dp=位置


三  后项转换
#将匹配到的后项输出出来
python match_template.py
输入： template_dict example： 怎么 怎样 怎么样 咋 怎 如何 不同于characteristic_word，只要同义就可
输入： template_library
输出： match_template example: [n][n][什么][意思] [n][n][什么][定义]

#characteristic_word
此目录保存了能用于分类意图的关键字

#template_library
此目录保存了不同意图的前项
