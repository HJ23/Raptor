from src.Base import BaseClass
from utils.Utility import logger


class VirusTotal(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.API_KEY=self.get_credentials()["VirusTotal_API_KEY"]
        self.URL="https://www.virustotal.com/vtapi/v2/domain/report?domain={domain}&apikey={key}"
    
    @logger("VirusTotal")
    def start(self,domain):
        results=[]
        try:
            tmp_url=self.URL.format(key=self.API_KEY,domain=domain)
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_out=out.json()
                results+=json_out["subdomains"] if("subdomains" in json_out) else []
        except Exception as e:
            print(e)
        return BaseClass.clean(results,domain)
        