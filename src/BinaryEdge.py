from src.Base import BaseClass
from utils.Utility import LOGGER,Log

class BinaryEdge(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.binaryedge.io/v2/query/domains/subdomain/{domain}"
        self.API_KEY=self.get_credentials()["BINARYEDGE_API_KEY"]

    
    # for starter plan limit param should be used becuase of the API monthly limit
    @LOGGER("BinaryEdge")
    def start(self,domain,limit=10):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        counter=1
        
        try:
            while(counter<limit):
                param={"page":str(counter)}
                self.requester.HEADERS["X-Key"]=self.API_KEY
                out=self.requester.sendGET(tmp_url,params=param)
                
                json_resp=out.json()
                
                # adjust limit for gathered results
                if("total" in json_resp.keys() and int(json_resp["total"]//json_resp["pagesize"])+1<limit ):
                    limit=int(json_resp["total"]//json_resp["pagesize"])+1   
                
                counter+=1
                results+=json_resp["events"] if("events" in json_resp.keys()) else []
                
        except Exception as e:
            Log.info(e,"BinaryEdge")
                
        return BaseClass.clean(results,domain)
