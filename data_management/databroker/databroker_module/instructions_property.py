# encoding: utf-8
import json
from databroker.databroker_module import abstract

class instructions_property(abstract.abstract):
    def process(self,msg):
        try:
            params = msg["instructions"][0]["params"]
            annotations = [params.get("condition",""),params.get("object",""),params.get("datatype","")]
            for i in range(len(annotations)):
                if annotations[i] is None:
                    annotations[i] = ""
            annotations = "".join(annotations)
            return self.__class__.__name__,annotations
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
