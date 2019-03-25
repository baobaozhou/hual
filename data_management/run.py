# encoding: utf-8
import argparse
import time
import os
import json
import collections
from threading import Thread
import uuid
import os
import shutil
import pandas as pd
import time
from databroker.databroker import databroker
from accessdb.accessRDB import accessRDB

class parallel(object):
    def __init__(self,*args,**kwargs):
        self.mods = args
        self.url = kwargs["url"]
        self.corpus = kwargs["corpus"]
        self.outdir = kwargs["outdir"]
        self.parts = kwargs["parts"]
        self.desc_id = kwargs["desc_id"]
        self.Sequence= kwargs["Sequence"]
        self.uuid = str(uuid.uuid1())
        self.intermediate_indir = 'input/{}/input'.format(self.uuid)
        self.intermediate_outdir = 'input/{}/output'.format(self.uuid)
        os.makedirs(self.intermediate_indir)
        os.makedirs(self.intermediate_outdir)

    def run(self):
        threads = []
        n = 1
        count = self.split(self.parts,self.corpus,self.intermediate_indir)
        print("start")
        for fd in os.listdir(self.intermediate_indir):
            infilepath = os.path.join(self.intermediate_indir,fd)
            if os.path.isfile(infilepath) and fd.endswith(".xlsx"):
                d = databroker(*self.mods,url=self.url,corpus=infilepath)
                t = Thread(target=self.work,args=(d,self.desc_id,self.intermediate_outdir,n,self.Sequence))
                threads.append(t)
                t.start()
                print(n)
                n += 1
        for t in threads:
            t.join()
        print("\033[{}B".format(str(n)))
        print("begin merging")
        all_parts = self.merge(self.intermediate_outdir,self.outdir)
        print("end")
        return count == n and count == all_parts

        
        

    def work(self,d,desc_id,out,position,Sequence):
        result_json = d.Standardize(desc_id,output=None,Sequence=Sequence,position=position)
        d.Specialize(result_json,os.path.join(out,"{corpus}-output-{time}.xlsx".format(corpus=d.corpus.split("/")[-1],time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())))))

    def split(self,n,f,output):
        if  n <= 0:
            print("n=",n)
            shutil.copy(f,output)
            return  1
        if n >= 1000:
            n = 999
        df = pd.read_excel(f)
        total = len(df)
        print("total",total)
        step = total//n
        print("step:{}".format(step))
        left = total%n
        start = 0
        stop = step
        if left > 0:
            stop += 1
            left -= 1
        count = 1
        print("begin spliting")
        while start < total:
            print(count)
            print("range:",start,stop)
            tmp = df[start:stop]
            tmp.to_excel(os.path.join(output,"{}.xlsx".format("%03d"%count)),index=False)
            start = stop
            stop += step
            if left > 0:
                stop += 1
                left -= 1
            count += 1
        return  count
    
    def merge(self,d,output):
        dfs = []
        n = 1
        for fd in os.listdir(d):
            if os.path.isfile(os.path.join(d,fd)) and fd.endswith(".xlsx"):
                dfs.append(pd.read_excel(os.path.join(d,fd)))
                n += 1
        ret_df = pd.concat(dfs)
        outfile = os.path.join(output,"{corpus}-output-{time}.xlsx".format(corpus=corpus.split("/")[-1],time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))))
        ret_df.to_excel(outfile,index=False)
        return n

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='run')
    parser.add_argument('--host',default='115.182.62.171')
    parser.add_argument('-P','--port',default='1781')
    parser.add_argument('-b','--bot')
    parser.add_argument('-c','--corpus')
    parser.add_argument('-m','--mod') # -m entity,intent
    parser.add_argument('--op')
    parser.add_argument('--filter')
    parser.add_argument('--dup',help='this param specifies duplication or not when exporting , 0 represents none-duplication, others represents duplication',)
    parser.add_argument('-o','--out')
    parser.add_argument('--desc_id')
    parser.add_argument("--description") # task or batch 's description
    parser.add_argument("--task_id") # specify that the id of a task that owns this batch
    parser.add_argument("--catagory",help="1:badcase 2:taikang_corpus") 
    parser.add_argument("--batch_id") # the serial number of a batch in one task
    parser.add_argument("--parts") # the part of parallel
    parser.add_argument("--parallel_seq") # the Sequence mode of parallel

    # using when debug
    parser.add_argument("--jsonfile")
    args = parser.parse_args()
    host = args.host
    port = args.port
    bot = args.bot
    url  = 'http://{host}:{port}/bot/{bot}/simulator'.format(host=host,port=port,bot=bot)
    op = args.op
    if op == 'import':
        a = accessRDB()
        corpus = args.corpus
        desc_id = args.desc_id
        mod = args.mod
        if mod is None:
            mod = []
        else:
            mod = mod.split(',')
        # d = databroker("entity","intent",url=url,corpus=corpus)
        d = databroker(*mod,url=url,corpus=corpus)
        result_json = d.Standardize(desc_id,output="std_json/{time}.json".format(time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))))
        flag,fail = a.importData(result_json)
        print(flag)
        print(fail)
    elif op == 'export':
        a = accessRDB()
        SQL = args.filter
        out = args.out
        dup = args.dup
        d = databroker(url=url,corpus=None)
        if dup == '0':
            output = a.exportData(SQL,dup=False)
        else:
            output = a.exportData(SQL,dup=True)
        # print(s)
        d.Specialize(output,os.path.join(out,"output-{time}.xlsx".format(time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())))))
        # select * from tbl_tag where desc_id = "task01_batch01"
    elif op == 'newtask':
        a = accessRDB()
        description = args.description
        catagory = args.catagory
        task_id = a.insert_task(description,catagory)
        print(task_id)
    elif op == 'newbatch':
        a = accessRDB()
        task_id = args.task_id
        batch_id = args.batch_id
        description = args.description
        batch_id = a.insert_batch(task_id,batch_id,description)
        print(task_id)
        print(batch_id)
    elif op == 'importfromjson':
        a = accessRDB()
        jsonfile = args.jsonfile
        with open (jsonfile,encoding="utf-8") as f:
            jsondata = json.load(f,object_pairs_hook=collections.OrderedDict)
            jsondata = json.dumps(jsondata,ensure_ascii=False)
            flag,fail = a.importData(jsondata)
            print(flag)
            print(fail)
    elif op == 'exportfromjson':
        jsonfile = args.jsonfile
        out = args.out
        d = databroker(*[],url=url,corpus=None)
        with open(jsonfile,encoding="utf-8") as f:
            jsondata = json.load(f,object_pairs_hook=collections.OrderedDict)
            jsondata = json.dumps(jsondata,ensure_ascii=False)
            d.Specialize(jsondata,os.path.join(out,"output-{time}.xlsx".format(time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())))))
    elif op == 'batchprocessing':
        corpus = args.corpus
        desc_id = "batchprocessing-" + time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
        out = args.out
        mod = args.mod
        if mod is None:
            mod = []
        else:
            mod = mod.split(',')
        # d = databroker("entity","intent",url=url,corpus=corpus)
        d = databroker(*mod,url=url,corpus=corpus)
        result_json = d.Standardize(desc_id,output="std_json/{time}.json".format(time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))))
        d.Specialize(result_json,os.path.join(out,"{corpus}-output-{time}.xlsx".format(corpus=corpus.split("/")[-1],time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())))))
    
    elif op == 'batchprocessing-seq':
        corpus = args.corpus
        desc_id = "batchprocessing-seq-" + time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
        out = args.out
        mod = args.mod
        if mod is None:
            mod = []
        else:
            mod = mod.split(',')
        # d = databroker("entity","intent",url=url,corpus=corpus)
        d = databroker(*mod,url=url,corpus=corpus)
        result_json = d.Standardize(desc_id,output="std_json/{time}.json".format(time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))),Sequence=True)
        d.Specialize(result_json,os.path.join(out,"{corpus}-output-{time}.xlsx".format(corpus=corpus.split("/")[-1],time=time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time())))))

    elif op == 'parallel':
        corpus = args.corpus
        desc_id = "batchprocessing-" + time.strftime('%Y-%m-%d-%H_%M_%S',time.localtime(time.time()))
        out = args.out
        mod = args.mod
        Sequence = args.parallel_seq
        if Sequence is None:
            Sequence = False
        else:
            Sequence = True
        parts = int(args.parts)
        if mod is None:
            mod = []
        else:
            mod = mod.split(',')
        p = parallel(*mod,url=url,corpus=corpus,outdir=out,desc_id=desc_id,parts=parts,Sequence=Sequence)
        print(p.run())

    else:
        print("请输出正确的op名称")
