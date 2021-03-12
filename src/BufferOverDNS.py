from src.Base import BaseClass
from utils.Utility import logger


class BufferOverDNS(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://dns.bufferover.run/dns?q=.{domain}"
        self.SECTION="FDNS_A"
    
    @logger("BufferOverDNS")
    def start(self,domain):
        tmp_url=self.URL.format(domain=domain)
        results=[]
        out=self.requester.sendGET(tmp_url)
        if(not out is None):
            json_resp=out.json()
            
            for result in json_resp[self.SECTION]:
                if(len(result.split(","))==2):
                    results.append(result.split(",")[1])
                                
        return BaseClass.clean(results, domain)

