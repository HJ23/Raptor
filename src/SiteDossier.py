from src.Base import BaseClass
from utils.Utility import LOGGER,Log
from bs4 import BeautifulSoup 


class SiteDossier(BaseClass):
    def __init__(self):
        super().__init__()
        self.URL="http://www.sitedossier.com/parentdomain/{domain}"
        
    @LOGGER("SiteDossier")
    def start(self,domain):
        tmp_url=self.URL.format(domain=domain)
        results=[]
        try:
            out=self.requester.sendGET(tmp_url)
            bs=BeautifulSoup(out.text,"lxml")
            results=list(map(lambda x:x.text,bs.find_all('a',href=True)))
            
        except Exception as e:
            Log.info(e)
        return BaseClass.clean(results,domain)
  