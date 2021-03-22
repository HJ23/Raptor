from src.Base import BaseClass
from utils.Utility import LOGGER,Log


class ThreatMiner(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.threatminer.org/v2/domain.php?q={domain}&rt=5"
    
    @LOGGER("ThreatMiner")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_resp=out.json()                   
                results+=json_resp["results"] if("results" in json_resp.keys()) else []
        except Exception as e:
            Log.info(e,"ThreadMiner")
        return BaseClass.clean(results,domain)
