#将grammer打上cd，c，d,bl等标签
python sparql.py
输入： grammar
输出： tag_model example: cd	INTENT_REGEX	sys.knowledge_query	1.0	{{人事}}<ComplexProperty>的<datatype>
输出： dict_cpdp 合法属性值

#将grammar的合法值还回
python template_match.py
输入： grammar
输入： bulid_dictionary.py  (同义词字典，cpdp字典)
输出： match_cpdp
输出： match_vocab

#生成grammar上传平台测试
python test.py
