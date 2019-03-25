# encoding: utf-8
import json
import traceback
from databroker.databroker_module import abstract


class pquery(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            str_chosenMatcher = nluResult["chosenMatcher"]
            matcherResultMap = nluResult["matcherResultMap"]
            chosenMatcher = matcherResultMap[str_chosenMatcher]
            pquery = chosenMatcher[0]["pQuery"]
            return self.__class__.__name__,pquery
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)

