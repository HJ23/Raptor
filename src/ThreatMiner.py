from src.Base import BaseClass
from utils.Utility import logger,Log


class ThreatMiner(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.threatminer.org/v2/domain.php?q={domain}&rt=5"
    
    @logger("ThreatMiner")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_resp=out.json()                   
                results+=json_resp["results"]
        except Exception as e:
            Log.info(e)
        return BaseClass.clean(results,domain)
