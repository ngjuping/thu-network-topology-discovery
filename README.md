# NetworkTopoTHU

## How to run visualization
Under the view directory, run
```
python serve.py
```

## How to run map.py
```
python3 map.py --input raw/7.csv --output results/7.json --subnet 219.223.176.0/20 --skip 2
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

