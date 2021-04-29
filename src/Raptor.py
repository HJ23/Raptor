from src.Facebook import FacebookCert
from src.RapiDNS import RapiDNS
from src.BufferOverDNS import BufferOverDNS
from src.HackerTarget import HackerTarget
from src.NetCraft import NetCraft
from src.DNSDumpster import DNSDumpster
from src.VirusTotal import VirusTotal
from src.BinaryEdge import BinaryEdge
from src.ThreatCrowd import ThreatCrowd
from src.Sublist3r import Sublist3r
from src.ThreatMiner import ThreatMiner
from src.CertSpotter import CertSpotter 
from src.Bing import Bing
from src.AlienVault import AlienVault
from src.Google import Google
from src.Shodan import Shodan
from src.Base import BaseClass
from src.Crobat import Crobat
from src.SiteDossier import SiteDossier
from src.UrlScan import UrlScan
from src.Censys import Censys
from src.CertDetails import CertDetails
from src.GoogleCert import GoogleCert
from src.HttProbe import HttProbe


from concurrent.futures import ThreadPoolExecutor
from utils.Utility import TIMER 
import os

class Raptor:
    def __init__(self,output,threads=10,verbose=False,probe=False):
        self.modules=[FacebookCert(),RapiDNS(),BufferOverDNS(),HackerTarget(),NetCraft(),
                      DNSDumpster(),VirusTotal(),BinaryEdge(),ThreatCrowd(),ThreatMiner(),GoogleCert(),
                      UrlScan(),CertDetails(),Censys(),Sublist3r(),CertSpotter(),Bing(),SiteDossier(),AlienVault(),Google(),Shodan(),Crobat()]
        self.probe=probe
        self.output=output
        self.threads=threads
        BaseClass.VERBOSE_MODE=verbose
        
    def save_out(self,results):

        cur_dir=os.path.dirname(os.path.abspath(__file__))
        out_dir=os.path.join(cur_dir,"..","outputs",self.output)
        
        final=list(map(lambda x:x+"\n",results))
        with open(out_dir,"w") as file:
            file.writelines(final)
        return 
               
    @TIMER
    def start(self,domain):
        final=[domain]
        futures=[]
        with ThreadPoolExecutor(self.threads) as thread:
            for module in self.modules:
                futures.append(thread.submit(module.start,domain=domain))
        
        for future in futures:
            final+=future.result()        

        final=list(set(final))
        if(self.probe):
            probe_obj=HttProbe(self.threads)
            final=probe_obj.start(final)

        return final
        
