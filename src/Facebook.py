from .Base import BaseClass
import time
from utils.Utility import logger,Log

class FacebookCert(BaseClass):
    def __init__(self):
        super().__init__()
        
        credentials=self.get_credentials()
        
        self.APP_SECRET=credentials["Facebook_API_SECRET"]
        self.APP_ID=credentials["Facebook_API_ID"]
        
        self.GETAUTH="https://graph.facebook.com/oauth/access_token?client_id={Id}&client_secret={secret}&grant_type=client_credentials"
        self.GETDOMAINS="https://graph.facebook.com/certificates?fields=domains&access_token={token}&query=*.{domain}"
        
        self.TOKEN=self.getAuth()
        
    def getAuth(self):
        tmp_url=self.GETAUTH.format(Id=self.APP_ID,secret=self.APP_SECRET)
        out=self.requester.sendGET(tmp_url)
        json_resp=out.json()
        # assert key not found !
        return json_resp["access_token"] if("access_token" in json_resp) else ""
    
    @logger("FacebookCert")
    def start(self,domain):
        results=[]
        tmp_url=self.GETDOMAINS.format(domain=domain,token=self.TOKEN)
        
        try:
            while(tmp_url!=""):
                out=self.requester.sendGET(tmp_url)
                if(not out is None and out.status_code==200):
                    json_resp=out.json()
                    for domain_obj in json_resp["data"]:
                        results+=domain_obj["domains"]

                    time.sleep(2)   
                    tmp_url=json_resp["paging"]["next"] if("next" in json_resp["paging"]) else ""
                else:
                    break
        except Exception as e:
            Log.info(e)
        return BaseClass.clean(results, domain)
