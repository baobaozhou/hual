# encoding: utf-8
import json
from databroker.databroker_module import abstract

class chosenscore(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            chosenscore = str(currentMatcher[0]["score"])
            return self.__class__.__name__,chosenscore
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)