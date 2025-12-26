from core.helpers import clear, pause

from tools.dns_tools import (
    domain_to_ip, ip_to_domain, dns_records, whois_lookup
)
from tools.ip_tools import (
    ip_info, public_ip, ping_host, traceroute_host, port_check
)
from tools.web_tools import (
    http_headers, website_status, ssl_info, user_agent_test
)
from tools.utils_tools import (
    base64_encode, base64_decode, url_encode, url_decode
)

def main_menu():
    while True:
        print("""
[01] Domain → IP
[02] IP → Domain
[03] DNS Records
[04] WHOIS Lookup

[05] IP Infos
[06] Öffentliche IP
[07] Ping
[08] Traceroute
[09] Port Check

[10] HTTP Header
[11] Website Status
[12] SSL Zertifikat
[13] User-Agent Test

[14] Base64 Encode
[15] Base64 Decode
[16] URL Encode
[17] URL Decode

[00] Exit
""")

        choice = input("NOXNET > ").strip()
        clear()

        actions = {
            "1": domain_to_ip,
            "2": ip_to_domain,
            "3": dns_records,
            "4": whois_lookup,
            "5": ip_info,
            "6": public_ip,
            "7": ping_host,
            "8": traceroute_host,
            "9": port_check,
            "10": http_headers,
            "11": website_status,
            "12": ssl_info,
            "13": user_agent_test,
            "14": base64_encode,
            "15": base64_decode,
            "16": url_encode,
            "17": url_decode
        }

        if choice == "0":
            print("NOXNET beendet.")
            break
        elif choice in actions:
            actions[choice]()
            pause()
        else:
            print("Ungültige Auswahl")
            pause()
