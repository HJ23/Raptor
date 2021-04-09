from src.Base import BaseClass
from utils.Utility import LOGGER,Log
import json 
import time


class GoogleCert(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch?domain={domain}&include_expired=false&include_subdomains=true"
        self.URL_WITHKEY="https://transparencyreport.google.com/transparencyreport/api/v3/httpsreport/ct/certsearch/page?p={key}"

    @LOGGER("GoogleCert")
    def start(self,domain,limit=50):
        
        results=[]
        counter=1
        next_key=""
        tmp_url=""
        
        try:
            while(not next_key is None and counter<limit):
                if(next_key!=""):
                    tmp_url=self.URL_WITHKEY.format(key=next_key)
                elif(next_key==""):
                    tmp_url=self.URL.format(domain=domain)
                out=self.requester.sendGET(tmp_url)
                
                resp = out.content.decode("utf-8", "ignore").replace(")]}'", "")
                data_json = json.loads(resp)
                next_key= data_json[0][3][1]
                data_json = data_json[0][1]
                for result in data_json:
                    results.append(result[1])
                counter+=1
                time.sleep(1.3)
                
        except Exception as e:
            print(e)
            Log.info(e,"GoogleCert")
        
        print(results)
        return BaseClass.clean(results,domain)
