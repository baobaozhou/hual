# encoding: utf-8
import json
from databroker.databroker_module import abstract

class instructions_type(abstract.abstract):
    def process(self,msg):
        try:
            annotation = msg["instructions"][0]["type"]
            return self.__class__.__name__,annotation
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
