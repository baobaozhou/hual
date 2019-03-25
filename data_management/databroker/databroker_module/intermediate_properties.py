# encoding: utf-8
import json
from databroker.databroker_module import abstract

class intermediate_properties(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            slots = currentMatcher[0]["slots"]
            result = []
            for key,value in slots.items():
                if key.lower() in map(lambda x: x.lower(),["datatype","ConditionProperty","DiffusionProperty","HualObjectproperty","YShapeProperty"]):
                    result.append([key,value[0]["matched"]])
            if len(result) == 0:
                return self.__class__.__name__,""
            result = sorted(result,key=lambda x:x[0])
            properties = "^".join(map(lambda x: "#".join(x),result))
            return self.__class__.__name__,properties
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)
