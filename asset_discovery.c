Group1-center left
Group2-center right
Group3-bottom left
Group4-bottom right
Group5-righttop

Yellow Dots (shenzhen)
219.223.190.2 (dns.sz.tsinghua.edu.cn)
219.223.190.1
219.223.190.14
219.223.190.4
219.223.190.5

Group 1-1 (Mostly printers except 1)
59.66.192.2
59.66.160.4
59.66.142.3
59.66.189.12
59.66.234.11

Group 1-2 (some printers some servers)
166.111.147.229
166.111.6.16
166.111.166.88
166.111.30.164
166.111.153.172
166.111.147.1
166.111.152.229

Group 2-1 (Server cluster)
101.6.109.31 (xmpp, opsmessaging)
101.6.50.212
101.6.160.9 (Database)
101.6.130.24
101.6.50.134 (wswbtserver,msft-ds)

Group 2-2 (Web servers, printers, self hosted Gitlab)
166.111.53.22
166.111.4.25
166.111.90.156
166.111.224.126
166.111.69.46 (self hosted gitlab)
http://166.111.69.46/users/sign_in (self hosted gitlab)
166.111.89.61
166.111.5.228
166.111.224.205
166.111.180.6

Group 3 (up but no service,probably router, some http servers)
183.172.236.65
183.172.158.69
183.172.91.146
183.172.211.165
183.172.194.218
183.172.172.194
183.172.204.85
183.172.243.152
183.172.188.53
183.172.186.176

Group 4 (Some ftps, filtered web servers)
183.172.168.32
183.172.218.133
183.172.144.14
183.172.217.23
183.172.164.191
183.172.229.69
183.172.212.231
183.172.85.199
183.172.195.29


Group 5 (59.66.X.X up but no service, some web servers)
59.66.120.155
59.66.126.61
59.66.126.214
59.66.127.18
59.66.121.173
59.66.124.199
166.111.12.147 (Printer page)
http://166.111.12.147/web/guest/en/websys/webArch/mainFrame.cgi
166.111.15.209
166.111.158.12
101.6.54.73
101.6.69.3
101.6.64.81

Core nodes
118.229.2.78 (bgp,idp)
118.229.2.66 sas
172.17.2.30 cant access
172.17.2.26 sas
118.229.2.14 (bgp,ldp)
118.229.2.13 (middle)
--- node to the core web servers
118.229.9.6 (ssh)

info,zhjwxk.cic,academic,learn,git GW
myhome passes this as well
118.229.9.6

net GW
118.229.8.6


Hypothesis proved (at nodes with 118.229.9.6 as GW!)
https://101.6.4.226/login.html
https://101.6.8.118/web/frame/login.html (server)




iperf
118.229.2.66 - 118.229.9.6
118.229.2.78 - 118.229.9.6