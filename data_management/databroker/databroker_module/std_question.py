# encoding: utf-8
import json
from databroker.databroker_module import abstract

class std_question(abstract.abstract):
    def process(self,msg):
        try:
            annotations = ""
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            if chosenMatcher == "FaqIntentMatcher":
                currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
                slots = currentMatcher[0]["slots"]
                if "faqAnswer" in slots:
                    annotations = slots["faqAnswer"][0]["matched"]["standardQuestion"]
            return self.__class__.__name__,annotations
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)

