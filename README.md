# NetworkTopoTHU

## How to run visualization
Under the view directory, run
```
 python -m http.server 8080
```

## How to run map.py
```
python3 map.py -i raw/1.csv -o result/1.json -g 1 --skip 500
```

## Target IP CIDRs
- 59.66.0.0/16 
- 101.5.0.0/16 
- 101.6.0.0/16 
- 118.229.0.0/19 
- 166.111.0.0/16 
- 183.172.0.0/15 
- 202.112.39.2/32 
- 219.223.168.0/21 
- 219.223.176.0/20 

## Zmap ip ping test command
`sudo zmap --probe-module=icmp_echoscan -B 10M -o results.csv 101.5.0.0/16`

