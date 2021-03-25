from src.Base import BaseClass
from utils.Utility import LOGGER,Log
import time

class UrlScan(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.API_KEY=self.get_credentials()["URLSCAN_API_KEY"]
        self.URL="https://urlscan.io/api/v1/search/"
    
    
    @LOGGER("UrlScan")
    def start(self,domain,limit=10):
        self.requester.HEADERS["API-KEY"]=self.API_KEY
        counter=0
        results=[]
        has_more=True
        search_after=None
        params = {
            "q": f"domain:{domain}",
            "sort_field": "date",
            "sort_order": "desc",
            "size": "100"
        }
        
        try:
            while(counter<limit and has_more):
                time.sleep(1)
                
                if(not search_after is None):
                    params["search_after"]=",".join(search_after)
                
                out=self.requester.sendGET(self.URL,params=params)
                json_resp=out.json()
                
                for result in json_resp["results"]:
                    results+=[result["page"]["domain"]]                   
                search_after=list(map(lambda x:str(x),result["sort"]))
                has_more=json_resp["has_more"]
                
                counter+=1
        except Exception as e:
            Log.info(e,"UrlScan")
        return BaseClass.clean(results,domain)
