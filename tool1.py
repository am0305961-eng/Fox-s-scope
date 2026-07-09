# IP Scanner v2.0
# Author: DrFox

def main():
    import socket
    import threading

    print("Sanning IPs")

    ip = "192.168.1."

    def scan(ips):

        for port in [80 , 443 , 135 , 22 , 135 , 445 , 62078 , 8008 , 8009, 22]:

            s = socket.socket()

            s.settimeout(0.3)

            call = s.connect_ex((ips, port))
            s.close()

            if call == 0:
                print (f"{ips} is open!")
                break

            elif call in [10061,111]:
                print(f"{ips} Is Alive Connection Refused ")
                break

    threads = []
    for i in range (1 , 256):
        ips = ip + str(i)
        m = threading.Thread(target = scan , args = (ips,))
        threads.append(m)
        m.start()

    for thread in threads:
       thread.join()

    print("\nScan complete Returning to menu")