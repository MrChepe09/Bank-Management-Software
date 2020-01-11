import time
import os
time.sleep(1)
print "\n"*10

while True:
    os.system('cls')
    print "Welcome WOLV99"
    print "-----MENU-----"
    time.sleep(1)
    print "(1)Create Account""\n""(2)Delete Account""\n""(3)Exit"
    time.sleep(1)
    a = input("Enter Your Choice(1/2/3): ")
    if a == 1:
        os.system('cls')
        import started

    elif a == 2:
        os.system('cls')
        import remove

    elif a == 3:
        print 4*"\t","THANK-YOU FOR VISITING"
        print 5*"\t","Have a Nice Day"
        break

    else:
        print "Wrong Choice Entered"
        time.sleep(1)
        pass







