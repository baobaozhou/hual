# encoding: utf-8
import json
from databroker.databroker_module import abstract

class instructions_entities(abstract.abstract):
    def process(self,msg):
        try:
            annotations = msg["instructions"][0]["params"].get("entities")
            if annotations is not None:
                if type(annotations) == type([]):
                    annotations = "^".join(annotations)
            else:
                annotations = ""
            return self.__class__.__name__,annotations
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
