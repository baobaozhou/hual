# encoding: utf-8

import logging
import os
import threading
class log(object):
    '''
    singleton
    '''
    _instance_lock = threading.Lock()

    def __init__(self,level=logging.INFO,style='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename="messages.log"):
        logpath = os.path.join(
                                os.path.abspath(os.path.join(os.path.dirname(__file__),"..")),
                                "log",
                                filename
                                )
        logging.basicConfig(level=level,format=style,filename=logpath)
        self.logger = logging.getLogger(__file__)
    
    def __new__(cls, *args, **kwargs):
        if not hasattr(log, "_instance"):
            with log._instance_lock:
                if not hasattr(log, "_instance"):
                    log._instance = object.__new__(cls)
        return log._instance

    def getLog(self):
        return self.logger

if __name__ == "__main__":
    l = log()
    n = log()
    print(l)
    print(n)
    
    m = l.getLog()
    m.debug("aaaaa")
