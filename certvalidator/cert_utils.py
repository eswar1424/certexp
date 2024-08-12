import socket
import ssl
import pprint
import csv
from datetime import datetime,timedelta

def get_ssl_certificate(hostname, port=443):
    # Create a socket and connect to the server
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, port)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            certificate = ssock.getpeercert()

    return certificate

#pretty print the certificate
def prety_print_cert(certificate) -> None:
    pprint.pprint(certificate)

def get_expiry_date(hostname) -> datetime:
    certificate = get_ssl_certificate(hostname)
    #print(certificate['notAfter'])
    gmt_time = datetime.strptime(certificate['notAfter'], "%b %d %H:%M:%S %Y %Z")
    #print(gmt_time)
    ist_time = gmt_time + timedelta(hours=5, minutes=30)

    print(ist_time)
    return ist_time
    


def get_expiry_dates_of_file(filepath):
    file = csv.reader(open(filepath))
    output_file = csv.writer(open("expiry_dates.csv","w"),lineterminator="\n")
    for row in file:
        hostname = row[0]
        expiry_date = get_expiry_date(hostname)
        output_file.writerow([hostname,expiry_date.date(),expiry_date.time()])





