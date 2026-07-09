# Banner Grabber v1.0
# Author: DrFox

import socket
import ssl


def main():
    ip_traget = input("Enter The IP Of The Traget to Get the Banner: ").strip()
    def g_banner():
        try:

            r_pip = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            r_pip.settimeout(2)

            rules = ssl.create_default_context()
            rules.check_hostname = False
            rules.verify_mode = ssl.CERT_NONE

            s_pip = rules.wrap_socket(r_pip, server_hostname=ip_traget)

            s_pip.connect((ip_traget , 443))

            s_pip.sendall(b"GET / HTTP/1.1\r\n\r\n")

            banner = s_pip.recv(1024).decode(errors = "ignore")

            print("\n BANNER FOUND!: ")
            print(banner)

        except socket.timeout:
            print("\n[-] Error: Connection timed out. (The target might be offline or blocking us).")
        except ConnectionRefusedError:
            print("\n[-] Error: Connection refused. (Port 443 is closed on this device).")
        except Exception as e:
            print(f"\n[-] An unexpected error occurred: {e}")

    g_banner()