from .Base import BaseClass
from utils.Utility import LOGGER,Log
import time

class Bing(BaseClass):
    def __init__(self):
        super().__init__()
                
        self.URL='''https://api.bing.microsoft.com/v7.0/search'''
        
        self.requester.HEADERS["Ocp-Apim-Subscription-Key"]=self.get_credentials()["BING_API_KEY"]
    
    @LOGGER("Bing")
    def start(self,domain,limit=15):
        results=[]
        params={"q":"","textFormat":"HTML","count":50}
        params["q"]='''"*.'''+domain+'''"'''
        limits=0
        
        try:
            for x in range(0,limit):
                params["offset"]=limits
                out=self.requester.sendGET(self.URL,params=params)
                if(not out is None and out.status_code==200):
                    json_resp=out.json()
                    for resp in json_resp["webPages"]["value"]:
                        results+=[resp["url"]]
                limits=len(results)
                time.sleep(2)
        except Exception as e:
            Log.info(e,"Bing")
            
        return BaseClass.clean(results,domain)