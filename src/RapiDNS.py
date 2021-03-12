from .Base import BaseClass
from utils.Utility import logger
import re


class RapiDNS(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://rapiddns.io/subdomain/{domain}"
        self.REGEX_URL=re.compile('<a href="(.*?)"')
    
    @logger("RapidDNS")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200 ):
                urls=self.REGEX_URL.findall(out.text)
                results=urls
        except Exception as e:
            print(e)
        
        return BaseClass.clean(results, domain)


