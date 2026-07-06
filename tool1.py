def main():
    import socket
    import threading

    print("Sanning IPs")

    ip = "192.168.1."

    def scan(ips):

        for port in [80 , 443 , 135 , 22]:

            s = socket.socket()

            s.settimeout(0.2)

            call = s.connect_ex((ips, port))
            s.close()

            if call == 0:
                print (f"{ips} is open!")
                break

            elif call == 10061:
                print(f"{ips} Connection Refused")
                break


    for i in range (1 , 256):
       
        ips = ip + str(i)
        m = threading.Thread(target = scan , args = (ips,))
        m.start()
