import ipaddress
import urllib.request
import os

def ip_info():
    ip = input("IP: ")
    try:
        obj = ipaddress.ip_address(ip)
        print("Version:", obj.version)
        print("Privat:", obj.is_private)
        print("Global:", obj.is_global)
    except:
        print("Ungültige IP")

def public_ip():
    try:
        ip = urllib.request.urlopen("https://api.ipify.org").read().decode()
        print("Öffentliche IP:", ip)
    except:
        print("Fehler")

def ping_host():
    host = input("Host: ")
    os.system(f"ping -c 4 {host}" if os.name != "nt" else f"ping {host}")

def traceroute_host():
    host = input("Host: ")
    os.system(
        f"tracert {host}" if os.name == "nt" else f"traceroute {host}"
    )

def port_check():
    import socket
    host = input("Host: ")
    port = int(input("Port: "))
    try:
        with socket.create_connection((host, port), timeout=3):
            print("Port OFFEN")
    except:
        print("Port GESCHLOSSEN")
