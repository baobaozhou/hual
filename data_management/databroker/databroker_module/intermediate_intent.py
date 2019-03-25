# encoding: utf-8
import json
from databroker.databroker_module import abstract

class intermediate_intent(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            intent = currentMatcher[0]["intent"]
            return self.__class__.__name__,intent
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)