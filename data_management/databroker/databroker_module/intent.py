# encoding: utf-8
import json
from databroker.databroker_module import abstract

class intent(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            slots = currentMatcher[0]["slots"]

            intent = ""
            NLU_ConditionProperty=""
            NLU_DiffusionProperty =""
            NLU_HualObjectProperty =""
            NLU_datatype = ""
            for key in slots:
                if (key == "datatype"):
                    list = slots[key]
                    NLU_datatype = list[0]["matched"]
                if (key == "ConditionProperty"):
                    list = slots[key]
                    NLU_ConditionProperty = list[0]["matched"]
                if (key == "DiffusionProperty"):
                    list = slots[key]
                    NLU_DiffusionProperty = list[0]["matched"]
                if (key == "HualObjectProperty"):
                    list = slots[key]
                    NLU_HualObjectProperty = list[0]["matched"]
            if(NLU_ConditionProperty != "" and NLU_DiffusionProperty =="" and NLU_HualObjectProperty == "" and NLU_datatype == ""):
                intent = "sys.knowledge_query?ConditionProperty="+ NLU_ConditionProperty
            elif(NLU_ConditionProperty != "" and NLU_DiffusionProperty =="" and NLU_HualObjectProperty == "" and NLU_datatype != ""):
                intent = "sys.knowledge_query?ConditionProperty=" + NLU_ConditionProperty +"&datatype=" + NLU_datatype
            elif(NLU_ConditionProperty == "" and NLU_DiffusionProperty !="" and NLU_HualObjectProperty == "" and NLU_datatype == ""):
                intent = "sys.knowledge_query?DiffusionProperty=" + NLU_DiffusionProperty
            elif(NLU_ConditionProperty == "" and NLU_DiffusionProperty !="" and NLU_HualObjectProperty == "" and NLU_datatype != ""):
                intent = "sys.knowledge_query?DiffusionProperty=" + NLU_DiffusionProperty + "&datatype=" + NLU_datatype
            elif(NLU_ConditionProperty == "" and NLU_DiffusionProperty == "" and NLU_HualObjectProperty != "" and NLU_datatype == ""):
                intent = "sys.knowledge_query?HualObjectProperty=" + NLU_HualObjectProperty
            elif (NLU_ConditionProperty == "" and NLU_DiffusionProperty == "" and NLU_HualObjectProperty == "" and NLU_datatype != ""):
                intent = "sys.knowledge_query?datatype=" + NLU_datatype
            return self.__class__.__name__,intent
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)