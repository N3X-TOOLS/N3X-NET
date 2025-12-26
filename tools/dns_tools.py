import socket
import subprocess

def domain_to_ip():
    domain = input("Domain: ")
    try:
        print("IP:", socket.gethostbyname(domain))
    except:
        print("Fehler")

def ip_to_domain():
    ip = input("IP: ")
    try:
        print("Domain:", socket.gethostbyaddr(ip)[0])
    except:
        print("Kein Reverse-DNS")

def dns_records():
    domain = input("Domain: ")
    try:
        result = subprocess.check_output(
            ["nslookup", domain], stderr=subprocess.DEVNULL
        ).decode()
        print(result)
    except:
        print("DNS Lookup fehlgeschlagen")

def whois_lookup():
    domain = input("Domain: ")
    try:
        result = subprocess.check_output(
            ["whois", domain], stderr=subprocess.DEVNULL
        ).decode()
        print(result)
    except:
        print("WHOIS nicht verfügbar (evtl. Windows)")
