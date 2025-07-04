$TTL 604800
@   IN  SOA ns.atharva.puurshe.com. admin.atharva.puurshe.com. (
            1         ; Serial
            604800    ; Refresh
            86400     ; Retry
            2419200   ; Expire
            604800 )  ; Negative Cache TTL

@   IN  NS  ns.atharva.puurshe.com.
@   IN  A   192.168.1.100
ns  IN  A   192.168.1.100
