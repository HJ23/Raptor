from .Base import BaseClass
from utils.Utility import logger,Log



class Sublist3r(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.sublist3r.com/search.php?domain={domain}"     
    
    @logger("Sublist3r")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)

            if(not out is None and out.status_code==200):
                resp=out.json()                        
                results+=resp if(not resp is None) else []
        except Exception as e:
            Log.info(e)
        return BaseClass.clean(results,domain)
