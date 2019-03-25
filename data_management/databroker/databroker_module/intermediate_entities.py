# encoding: utf-8
import json
from databroker.databroker_module import abstract

class intermediate_entities(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            slots = currentMatcher[0]["slots"]
            result = []
            for key,value in slots.items():
                if key.lower() in map(lambda x: x.lower(),["datatype","ConditionProperty","DiffusionProperty","HualObjectproperty","YShapeProperty"]):
                    continue
                if key == "intentAnswer":
                    result.append(["{}-intent".format(key),str(value[0]["matched"]["hits"][0]["intent"])])
                elif key == "faqAnswer":
                    result.append(["{}-standardQuestion".format(key),str(value[0]["matched"]["standardQuestion"])])
                else:
                    result.append([key,str(value[0]["matched"])])
            if len(result) == 0:
                return self.__class__.__name__,""
            result = sorted(result,key=lambda x:x[0])
            entities = "^".join(map(lambda x: "#".join(x),result))
            return self.__class__.__name__,entities
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
