from src.Base import BaseClass
from utils.Utility import logger,Log


class HackerTarget(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.hackertarget.com/hostsearch/?q={domain}"     

    @logger("HackerTarget")
    def start(self,domain):
        tmp_url=self.URL.format(domain=domain)
        results=[]
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None):
                resp=out.text                        
                for result in resp.split("\n"):
                    if(len(result.split(","))==2):
                        results.append(result.split(",")[0])

        except Exception as e:
            Log.info(e)
        return BaseClass.clean(results,domain)
