import time
from termcolor import cprint
import requests as req
from functools import wraps
from requests.packages.urllib3.exceptions import InsecureRequestWarning
req.packages.urllib3.disable_warnings(InsecureRequestWarning)


class RequestClass:
    def __init__(self):
        self.HEADERS={ "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",\
                       "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                       "Accept-Language": "en-US,en;q=0.8",
                       "Accept-Encoding": "gzip",}
        self.SESSION=req.Session()

    def get_cookies(self, headers):
        if 'set-cookie' in headers:
            cookies = self.create_cookies(headers['set-cookie'])
        else:
            cookies = {}
        return cookies


    def sendGET(self,url,cookies=None,params=None,timeout=17):
        return self.SESSION.get(url=url,params=params,headers=self.HEADERS,verify=False,timeout=timeout,cookies=cookies)

    
    def sendPOST(self,url,params=None,cookies=None,json=None,auth=None,timeout=17):
        return self.SESSION.post(url,data=params,json=json,auth=auth,headers=self.HEADERS,verify=False,timeout=timeout,cookies=cookies)
        

def TIMER(func):
    def run(*args,**kwargs):
        start=time.time()
        out=func(*args,**kwargs)
        Log.success(f"* Total elapsed time : {time.time()-start}")
        return out
    return run

class Log:
    @staticmethod
    def info(arg,name=""):
        from src.Base import BaseClass
        if(BaseClass.VERBOSE_MODE):
            if(isinstance(arg,str)):
                cprint("# [INFO] "+arg,"blue")
            else:
                cprint("# [INFO] "+str(arg)+" : "+name,"red")
        return
    @staticmethod
    def success(arg):
        cprint(arg,"green")
        return


def LOGGER(name):
    def wrapper(func):
        @wraps(func)
        def run(*args,**kwargs):
            Log.info(f"* {name} just started !")
            out=func(*args,**kwargs)
            Log.info(f"* {name} just finished ! {len(out)} subdomains found !")
            return out
        return run
    return wrapper




def print_banner():
    print("\n\n")
    cprint("   8888888b.                    888                    ","green")
    cprint("   888   Y88b                   888                    ","green")
    cprint("   888    888                   888                    ","green")
    cprint("   888   d88P  8888b.  88888b.  888888 .d88b.  888d888 ","green")
    cprint('''   8888888P"      "88b 888 "88b 888   d88""88b 888P"''',"green")
    cprint("   888 T88b   .d888888 888  888 888   888  888 888  ","blue")
    cprint("   888  T88b  888  888 888 d88P Y88b. Y88..88P 888     ","green")
    cprint('''   888   T88b "Y888888 88888P"   "Y888 "Y88P"  888   ''',"green")
    cprint("                       888                         ","green")
    cprint("                       888                         ","green")
    cprint("                       888                         ","green")
    print("\n")
    cprint("- Raptor fast passive subdomain enumeration tool.","blue")
    cprint("- github.com/HJ23/Raptor","green")
    print("\n")    
    
