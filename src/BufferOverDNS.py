from src.Base import BaseClass
from utils.Utility import LOGGER,Log


class BufferOverDNS(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://dns.bufferover.run/dns?q=.{domain}"
        
    
    @LOGGER("BufferOverDNS")
    def start(self,domain):
        tmp_url=self.URL.format(domain=domain)
        results=[]
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_resp=out.json()
                section=json_resp["FDNS_A"] if("FDNS_A" in json_resp.keys()) else []
                for result in section:
                    if(len(result.split(","))==2):
                        results.append(result.split(",")[1])
        except Exception as e:
            Log.info(e,"BufferOverDNS")

        return BaseClass.clean(results, domain)

