# encoding: utf-8
import json
from databroker.databroker_module import abstract

class intermediate_pquery(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            pquery = currentMatcher[0]["pQuery"]
            return self.__class__.__name__,pquery
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)