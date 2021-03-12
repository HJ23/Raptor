from .Base import BaseClass
from utils.Utility import logger


class CertSpotter(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.certspotter.com/v1/issuances?domain={domain}&include_subdomains=true&expand=dns_names"
    
    @logger("CertSpotter")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_resp=out.json()
                for resp in json_resp:
                    results+=resp["dns_names"]
        except Exception as e:
            print(e)
        return BaseClass.clean(results, domain)

