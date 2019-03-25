# encoding: utf-8
import json
from databroker.databroker_module import abstract

class raw_entity(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            query = currentMatcher[0]["query"]
            slots = currentMatcher[0]["slots"]
            annotations = ""
            for key in slots:
                if (key == "人寿保险_产品"):
                    list = slots[key]
                    NLU_Entities_realStart = int(list[0]["realStart"])
                    NLU_Entities_realEnd = int(list[0]["realEnd"])
                    annotations = query[NLU_Entities_realStart:NLU_Entities_realEnd]
            return self.__class__.__name__,annotations
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)

