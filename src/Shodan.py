from src.Base import BaseClass
from utils.Utility import LOGGER,Log

class Shodan(BaseClass):
    def __init__(self):
        super().__init__()
        credentials=self.get_credentials()

        self.API_KEY=credentials["SHODAN_API_KEY"]
        self.URL="https://api.shodan.io/dns/domain/{domain}?key={api_key}"

    @LOGGER("Shodan")
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain,api_key=self.API_KEY)

        try:
            out=self.requester.sendGET(tmp_url)
            if(not out is None and out.status_code==200):
                json_resp=out.json()
                results+=list(map(lambda x:x+"."+domain,json_resp["subdomains"]))

        except Exception as e:
            Log.info(e,"Shodan")

        return BaseClass.clean(results,domain)

