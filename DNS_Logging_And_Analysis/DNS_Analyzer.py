import DnsQuery
import Logging
#Note that this functionality immediately returns when it finds a bad ip, doesn't go through all if it exists
def analyze_ips(domain, ips, flagged_ips):
    for ip in ips:
        print(f"Checking ip: {ip}")
        if ip in flagged_ips:
            Logging.log_flaggedIP(domain, ip)
            return True
    return False
def read_malicious_ips(file_path):
    with open(file_path, 'r') as file:
        flagged_ips = [line.strip() for line in file.readlines()]
    return flagged_ips
#Query DNS
domain = input("Enter domain: ")
ips = DnsQuery.get_ip_address(domain)
Logging.log_query(domain, ips)
malicious_ip_found = analyze_ips(domain, ips, read_malicious_ips('Malicious_IPS.txt'))
if malicious_ip_found:
    print("Bad IP found")
else:
    print("No bad IP's")
