import dns.resolver #This is part of the dnspython library, not that you only import parts of it, and there is no namespace to import called dnspython

def get_ip_address(domain):
    try:
        #Query the ipv4 records, A means ipv4, AAAA is ipv6
        result = dns.resolver.resolve(domain, 'A')
        #Extract and return the IP addresses
        ips = []
        for ipval in result:
            ips.append(ipval.to_text())
        return ips
    except dns.resolver.NoAnswer:
        print(f"No DNS answer for {domain}")
    except dns.resolver.NXDOMAIN:
        print(f"Domain {domain} does not exist")
    except Exception as e:
        print(f"An error has occurred: {e}")

#tests
#get_ip_address('www.cloudflare.com')
