from utils.Utility import *
from src.Base import BaseClass
from concurrent.futures import ThreadPoolExecutor


class HttProbe(BaseClass):
    def __init__(self,threads):
        super().__init__()
        self.threads=threads
        self.ports=["81", "300", "591", "593", "832", "981", "1010", "1311", "2082", "2087", "2095", "2096", "2480", "3000", "3128", "3333", "4243", "4567", "4711", "4712", "4993", "5000", "5104", "5108", "5800", "6543", "7000", "7396", "7474", "8000", "8001", "8008", "8014", "8042", "8069", "8080", "8081", "8088", "8090", "8091", "8118", "8123", "8172", "8222", "8243", "8280", "8281", "8333", "8443", "8500", "8834", "8880", "8888", "8983", "9000", "9043", "9060", "9080", "9090", "9091", "9200", "9443", "9800", "9981", "12443", "16080", "18091", "18092", "20720", "28017","4443"]
    
    def check(self,domain):
        results=[]
        
        for prefix in ["http://","https://"]:
            try:
                url=prefix+domain
                self.requester.sentGET(url,timeout=9)
                results.append(url)                    
            except Exception as e:
                Log.info(e,"HttProbe")
        
        for prefix in ["http://","https://"]:
            for port in self.ports:
                try:
                    url=prefix+domain+":"+port
                    self.requester.sendGET(url,timeout=9)
                    results.append(url)                    
                except Exception as e:
                    Log.info(e,"HttProbe")
        return results     
        
    
    def start(self,domains):
        
        final=[]
        futures=[]
        with ThreadPoolExecutor(self.threads) as thread:
            for domain in domains:
                futures.append(thread.submit(self.check,domain=domain))
        
        for future in futures:
            final+=future.result()
        
        return final
