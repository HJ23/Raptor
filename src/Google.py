from src.Base import BaseClass
from utils.Utility import logger
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
    
    @logger("Google")
    def start(self,domain,limit=4):
        results=[]
        for page_num in range(limit):
            tmp_url=self.URL.format(item=domain,offset=page_num*100)
            out=self.requester.sendGET(tmp_url)
            if(out is None):
                break
            results+=self.scrap_urls(out.text)
            time.sleep(2)
        return BaseClass.clean(results, domain)
