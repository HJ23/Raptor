### Passive Subdomain Enumeration Tool
---
![raptor](https://user-images.githubusercontent.com/39130214/110909816-fc04c180-8329-11eb-9344-d06f25458f61.png)

---
Raptor is a subdomain enumeration tool that discovers valid subdomains for websites passively. 

Raptor designed to comply with all passive sources licenses, and usage restrictions but speed in mind.

This software currently employs 22 free and commercial services. (Constantly updated if any new resource out there.)

For better results I highly encourage you to get API keys.



### Usage
#### To install requirements execute the command below

```sh
pip3 install -r requirements.txt  
```

#### Find subdomains of 'example.com' . 
```sh
python3 main.py --domain example.com
Or
python3 main.py -d example.com
```

#### Specify filename and extension  or it will use default one.

```sh
python3 main.py --domain example.com --output example.txt  
Or
python3 main.py -d example.com -o example.txt  
```
#### For Outputs check outputs directory.


#### Verbose mode for details.

```sh
python3 main.py --domain example.com --output example.txt --verbose
Or
python3 main.py -d example.com -o example.txt -v
```

### Run with Docker

#### Build an image
```
docker build -t hj23/raptor .
```

#### Run in a container
```
docker run --rm -v $PWD/outputs:/outputs hj23/raptor -d example.com
```

#### API keys for commercial services.

```
These are the commercial services it uses:

- Bing
- BinaryEdge
- VirusTotal
- Shodan
- UrlScan
- Censys

But all these services  provide free limited request package with automatic renewal basis.

for Bing limit is 1000 requests per month.
for BinaryEdge limit is 250 requests per month. 
for VirusTotal limit is 500 requests per day.
for Shodan if you have academic email limit is 100 requests per month. (1 request = 100 result)
for UrlScan limit is 1000 requests per day.
for Censys limit is 250 requests per month.

```
#### Having trouble with API keys ?
Check out our guide here :
[ How to get API keys for Raptor ? ](https://github.com/HJ23/Raptor/wiki)

#### Why this tool works slower than others ?
Well faster not always means better. API calls might take reasonable amount of time.
But most importantly in order not to exceed limits stated above scripts adjusted not only for best performance but also best
for API call allowance.

## Todo
- [ Add more sources ]()

----
#### Logo Credits : https://www.freepik.com/iyasalif
