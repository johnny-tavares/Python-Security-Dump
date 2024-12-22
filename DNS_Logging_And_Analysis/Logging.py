import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="dns_queries.log",
)
# Create a new logger for logging malicious IPs
malicious_logger = logging.getLogger('malicious_ips')
malicious_handler = logging.FileHandler('malicious_ips.log')  # Log to this file
malicious_handler.setLevel(logging.WARNING)  # Set level to WARNING for malicious IPs
malicious_formatter = logging.Formatter('%(asctime)s - %(message)s')
malicious_handler.setFormatter(malicious_formatter)
malicious_logger.addHandler(malicious_handler)

def log_query(domain, ips):
    logging.info(f"Queried domain: {domain} - IPs: {', '.join(ips)}")
def log_flaggedIP(domain, ip):
    malicious_logger.warning(f"Queried domain: {domain} - Flagged IP: {ip}")