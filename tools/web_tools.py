import requests
import ssl
import socket

def http_headers():
    url = input("URL: ")
    r = requests.get(url)
    for k, v in r.headers.items():
        print(f"{k}: {v}")

def website_status():
    url = input("URL: ")
    r = requests.get(url)
    print("Status Code:", r.status_code)

def ssl_info():
    host = input("Domain: ")
    ctx = ssl.create_default_context()
    with ctx.wrap_socket(socket.socket(), server_hostname=host) as s:
        s.connect((host, 443))
        cert = s.getpeercert()
        print(cert)

def user_agent_test():
    url = input("URL: ")
    r = requests.get(url, headers={"User-Agent": "NOXNET"})
    print("Status:", r.status_code)
