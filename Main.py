print (""" _____ ____ ___  _ _ ____    ____  ____ ____  ____  _____
/    //  _ \\  \//|// ___\  / ___\/   _Y  _ \/  __\/  __/
|  __\| / \| \  /   |    \  |    \|  / | / \||  \/||  \  
| |   | \_/| /  \   \___ |  \___ ||  \_| \_/||  __/|  /_ 
\_/   \____//__/\\  \____/  \____/\____|____/\_/   \____\
                                                         """)

import time



while True:
    user = input("\n1 For IP Scanner 2 For Port Scanner X To EXIT: ").strip().upper()
    if user == "1":
        try:
            import tool1
            tool1.main()
            time.sleep(0.5)

        except ModuleNotFoundError:
            print("ERROR FILE NOT FOUND!")

    elif user == "2":
        try:
            import tool2
            tool2.main()
            time.sleep(0.5)
        except ModuleNotFoundError:
            print("ERROR FILE NOT FOUND!")

    elif user == "X":
        print("Bye")
        break

    else:
        print("\n1 OR 2 ONLY!")