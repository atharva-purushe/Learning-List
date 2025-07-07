$TTL 604800
@   IN  SOA ns1.atharvapurushe.com. admin.atharvapurushe.com. (
            3
            604800
            86400
            2419200
            604800 )

@    IN  NS   ns1.atharvapurushe.com.
ns1  IN  A    127.0.0.1
@    IN  A    172.19.0.2
www  IN  A    172.19.0.2
