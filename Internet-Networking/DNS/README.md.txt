# Story : DNS 

# Objective : Gain practical experience with DNS by tracing DNS queries and setting up a DNS server.

## TASK 1 : DNS Query Tracing
    - I performed DNS query tracing by taking a website(www.instagram.com) 
    - Entered nslookup interactive mode and sent a query.

C:\Users\Atharva Purushe>nslookup
Default Server:  dsldevice.lan
Address:  192.168.1.1

> 163.70.144.174
Server:  dsldevice.lan
Address:  192.168.1.1

Name:    instagram-p42-shv-02-bom2.fbcdn.net
Address:  163.70.144.174

> instagram.com
Server:  dsldevice.lan
Address:  192.168.1.1

Non-authoritative answer:
Name:    instagram.com
Addresses:  2a03:2880:f288:1e2:face:b00c:0:4420
          163.70.144.174

> exit

## Task 2 : DNS Server Hosting
    - Setup a BIND9 DNR server using Dockers and mounted my own configuration files in the docker 
    - Defined the DNS zone for atharva.purushe.com and then mapped the domain to the IP 192.168.1.100
    - Verified it by using nslookup
Task2:.
│  docker-compose.yml
│
└───bind
    │   named.conf
    │
    └───zones
            db.atharva.purushe.com
            managed-keys.bind
            managed-keys.bind.jnl

## Task 3 : DNS Server Config
    -Created a zone definition in BIND’s named.conf for atharva.purushe.com.
    -Wrote a zone file that maps atharva.purushe.com and ns.atharva.purushe.com to 192.168.1.100.
    -Restarted your DNS server using Docker Compose.
    -Verified the DNS resolution using nslookup

