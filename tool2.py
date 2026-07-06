def main():
    # Port Scanner v2.0
    # Author: DrFox

    import socket
    import threading

    Target_ip = input("Enter The Target IP: ")

    def scan(ports):
        s = socket.socket()
        s.settimeout(0.1)
        call = s.connect_ex((Target_ip , ports))
        s.close()
        if call == 0:
            print(f"Port {ports} Is Open")

    print("Scanning...")
    for i in range (1 , 1025):
        g = threading.Thread(target=scan,args=(i,))
        g.start()

                            