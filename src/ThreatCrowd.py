from src.Base import BaseClass
from utils.Utility import LOGGER,Log


class ThreatCrowd(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}"
    
    @LOGGER("ThreatCrowd")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            json_resp=out.json()
            results+=json_resp["subdomains"] if("subdomains" in json_resp.keys()) else []         
        except Exception as e:
            Log.info(e,"ThreadCrowd")
        return BaseClass.clean(results,domain)

