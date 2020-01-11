import time
import os
while True:
    os.system('cls')
    print "\t""--------------LOG-IN---------------"
    print "ARE YOU A""\n""(1)MANAGER""\n""(2)ACCOUNT HOLDER""\n""(3)EXIT"
    time.sleep(0.5)
    id = int(raw_input("Enter Your Choice(1/2/3): "))
    if id == 1:
        time.sleep(0.5)
        os.system('cls')
        print"\t""ACCOUNT LOG-IN"
        user = str.lower(raw_input("Enter Your Username: "))
        pas = str.lower(raw_input("Enter Your Password: "))
        if user == 'wolv99' and pas == 'srbank1234':
            time.sleep(1)
            print "LOG-IN Successful"
            import Menu
        elif user == 'yashraj223' and pas == 'rajput100':
            time.sleep(1)
            print "LOG-IN Successful"
            import Menu
        else:
            time.sleep(1)
            time.sleep(0.5)
            print "Wrong USERNAME or PASSWORD"
            time.sleep(1)
            print "Please Try Again"
            time.sleep(0.5)
    elif id == 2:
        import usermenu
    elif id == 3:
        break
    else:
        time.sleep(0.5)
        print "WRrong Choice entered"
        pass
