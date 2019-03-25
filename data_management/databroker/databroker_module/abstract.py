# encoding: utf-8

import json


class abstract(object):
    def process(self,*args,**kwargs):
        pass
        
    def timeout(self):
        return self.__class__.__name__,"timeout"

    def response_illegal(self):
        return self.__class__.__name__,"response illegal"

    def query_empty(self):
        return self.__class__.__name__,"query empty"