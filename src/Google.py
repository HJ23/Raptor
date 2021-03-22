from src.Base import BaseClass
from utils.Utility import LOGGER,Log
from bs4 import BeautifulSoup 
import time

class Google(BaseClass):
    def __init__(self):
        super().__init__()
        self.URL="https://www.google.com/search?q=site:'*.{item}'&oq=site:'*.{item}'&num=100&start={offset}"
    
    def scrap_urls(self,html):
        results=[]
        tmp_bs=BeautifulSoup(html,"html.parser")
        blocks=tmp_bs.find_all('div', attrs={'class': 'g'})

        for block in blocks:
            results.append(block.find('a', href=True)["href"])
        
        return results
    
    @LOGGER("Google")
    def start(self,domain,limit=5):
        results=[]
        try:
            for page_num in range(limit):
                tmp_url=self.URL.format(item=domain,offset=page_num*100)
                out=self.requester.sendGET(tmp_url)
                if(not out is None and out.status_code==200):
                    results+=self.scrap_urls(out.text)
                    time.sleep(2)
        except Exception as e:
            Log.info(e,"Google")
        return BaseClass.clean(results, domain)
