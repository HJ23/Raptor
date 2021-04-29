import sys
sys.path.append(".")
import argparse
from src.Raptor import Raptor
from utils.Utility import print_banner,Log

parser=argparse.ArgumentParser(description="Raptor advanced subdomain discovery,recon tool.")

parser.add_argument("--domain","-d",required=True )
parser.add_argument("--threads","-t",required=False,default=10,type=int)
parser.add_argument("--output","-o",required=False,default="raptor_out.txt")
parser.add_argument("--verbose","-v",required=False,action="store_true",default=False)
parser.add_argument("--probe","-p",required=False,action="store_true",default=False)


args=parser.parse_args()

if(__name__=="__main__"):
    print_banner()
    
    obj=Raptor(output=args.output,verbose=args.verbose,probe=args.probe)
    out=obj.start(domain=args.domain)
    obj.save_out(out)
    Log.success("* Total {} subdomains found".format(len(out)))
    