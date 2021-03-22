from .Base  import BaseClass
from utils.Utility import LOGGER,Log

class Crobat(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://sonar.omnisint.io/subdomains/{domain}"
    
    @LOGGER("Crobat")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            results=out.json() if(not out.json() is None) else []
        except Exception as e:
            Log.info(e,"Crobat")
        return BaseClass.clean(results, domain) 
