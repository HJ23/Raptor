from src.Base  import BaseClass
from utils.Utility import LOGGER,Log


class CertDetails(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://certificatedetails.com/api/list/{domain}"
    
    @LOGGER("CertDetails")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            json_resps=out.json()
            
            for json_resp in json_resps:
                results+=[json_resp["CommonName"]] if("CommonName" in json_resp.keys()) else []
                
        except Exception as e:
            Log.info(e,"CertDetails")
        return BaseClass.clean(results, domain)
