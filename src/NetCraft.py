from src.Base import BaseClass
from utils.Utility import LOGGER,Log
import re
from urllib.parse import urlparse
import hashlib
import urllib.parse as urllib
import time

# This module inspired from sublist3r project 

class NetCraft(BaseClass):
    def __init__(self):
        super().__init__()
        
        self.URL="https://searchdns.netcraft.com/?restriction=site+ends+with&host={domain}"
        self.REGEX_NEXTPAGE=re.compile('''<a.*?href="(.*?)">Next Page''')
        self.REGEX_URL=re.compile('<a class="results-table__host" href="(.*?)"')

    def extract(self,resp):
        tmp_res=[]
        links_list = self.REGEX_URL.findall(resp)
        for link in links_list:
            subdomain = urlparse(link).netloc
            tmp_res.append(subdomain.strip())
        return tmp_res
    
    def create_cookies(self, cookie):
        cookies = dict()
        cookies_list = cookie[0:cookie.find(';')].split("=")
        cookies[cookies_list[0]] = cookies_list[1]
        
        cookies['netcraft_js_verification_response'] = hashlib.sha1(urllib.unquote(cookies_list[1]).encode('utf-8')).hexdigest()
        return cookies

    def get_cookies(self, headers):
        if 'set-cookie' in headers:
            cookies = self.create_cookies(headers['set-cookie'])
        else:
            cookies = {}
        return cookies
    
    @LOGGER("NetCraft") 
    def start(self,domain):
        results=[]
        tmp_url=self.URL.format(domain=domain)

        try:
            out=self.requester.sendGET(tmp_url)
            
            cook=self.get_cookies(out.headers)
            while(True):
                tmp_url=self.URL.format(domain=domain)

                out=self.requester.sendGET(tmp_url,cookies=cook)
                if(not out is None and out.status_code==200):
                    resp=out.text
                    results+=self.extract(resp)           
                    domain=self.REGEX_NEXTPAGE.findall(resp)[0]
                    if(not "Next Page" in resp):
                        break 
                    time.sleep(2)
                else:
                    break
        except Exception as e:
            Log.info(e,"NetCraft")
        return BaseClass.clean(results,domain)
