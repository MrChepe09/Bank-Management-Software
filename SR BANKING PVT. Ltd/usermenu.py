import time
import os
time.sleep(1)
os.system('cls')
print 5*"\t","Welcome USER-17142589"
time.sleep(2)
while True:
    os.system('cls')
    print "---------MENU---------"
    time.sleep(1.5)
    print "(1)Check Balance""\n""(2)Deposit Cash""\n""(3)Withdraw Cash""\n""(4)Terms and Conditions""\n""(5)About Us""\n""(6)Exit"
    time.sleep(1)
    aa = input("Enter Your Choice(1/2/3/4/5/6): ")
    if aa == 1:
        import checkbalance
    elif aa == 2:
        import deposit
    elif aa == 3:
        import withdraw
    elif aa == 5:
        print "(1)About BANK""\n""(2)About DEVELOPERS"
        n = str(raw_input("Enter your Choice(1/2): "))
        if n == '1':
            import aboutbank
        elif n == '2':
            print 5*"\t","Coded/Programmes BY:- WOLV99"
            print 8*"\t","Tested BY:- YASHRAJ100"
            print 10*"\t","Sponsored BY:- HarshitPatel"
            print 12*"\t","Guided BY/Submitted TO :- Mrs. Rashmi Kori"
            a = raw_input("Press ENTER to continue; ")
    elif aa == 4:
        import Terms

    elif aa == 6:
        break
    else:
        print"Please Enter a valid Choice..."
        time.sleep(1)
        pass

