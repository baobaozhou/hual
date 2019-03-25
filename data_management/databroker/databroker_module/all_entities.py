# encoding: utf-8
import json
from databroker.databroker_module import abstract

class all_entities(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            slots = currentMatcher[0]["slots"]
            annotations = ""
            NLU_Entities = []
            for key in slots:
                if (key == "人寿保险_产品"):                
                    list = slots[key]
                    for list_item in list:
                        NLU_Entities.append(list_item["matched"])
                        NLU_Entities_realStart = list_item["realStart"]
                        NLU_Entities_realEnd = list_item["realEnd"]
            annotations = ",".join(NLU_Entities)
            return self.__class__.__name__,annotations
        except Exception as e:
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
        
