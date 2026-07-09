# Main v2.0
# Author: DrFox

import time
try:
    import tool1
    import tool2
    import tool3
except ModuleNotFoundError as e:
    print(f"ERROR F404 Tool {e} NOT Found")

print(r"""    ______                 _                                     
   / ____/___  _  __      (_)____      ______________  ____  ___ 
  / /_  / __ \| |/_/_____/ / ___/_____/ ___/ ___/ __ \/ __ \/ _ \
 / __/ / /_/ />  </_____/ (__  )_____(__  ) /__/ /_/ / /_/ /  __/
/_/    \____/_/|_|     /_/____/     /____/\___/\____/ .___/\___/ 
                                                   /_/          """)


while True:
    user = input("Enter 1 For IP Scan 2 For Port Scan 3 For Banner Grabber OR X To exit: ").strip().upper()
    if user == "1":    
        try:
                tool1.main()
                time.sleep(0.5)
        except NameError:
            print("ERROR tool1 Is NOT found")

    elif user == "2":    
        try:
                tool2.main()
                time.sleep(0.5)
        except NameError:
            print("ERROR tool2 Is NOT found")

    elif user == "3":    
        try:
                tool3.main()
                time.sleep(0.5)
        except NameError:
            print("ERROR tool3 Is NOT found")

    elif user == "X":    
        print("EXTTING bye!")
        break

    else :
        print ("\nhmm That Doesn't Seem Right... Try 1,2,3 or x")