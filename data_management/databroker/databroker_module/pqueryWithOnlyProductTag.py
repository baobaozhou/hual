# encoding: utf-8
import json
from databroker.databroker_module import abstract

class pqueryWithOnlyProductTag(abstract.abstract):
    def process(self,msg):
        try:
            nluResult = msg["nluResult"]
            queryActsBeforeIntent = nluResult["queryActsBeforeIntent"]
            queryActsBeforeIntent_idx_0 = queryActsBeforeIntent[0]
            query = queryActsBeforeIntent_idx_0["query"]
            pqueryWithOnlyProductTag = query
            if "人寿保险_产品" in queryActsBeforeIntent_idx_0["slots"]:
                for ele in queryActsBeforeIntent_idx_0["slots"]["人寿保险_产品"]:
                    start = ele["realStart"]
                    end = ele["realEnd"]
                    pqueryWithOnlyProductTag = pqueryWithOnlyProductTag.replace(query[start:end],"{{人寿保险_产品}}")
            return self.__class__.__name__,pqueryWithOnlyProductTag
        except Exception as e:
            msg = json.dumps(msg,ensure_ascii=False)
            return self.__class__.__name__,"error:{msg}".format(msg=msg)

