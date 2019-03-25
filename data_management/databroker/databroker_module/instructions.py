# encoding: utf-8
import json
from databroker.databroker_module import abstract

class instructions(abstract.abstract):
    def process(self,msg):
        try:
            instructions = json.dumps(msg["instructions"],ensure_ascii=False)
            return self.__class__.__name__,instructions
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
