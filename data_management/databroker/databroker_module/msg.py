# encoding: utf-8
import json
from databroker.databroker_module import abstract

class msg(abstract.abstract):
    def process(self,msg):
        msg = json.dumps(msg,ensure_ascii=False)
        return self.__class__.__name__,msg
