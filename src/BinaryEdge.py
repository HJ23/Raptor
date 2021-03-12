from src.Base import BaseClass
from utils.Utility import logger

class BinaryEdge(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://api.binaryedge.io/v2/query/domains/subdomain/{domain}"
        self.API_KEY=self.get_credentials()["BinaryEdge_API_KEY"]

    
    # for starter plan limit param should be used becuase of the API monthly limit
    @logger("BinaryEdge")
    def start(self,domain,limit=10):
        results=[]
        tmp_url=self.URL.format(domain=domain)
        counter=0
        param={"page":"1"}
        
        while(counter<limit):
            self.requester.HEADERS["X-Key"]=self.API_KEY
            out=self.requester.sendGET(tmp_url,params=param)
            
            if(not out is None and out.status_code==200):
                json_resp=out.json()
                counter+=1
                results+=json_resp["events"]
                
                if(int(json_resp["total"]//json_resp["pagesize"])+1<limit ):
                    limit=int(json_resp["total"]//json_resp["pagesize"])+1   
            else:
                break
                
        return BaseClass.clean(results,domain)
