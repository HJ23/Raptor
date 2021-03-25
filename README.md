### Passive Subdomain Enumeration Tool
---
![raptor](https://user-images.githubusercontent.com/39130214/110909816-fc04c180-8329-11eb-9344-d06f25458f61.png)

---

# Usage
#### To install requirements execute the command below

```sh
pip3 install -r requirements.txt  
```

#### Find subdomains of 'example.com' . 
```sh
python3 main.py --domain example.com  
```

#### Specify filename and extension  or it will use default one.

```sh
python3 main.py --domain example.com --output example.txt  
```
#### For Outputs check outputs directory.


#### Verbose mode for details.

```sh
python3 main.py --domain example.com --output example.txt --verbose
```

#### API keys for commercial services.

```
For better results I highly encourage you to get API keys.
This software currently uses 19 free and commercial services.
These are the commercial services it uses:

- Bing
- BinaryEdge
- VirusTotal
- Shodan
- UrlScan

But all these services also provide free limited request package with automatic renewal basis.

for Bing limit is 1000 request per month.
for BinaryEdge limit is 250 request per month. 
for VirusTotal limit is 500 request per day.
for Shodan if you have academic email limit is 100 request per month. (1 request = 100 result)
for UrlScan limit is 1000 request per day.
```
#### Having trouble with API keys ?
Check out our guide here :
[ How to get API keys for Raptor ? ](https://github.com/HJ23/Raptor/wiki)

#### Why this tool works slower than others ?
Well faster not always mean better. API calls might take reasonable amount of time.
Also in order not to exceed limits stated above scripts adjusted not only for best performance but also best
for API call allowance.

## Todo
- [ Add more sources ]()

----
#### Logo Credits : https://www.freepik.com/iyasalif
