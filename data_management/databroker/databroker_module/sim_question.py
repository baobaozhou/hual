# encoding: utf-8
import json
from databroker.databroker_module import abstract

class sim_question(abstract.abstract):
    def process(self,msg):
        try:
            annotations = ""
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            annotations = ""
            if chosenMatcher == "FaqIntentMatcher":
                currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
                slots = currentMatcher[0]["slots"]
                if "faqAnswer" in slots:
                    content = nluResult["matcherResultMap"]["FaqIntentMatcher"][0]["slots"]["faqAnswer"][0]["matched"]["hits"]
                else:
                    content = []
                tmp = []
                for ele in content:
                    tmp.append("#".join(ele["sim_question"]))
                if len(tmp) != 0:
                    annotations = '^'.join(tmp)
            return self.__class__.__name__,annotations
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)

