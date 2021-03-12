from src.Base import BaseClass
from utils.Utility import logger


class ThreatCrowd(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
    
    @logger("ThreatCrowd")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        out=self.requester.sendGET(tmp_url)
        
        if(not out is None):
            resp=out.json()
            results=resp["subdomains"]            
        
        return BaseClass.clean(results,domain)

