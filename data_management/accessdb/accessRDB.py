# encoding: utf-8
import MySQLdb
import MySQLdb.cursors
import os
import json
import collections
import traceback
from accessdb import access
from log_module import log

class accessRDB(access.access):
    tpl_insert_stmt = """insert into {table} ({attributes}) values ({values});"""

    @classmethod
    def getConfig(cls,filename):
        config = dict()
        with open(filename,'r',encoding="utf-8") as f:
            for line in f.readlines():
                line = line.strip()
                tmp = [ele.strip() for ele in line.split("=")]
                if tmp[1].isdecimal():
                    config[tmp[0]] = int(tmp[1])
                else:
                    config[tmp[0]] = tmp[1]
        config["cursorclass"] = MySQLdb.cursors.DictCursor
        return config

    def __init__(self):
        filename = "config.txt"
        self.configpath = os.path.join(os.path.dirname(__file__),"etc/",filename)
        self.config = self.getConfig(self.configpath)
        self.conn = MySQLdb.connect(**self.config)
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()
    
    def insert(self,**kwargs):
        table = kwargs["table"]
        attributes = []
        values = []
        for key,value in kwargs.items():
            if key == "table":
                continue
            else:
                attributes.append(key)
                values.append("\"{}\"".format(value.replace('"',"'").replace('\r\n','\n').replace('\r','\n')))
        stmt = self.tpl_insert_stmt.format(table=table,attributes=','.join(attributes),values=','.join(values))
        return self.execute(stmt=stmt)
    
    def execute(self,**kwargs):
        log_writter = log.log().getLog()
        log_writter.info(kwargs["stmt"])
        self.cursor.execute(kwargs["stmt"])
        self.conn.commit()
        result = self.cursor.fetchall()
        return result
    
    def importData(self,standard_form):
        fail = []
        flag = True
        data_json = json.loads(standard_form,object_pairs_hook=collections.OrderedDict,encoding="utf-8")
        for i in range(len(data_json)):
            try:
                content_dict = data_json[i]
                # 1. 查找corpus_id 若不存在则插入
                corpus = self.execute(stmt="""select * from {} where query="{}";""".format("tbl_corpus",content_dict["query"].replace("\"","'")))
                if len(corpus) == 0:
                    self.insert(table="tbl_corpus",query=content_dict["query"].replace("\"","'"))
                corpus_id = self.execute(stmt="""select * from {} where query="{}";""".format("tbl_corpus",content_dict["query"].replace("\"","'")))[0]["id"]
                # 2. 插入tags 
                for tag in content_dict["tags"]:
                    result = self.execute(stmt="""select * from {} where key_name="{}";""".format("tbl_key",tag["key"]))
                    if len(result) == 1:
                        key_id = result[0]["id"]
                    else:
                        self.insert(table="tbl_key",key_name=tag["key"])
                        result = self.execute(stmt="""select * from {} where key_name="{}";""".format("tbl_key",tag["key"]))
                        key_id = result[0]["id"]
                    domain = tag["desc_id"].split(".")[0]
                    self.insert(table="tbl_tag_{}".format(domain),corpus_id=str(corpus_id),key_id=str(key_id),value=str(tag["value"]),desc_id=tag["desc_id"],time=tag["time"],sn=str(i+1))
            except Exception as e:
                print(traceback.format_exc())
                fail.append(i+1)
                flag = False
        return flag,fail
            

    
    def exportData(self,sql,dup=True):
        # log writter
        log_writter = log.log().getLog()

        # 只考虑了tbl_tag表搜索全部字段的情况 select * from tbl_tag where ....;
        result = self.execute(stmt=sql)
        if len(result) == 0:
            return None
        tmp = collections.OrderedDict()

        if dup:
            for res in result:
                if res["sn"] not in tmp:
                    tmp[res["sn"]] = []

                ele = collections.OrderedDict()
                for key,value in res.items():
                    if key in ["id","sn"]:
                        continue
                    ele[key] = value
                tmp[res["sn"]].append(ele)
        else:
            corpus_id2sn = dict()
            for res in result:
                if res["sn"] not in tmp:
                    tmp[res["sn"]] = []
                ele = collections.OrderedDict()
                for key,value in res.items():
                    if key in ["id","sn"]:
                        continue
                    ele[key] = value
                if ele["corpus_id"] not in corpus_id2sn:
                    corpus_id2sn[ele["corpus_id"]] = res["sn"]
                    tmp[res["sn"]].append(ele)
                elif corpus_id2sn[ele["corpus_id"]] == res["sn"]:
                    tmp[res["sn"]].append(ele)
        
        standard_form_list = []
        for key,value in tmp.items():
            if len(value) == 0:
                continue
            corpus_id = None
            for one in value:
                if "corpus_id" in one:
                    corpus_id = one["corpus_id"]
            query = self.execute(stmt="select query from tbl_corpus where id = {corpus_id};".format(corpus_id=corpus_id))[0]["query"]
            ele = collections.OrderedDict()
            ele["query"] = query
            ele["tags"] = []
            sorted_value = sorted(value,key=lambda x:int(x["key_id"]))
            for val in sorted_value:
                val.pop("corpus_id")
                key_name = self.execute(stmt="select key_name from tbl_key where id = {key_id};".format(key_id=val["key_id"]))[0]["key_name"]
                val.pop('key_id')
                val["key"] = key_name
                ele["tags"].append(val)
            standard_form_list.append(ele)
        standard_form = json.dumps(standard_form_list,ensure_ascii=False)
        return standard_form
                  
    

    def insert_task(self,description,catagory):
        if catagory is None:
            status = "1"
        else:
            status = catagory
        self.insert(table="tbl_task",description=description,status=status)
        lastrowid = self.cursor.lastrowid
        return lastrowid

    def insert_batch(self,task_id,batch_id,description):
        self.insert(table="tbl_batch",task_id=task_id,batch_id=batch_id,description=description)
        lastrowid = self.cursor.lastrowid
        return lastrowid
        
if __name__ == "__main__":
    query = "住院日额保险金,"
    a = accessRDB()
    result = a.execute(stmt="""select * from {} where query="{}";""".format("tbl_corpus",query))
    print(result) 
