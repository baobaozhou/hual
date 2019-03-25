# encoding: utf-8
import json
from databroker.databroker_module import abstract


class entity(abstract.abstract):
    def process(self, msg):
        try:
            nluResult = msg["nluResult"]
            chosenMatcher = nluResult["chosenMatcher"]
            currentMatcher = nluResult["matcherResultMap"][chosenMatcher]
            slots = currentMatcher[0]["slots"]
            annotations = ""
            for key in slots:
                if (key == "人寿保险_产品"):
                    NLU_Entities = []
                    list = slots[key]
                    for list_item in list:
                        NLU_Entities.append(list_item["matched"])
                        NLU_Entities_realStart = list_item["realStart"]
                        NLU_Entities_realEnd = list_item["realEnd"]
                        annotations = "[{\"from\":" + str(int(NLU_Entities_realStart)) + ",\"to\":" + str(
                            int(NLU_Entities_realEnd)) + ",\"category\":\"dict\",\"type\":\"人寿保险_产品\",\"value\":\"" + \
                                      NLU_Entities[0] + "\"}]"
            return self.__class__.__name__, annotations
        except Exception as e:
            msg = json.dumps(msg, ensure_ascii=False)
            return self.__class__.__name__, "error:{msg}".format(msg=msg)
