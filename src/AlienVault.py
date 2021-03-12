from .Base  import BaseClass
from utils.Utility import logger


class AlienVault(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://otx.alienvault.com/api/v1/indicators/domain/{domain}/passive_dns"
    
    @logger("AlienVault")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_resp=out.json()
                resps=json_resp["passive_dns"]
                
                for resp in resps:
                    results.append(resp["hostname"])
        except Exception as e:
            print(e)
        return BaseClass.clean(results, domain)
