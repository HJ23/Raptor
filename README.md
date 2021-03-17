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
#### This software currently uses 15 free and commercial services.

#### API keys for commercial services.

```
For better results i highly encourage you to get API keys.
Raptor uses 3 commercial products for its enumeration.

- Bing
- BinaryEdge
- VirusTotal

But all these services also provide free limited request package with automatic renewal basis.

for Bing limit is 1000 request per month.
for BinaryEdge limit is 250 request per month. 
for VirusTotal limit is 500 request per day.


```
#### Having trouble with API keys ?
Check out our guide here :
[ How to get API keys for Raptor ? ](https://github.com/HJ23/Raptor/wiki)



## Todo
- [ Add more sources ]()
- [ Add bruteforcer ]()
- [ Improve verbose mode ]()
- [  ]()

----
#### Logo Credits : https://www.freepik.com/iyasalif
