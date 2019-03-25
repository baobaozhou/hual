# encoding: utf-8
import json
from databroker.databroker_module import abstract

class result(abstract.abstract):
    def process(self,msg):
        try:
            result = str(msg["result"])
            return self.__class__.__name__,result
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)

