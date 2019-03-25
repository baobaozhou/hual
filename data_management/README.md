### 0. 特殊说明
#### 1) 保留task
1) task_id:2 此task存放泰行销知识点(所有语料都有正确答案，泰康给的原始标注语料或经过二次处理有正确答案的语料)
2) task_id:5 此task存放所有已处理过的badcase
3) task_id:6 待确认case
### 1. 主程序 run.py
#### 1) 导入
>#### a. 命令行使用
```
python run.py --op import -b bot_name -c /path/to/corpus [-m mod1[,mod2,...]] --desc_id Domain.taskNum.batchNum
```
根据Domain不同会将数据存放在不同表中，即分表，以此在一定程度上应对未来数据量增大的情况 

注意: 若不指定-m选项,则会把-c指定的语料的原始标注信息入库   
>>例如:
```
python run.py --op import -b taikang_952 -c input/test.xlsx -m entity,intent --desc_id taixingxiao.1.1
```
标注数据会存放在tbl_tag_xiaoxingxiao 这张表中
>#### b. databroker_module (上述-m选项指定的内容)

>>I. 根据需求，需要在databroker/databroker_module下编写tag的数据提取处理模块（.py文件，从http_response的msg字段中提取出tag）

>>II. module_file: tag_name.py（要求： 模块的文件名、类名与tag的名称完全一致），如下:

```
# encoding: utf-8
from . import abstract

class tag_name(abstract.abstract):
    def process(self,msg):
        # param msg: http://{host}:{port}/bot/{bot}/simulator接口返回的http_response中msg字段，其中包含了所有返回信息，解析tag都是基于此数据来完成的

        annotations = ""
        # 从msg提取annotations的过程

        # 返回 self.__class__.__name__ 和 annotations  
        # 这要求了类名必须与tag名相同
        return self.__class__.__name__,annotations
```
>>例如: module_file: entity.py
```
# encoding: utf-8
from . import abstract

class entity(abstract.abstract):
    def process(self,msg):
        nluResult = msg["nluResult"]
        chosenMatcher = nluResult["chosenMatcher"]
        currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
        slots = currentMatcher[0]["slots"]
        annotations = ""
        for key in slots:
            if (key == "人寿保险_产品"):
                NLU_Entities = []
                list = slots[key]
                for list_item in list:
                    NLU_Entities.append(list_item["matched"])
                    NLU_Entities_realStart = list_item["realStart"]
                    NLU_Entities_realEnd = list_item["realEnd"]
                    annotations = "[{\"from\":" + str(int(NLU_Entities_realStart)) + ",\"to\":" + str(int(NLU_Entities_realEnd)) + ",\"category\":\"dict\",\"type\":\"人寿保险_产品\",\"value\":\"" + NLU_Entities[0] + "\"}]"
        return self.__class__.__name__,annotations
```
#### 2) 导出
>#### a. 命令行使用
```
python run.py --op export --filter SQL_statement -o /path/to/output_dir --dup 1|0
```
--dup: 导出时是否允许重复，0:否 1或其它:是
>>例如:
```
python run.py --op export --filter "select * from tbl_tag where desc_id = \"task01_batch01\" and corpus_id = 2;" -o output/ --dup 0
```

#### 3) 添加任务
>#### 命令行使用
```
python run.py --op newtask --description "description_info"
```

>>例如:
```
python run.py --op newtask --description "taikang_txx_all badcase 0924-1014"
```

#### 4) 添加批次
一个任务可以通过多批处理来完成。
>#### 命令行使用
```
python run.py --op newbatch --batch_id batch_id --task_id task_id --description "description_info"
```
--batch_id: batch_id

--task_id: 当前批次隶属的task的id

--description: 描述信息

>>例如:
```
python run.py --op newbatch --batch_id "1" --task_id "1" --description "first"
```
#### 5) 跑批量并直接导出(不入库)
>#### a. 命令行使用
```
python run.py --op batchprocessing -b bot_name -c /path/to/corpus [-m mod1[,mod2,...]] -o /path/to/output_dir
```

注意: 若不指定-m选项,则会把-c指定的语料的原始标注导出  
>>例如:
```
python run.py --op batchprocessing -b taikang_952 -c input/test.xlsx -m entity,intent -o output/
```