### Passive Subdomain Enumeration Tool
---
![raptor](https://user-images.githubusercontent.com/39130214/110909816-fc04c180-8329-11eb-9344-d06f25458f61.png)

---


# Usage
#### To install requirements execute command below


```sh
pip3 install -r requirements.txt  
```

#### Find subdomains of 'example.com' : 
```sh
python3 main.py --domain example.com  
```

#### Specify output or it will save as default filename and extension

```sh
python3 main.py --domain example.com --output example.txt  
```



#### Verbose for detailed outputs

```sh
python3 main.py --domain example.com --output example.txt --verbose
```

#### API keys for commercial products
```
Raptor uses 4 commercial products for its enumeration. But all these services also provides free limited amount of request package with monthly automatic renewal.

check out our guide below :
[ How to get API keys for Raptor ? ](https://github.com/HJ23/Raptor/wiki)

for Bing it is 1000 request for month.
for BinaryEdge it is 250 request for month. 
etc.
```

## ToDo
- [ Add more sources ]
- [ Docker ]
- [ Add detailed API key guide for paid services ]


----
#### Logo Credits : https://www.freepik.com/iyasalif
