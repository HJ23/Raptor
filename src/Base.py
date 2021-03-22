import yaml
import os
from utils.Utility import RequestClass

class BaseClass:
    VERBOSE_MODE=False
    
    def __init__(self):
        self.requester=RequestClass()
    
    
    @staticmethod
    def get_credentials():
        return yaml.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","config","configs.yaml")))
    
    def start(self,domain):
        raise NotImplementedError("Base class start method not implemented!")

    @staticmethod
    def clean(results,domain)->list:
        final=set()
        for url in results:
            for useless in ["https://","http://",":","\\","*","https:\\\\","http:\\\\"]:
                url=url.replace(useless,"")
            
            splitted=url.split("/")
            if( splitted[0].endswith("."+domain) and splitted[0][0].isalnum() ):
                final.add(splitted[0])

        return list(final)

