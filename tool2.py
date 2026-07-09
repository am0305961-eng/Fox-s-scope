# Port Scanner v2.0
# Author: DrFox

def main():
    
    import socket
    import threading
    import time

    Target_ip = input("Enter The Target IP: ") #User Input

    def scan(ports): #Function 
        s = socket.socket() #We Make The Mobile Name it S
        s.settimeout(0.1) # Wait For 0.1 Before Moveing On
        call = s.connect_ex((Target_ip , ports)) # Connect to this IP And Port Then Close
        s.close() # Close the Moble
        if call == 0:
            print(f"Port {ports} Is Open")

    print("Scanning...")
    for i in range (1 , 1025): #LOOP From 1 to 1025
        g = threading.Thread(target=scan,args=(i,))
        g.start()


        time.sleep(0.001)